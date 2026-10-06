"""Writes every generated file of REO_Cheats from tools/cheat_list.py (the options, sites and data words) and
tools/owner_codes.py (the owner's codes, verbatim):

    python tools/gen_manifests.py

  mod.toml, mod.json, manifest.json   the mod's settings (RecompModTool / the game's mod manifest / Thunderstore)
  src/gen_cheats.h                    the site table, the conditions, the value and item tables the C code uses
  patches_sites.json                  every code-patch site the mod can write, for the game build
  README.md                           from tools/README.template.md, with the table of every cheat

The option keys the owner's saved settings use (mods/mod_config.json, "reo-cheats") keep their meaning."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cheat_list as C  # noqa: E402
import owner_codes as O  # noqa: E402

VERSION = '1.2.0'
NAME = 'Resident Evil Outbreak — Cheats'
SHORT = 'All of the regular release\'s cheats for Resident Evil Outbreak, each its own option, on the NTSC-U v2.00 disc'

MASTER_NAMES = {
    'armax': 'Action Replay MAX master code, (M) Must Be On by Codejunkies',
    'cb': 'CodeBreaker master code, Enable Code (Must Be On) by Code Master et al.',
    'gs': 'GameShark master code ([M] Must Be On, Alternate [M] Must Be On or Must Be On by MadCatz)',
}
STATUS_WORDS = {
    C.WORKS: 'WORKS AS WRITTEN on your disc',
    C.ADAPTED: 'ADAPTED TO YOUR DISC',
    C.SUBST: 'NOT DECODABLE, SUBSTITUTE FROM THE NAME (not a proven equivalent)',
    C.NOT: 'NOT WORKING ON YOUR DISC',
    C.MASTER: 'MASTER CODE',
    C.PARAM: 'VALUE',
    C.LEGACY: 'KEPT FROM AN OLDER VERSION',
}
STATUS_SHORT = {C.WORKS: 'works as written', C.ADAPTED: 'adapted to your disc',
                C.SUBST: 'not decodable: substitute from the name (valid costume bits)',
                C.NOT: 'not working on your disc', C.MASTER: 'master code', C.PARAM: 'value of the option above',
                C.LEGACY: 'kept setting'}
# the statuses that write something (their description and table row show what they do to the save)
ACTIVE = (C.WORKS, C.ADAPTED, C.SUBST)


# ---- the owner's codes ---------------------------------------------------------------------------------------------
def entry(ref):
    name, author, nth = ref
    found = [e for e in O.ENTRIES if e['name'] == name and e['author'].startswith(author)]
    assert len(found) > nth, ref
    return found[nth]


def form_text(ref):
    e = entry(ref)
    return '\n'.join([f'{e["name"]} by {e["author"]}', e['device']] + e['lines'])


def pnach_lines(section):
    secs = O.PNACH[section]
    out = []
    for s in secs:
        for ln in s['lines']:
            m = re.match(r'patch=\d+,EE,([0-9A-Fa-f]{8}),extended,([0-9A-Fa-f]{8})', ln)
            out.append(f'{m.group(1).upper()} {m.group(2).upper()}')
    return out


def pnach_text(o):
    parts = []
    for sec in o['pnach']:
        parts.append(f'[{sec}] ' + ' / '.join(pnach_lines(sec)))
    return '\n'.join(parts)


# ---- item values ---------------------------------------------------------------------------------------------------
FIX = {'Assualt Rifle Magazine (30)': 'Assault Rifle Magazine (30)', 'Hangun Rounds (15)': 'Handgun Rounds (15)',
       'G. Launcher0Burst Rounds (4)': 'G. Launcher-Burst Rounds (4)', 'Blue Herbs': 'Blue Herb',
       'Red Herbs': 'Red Herb', 'Security Rook Card Key': 'Security Room Card Key',
       '45 Auto Round (7)': '45 Auto Rounds (7)'}
TABLES = [t for t in O.ITEM_TABLES if not t.startswith('Untitled')]
PAST = 12


def canon(name):
    n = FIX.get(name, name)
    return n


def canon_key(name):
    return canon(name).lower()


def item_names():
    variants = {}
    for t in TABLES:
        for _, n in O.ITEM_TABLES[t]:
            variants.setdefault(canon_key(n), set()).add(canon(n))
    display = {}
    for k, vs in variants.items():
        # the spelling with the most capitalised words (First Aid Spray over First aid Spray)
        display[k] = sorted(vs, key=lambda s: (-sum(w[:1].isupper() for w in s.split()), s))[0]
    keys = sorted(display, key=lambda k: (k != 'nothing', display[k].lower()))
    return keys, [display[k] for k in keys]


ITEM_KEYS, ITEM_LABELS = item_names()
ITEM_CHOICES = ['Off'] + ITEM_LABELS + [f'Past the table +{j} (a character\'s own item, see the note)'
                                        for j in range(PAST)]


def choices_of(o):
    ch = o['choices']
    if ch == 'ITEMS':
        return ITEM_CHOICES, None
    if ch == 'ITEM_TABLES':
        return list(TABLES), None
    return ['Off'] + [label for label, _ in ch], [0] + [value for _, value in ch]


# ---- descriptions --------------------------------------------------------------------------------------------------
def description(o):
    parts = [o['what']]
    if o['note']:
        parts.append(o['note'])
    if o['forms']:
        codes = [form_text(o['forms'][0])]
        if len(o['forms']) > 1:
            codes.append('Also in your list as:\n' + '\n\n'.join(form_text(r) for r in o['forms'][1:]))
        parts.append('Your code:\n' + '\n\n'.join(codes))
    if o['pnach']:
        parts.append('Plain code (your pnach):\n' + pnach_text(o))
    if o['status'] in (C.WORKS, C.ADAPTED, C.SUBST, C.NOT, C.MASTER) and o['evidence']:
        parts.append(f'{STATUS_WORDS[o["status"]]}. ' + o['evidence'])
    elif o['evidence']:
        parts.append(o['evidence'])
    if o['status'] in ACTIVE:
        parts.append('Save data: ' + o['save'])
    if o['master'] in MASTER_NAMES and o['status'] != C.PARAM:
        name = MASTER_NAMES[o['master']]
        parts.append('Needs the ' + name + ('' if name.endswith('.') else '.'))
    text = '\n\n'.join(p for p in parts if p)
    assert len(text) <= 4096, (o['key'], len(text))
    return text


def label(o):
    base = o['label'] if o['group'] == C.G_MASTER or o['status'] == C.PARAM else f'{o["group"]}: {o["label"]}'
    if o['status'] == C.NOT:
        base += ' (does nothing on your disc)'
    elif o['status'] == C.SUBST:
        base += ' (code not decodable: substitute)'
    assert len(base) <= 128, (o['key'], len(base), base)
    return base


# ---- mod.toml / mod.json / manifest.json ---------------------------------------------------------------------------
def toml_str(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '"'


def counts():
    cheats = [o for o in C.OPTIONS if o['count']]
    by = {s: sum(1 for o in cheats if o['status'] == s) for s in (C.WORKS, C.ADAPTED, C.SUBST, C.NOT)}
    assert sum(by.values()) == len(cheats), by
    return len(cheats), by


N_CHEATS, BY = counts()
COUNT_TEXT = (f'{BY[C.WORKS]} work as written, {BY[C.ADAPTED]} adapted to your disc, {BY[C.SUBST]} not decodable '
              f'(costume codes: a substitute from the name, not a proven equivalent), {BY[C.NOT]} cannot work on your '
              'disc')

DESCRIPTION = f"""Every cheat of the owner's regular (original release) Resident Evil Outbreak (NTSC-U) list, each its own option: {N_CHEATS} cheats from Codejunkies (Action Replay MAX), Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 (CodeBreaker v7+), MadCatz and bungholio (GameShark v3-4 / Xploder v4), on SLUS-20765 disc version 2.00, the disc this recompilation runs (its game code has the Greatest Hits memory layout).
{BY[C.WORKS]} work as written, {BY[C.ADAPTED]} are adapted to your disc (moved only to a proven equivalent), {BY[C.SUBST]} could not be decoded and do what their name says instead (costume codes: a substitute with valid costume bits, not a proven equivalent), {BY[C.NOT]} cannot work on your disc and do nothing (the reason is in their description).
Every option shows your device code(s), the plain code and the evidence. A cheat applies only while the master code of its device is On.
Separate from "Resident Evil Outbreak — Greatest Hits Cheats": enable only one of the two."""

HOST_DESCRIPTION = (
    f'Every cheat of your regular Resident Evil Outbreak list, each its own option: {N_CHEATS} cheats '
    f'({COUNT_TEXT}). '
    'Grouped as in your list; each option shows your device code(s), the plain code and the evidence.\n\n'
    'Master codes: (M) Must Be On by Codejunkies (Action Replay MAX), Enable Code (Must Be On) by Code Master, '
    'Lajos Szalay, Jay007, VirusPunk, Jarnold83 (CodeBreaker v7+), and [M] Must Be On, Alternate [M] Must Be On or '
    'Must Be On by MadCatz (GameShark v3-4 / Xploder v4). A cheat applies only while the master code of its device is '
    'On; Off switches those cheats off and puts the game\'s original code back.\n\n'
    'Choice options return the index of the chosen entry (Off = 0). The switches are saved, but the cheats only take '
    'effect once the game runs mod code. Only one of the two cheat mods can be on.')


def write(path, text):
    with open(os.path.join(OUT, path), 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def gen_mod_files():
    lines = [
        '[manifest]',
        'id = "REO_Cheats"',
        f'version = "{VERSION}"',
        'display_name = ' + toml_str(NAME),
        'description = """\n' + DESCRIPTION + '\n"""',
        'short_description = ' + toml_str(SHORT),
        'authors = [ "RaccoonRecomp" ]',
        '# The game id of the disc this recompilation runs (SLUS-20765 v2.00); the same id REO_GreatestHits_Cheats and',
        '# REO_ModernCam use for it.',
        'game_id = "reo"',
        'minimum_recomp_version = "1.0.0"',
        'dependencies = []',
        'native_libraries = []',
        '',
        '[inputs]',
        'elf_path = "build/mod.elf"',
        'mod_filename = "REO_Cheats"',
        '# Function reference symbols for SLUS-20765 v2.00 (this mod references no game functions).',
        'func_reference_syms_file = "syms/reo.syms.toml"',
        'data_reference_syms_files = []',
        'additional_files = [ "thumb.png" ]',
    ]
    settings = []
    for o in C.OPTIONS:
        desc = description(o)
        lab = label(o)
        lines += ['', '[[manifest.config_options]]', 'id = ' + toml_str(o['key']), 'name = ' + toml_str(lab),
                  'description = ' + toml_str(desc)]
        d = {'key': o['key']}
        if o['kind'] == 'bool':
            lines += ['type = "Enum"', 'options = [ "Off", "On" ]',
                      'default = ' + toml_str('On' if o['default'] else 'Off')]
            d['type'] = 'boolean'
            d['default'] = bool(o['default'])
        elif o['kind'] == 'choice':
            ch, _ = choices_of(o)
            assert o['default'] in ch, (o['key'], o['default'])
            assert len(set(ch)) == len(ch), o['key']
            lines += ['type = "Enum"', 'options = [ ' + ', '.join(toml_str(c) for c in ch) + ' ]',
                      'default = ' + toml_str(o['default'])]
            d['type'] = 'choice'
            d['choices'] = ch
            d['default'] = o['default']
        else:
            lines += ['type = "Number"', f'min = {o["min"]}', f'max = {o["max"]}', 'step = 1', 'precision = 0',
                      'percent = false', f'default = {o["default"]}']
            d['type'] = 'integer'
            d['default'] = int(o['default'])
            d['min'] = int(o['min'])
            d['max'] = int(o['max'])
            assert o['min'] <= o['default'] <= o['max'], o['key']
        d['label'] = lab
        d['description'] = desc
        settings.append(d)
    write('mod.toml', '\n'.join(lines) + '\n')

    manifest = {
        'id': 'reo-cheats',
        'name': NAME,
        'version': VERSION,
        'author': 'RaccoonRecomp',
        'authors': ['Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 (codes, GameHacking.org)',
                    'Codejunkies (codes, GameHacking.org)', 'MadCatz (codes, GameHacking.org)',
                    'bungholio (codes, GameHacking.org)', 'nobody (Item Values tables, GameHacking.org)'],
        'description': HOST_DESCRIPTION,
        'icon': 'icon.png',
        'game': {'id': 'resident-evil-outbreak-file-1', 'revisions': ['slus-20765-v2.00']},
        'apiVersion': 1,
        'conflicts': [{'id': 'reo-greatest-hits-cheats',
                       'reason': 'Both cheat mods patch the same game code on your disc; enable one at a time.'}],
        'settings': settings,
    }
    assert len(HOST_DESCRIPTION) <= 4096
    write('mod.json', json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    write('manifest.json', json.dumps({'name': 'REO_Cheats', 'version_number': VERSION, 'website_url': '',
                                       'description': SHORT, 'dependencies': []}, indent=4) + '\n')
    assert len(SHORT) <= 250
    keys = [o['key'] for o in C.OPTIONS]
    assert len(keys) == len(set(keys)), 'duplicate keys'
    for k in keys:
        assert len(k) <= 64 and re.match(r'^[A-Za-z][A-Za-z0-9_]*$', k), k


# ---- src/gen_cheats.h ----------------------------------------------------------------------------------------------
def c_str(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


MASTER_C = {'armax': 'armax', 'cb': 'cb', 'gs': 'gs'}


def gen_header():
    cond_names = list(C.CONDS)
    h = ['// GENERATED by tools/gen_manifests.py from tools/cheat_list.py: do not edit.',
         '#ifndef __GEN_CHEATS_H__', '#define __GEN_CHEATS_H__', '', '#include "recomp_api.h"', '#include "reo_mem.h"',
         '#include "reo_master.h"', '']
    for i, n in enumerate(cond_names):
        h.append(f'#define REO_COND_{n} {i}')
    h += [f'#define REO_COND_COUNT {len(cond_names)}', '',
          'typedef struct { u32 addr; u32 word; } Reo_Guard;',
          'typedef struct { u32 cond; u32 value; } Reo_Choice;',
          'typedef struct { u32 pc; u32 original; u32 guardFirst; u32 guardCount; u32 choiceFirst; u32 choiceCount; '
          '} Reo_Site;', '']
    guards, choices, sites = [], [], []
    for s in C.SITES:
        gf, cf = len(guards), len(choices)
        guards += s['guards']
        choices += s['choices']
        sites.append((s, gf, len(s['guards']), cf, len(s['choices'])))
    h.append('static const Reo_Guard kReoGuards[] = {')
    h += [f'    {{ 0x{a:08X}u, 0x{w:08X}u }},' for a, w in guards]
    h += ['};', '', 'static const Reo_Choice kReoChoices[] = {']
    h += [f'    {{ REO_COND_{k}, 0x{v:08X}u }},' for k, v in choices]
    h += ['};', '', '// pc, original word, guards, replacements (the first whose condition is on wins).',
          'static const Reo_Site kReoSites[] = {']
    for s, gf, gc, cf, cc in sites:
        h.append(f'    {{ 0x{s["pc"]:08X}u, 0x{s["original"]:08X}u, {gf}, {gc}, {cf}, {cc} }}, '
                 f'// {s["image"]} {s["asm"]}')
    h += ['};', '']

    # the conditions
    h += ['// The conditions of the sites, once per frame: option On, its device\'s master code On, and the pad for a '
          'joker.', 'static inline void Reo_ComputeConds(u32* cond, u32* latch) {',
          '    u32 armax = Reo_MasterArmax();', '    u32 cb = Reo_MasterCodeBreaker();',
          '    u32 gs = Reo_MasterGameShark();', '    u32 on;', '']
    for n, c in C.CONDS.items():
        terms = []
        for key, val in c['opts']:
            terms.append(f'Reo_Opt({c_str(key)}) != 0' if val is None else f'Reo_Opt({c_str(key)}) == {val}')
        h.append(f'    on = {MASTER_C[c["master"]]} && ({" || ".join(terms)});')
        if 'joker' in c:
            a, v = c['joker']
            h.append(f'    cond[REO_COND_{n}] = on && Reo_Pad(0x{a:08X}u) == 0x{v:04X}u;')
        elif 'latch' in c:
            a, von, voff = c['latch']
            h += [f'    if (!on) {{', f'        latch[REO_COND_{n}] = 0;', '    } else {',
                  f'        u32 pad = Reo_Pad(0x{a:08X}u);',
                  f'        if (pad == 0x{von:04X}u) {{', f'            latch[REO_COND_{n}] = 1;',
                  f'        }} else if (pad == 0x{voff:04X}u) {{', f'            latch[REO_COND_{n}] = 0;', '        }',
                  '    }', f'    cond[REO_COND_{n}] = latch[REO_COND_{n}];']
        else:
            h.append(f'    cond[REO_COND_{n}] = on;')
    h += ['}', '']

    # value tables of the choice options (index 0 = Off)
    for o in C.OPTIONS:
        if o['kind'] == 'choice' and isinstance(o['choices'], list):
            _, vals = choices_of(o)
            h.append(f'static const u32 kVal_{o["key"]}[] = {{ ' + ', '.join(f'0x{v:X}u' for v in vals) + ' };')
    h.append('')

    # item tables
    h += [f'#define REO_KEY_ITEM_TABLE "bh_item_values_table"', f'#define REO_ITEM_TABLE_COUNT {len(TABLES)}',
          f'#define REO_ITEM_NAME_COUNT {len(ITEM_KEYS)}', f'#define REO_ITEM_PAST_COUNT {PAST}', '']
    for ti, t in enumerate(TABLES):
        ids = [ITEM_KEYS.index(canon_key(n)) for _, n in O.ITEM_TABLES[t]]
        h.append(f'// {t}')
        h.append(f'static const u8 kReoItemTable{ti}[] = {{ ' + ', '.join(str(i) for i in ids) + ' };')
    h.append('static const u8* const kReoItemTables[] = { ' +
             ', '.join(f'kReoItemTable{ti}' for ti in range(len(TABLES))) + ' };')
    h.append('static const u32 kReoItemTableLen[] = { ' +
             ', '.join(str(len(O.ITEM_TABLES[t])) for t in TABLES) + ' };')
    h += ['', 'typedef struct { const char* key; u32 addr; } Reo_Slot;', 'static const Reo_Slot kReoSlots[] = {']
    h += [f'    {{ {c_str(k)}, 0x{a:08X}u }},' for k, _, a in C.SLOTS]
    h += ['};', '']

    # save-data masks and per-character costumes
    h += ['typedef struct { const char* key; u32 addr; u32 bits; } Reo_Costume;', 'static const Reo_Costume kReoCostumes[] = {']
    for ch, ci in C.CHARS:
        for t in ('all', 'b', 'c'):
            if t == 'c' and ci not in C.FEMALE:
                continue
            bits = {'all': 3 if ci in C.FEMALE else 1, 'b': 1, 'c': 2}[t]
            h.append(f'    {{ {c_str(f"cb_costume_{ch.lower()}_{t}")}, 0x{0x0031FB64 + ci:08X}u, {bits} }},')
    h += ['};', '',
          'static const u32 kReoCollectionMask[6] = { ' + ', '.join(f'0x{w:08X}u' for w in C.COLLECTION_MASK) + ' };',
          'static const u32 kReoCostumeMask[2] = { ' + ', '.join(f'0x{w:08X}u' for w in C.COSTUME_MASK) + ' };',
          'static const u32 kReoNpcMask[3] = { ' + ', '.join(f'0x{w:08X}u' for w in C.NPC_MASK) + ' };',
          f'#define REO_INFINITY_BITS 0x{C.INFINITY_BITS:08X}u', '', '#endif', '']
    write(os.path.join('src', 'gen_cheats.h'), '\n'.join(h))


# ---- patches_sites.json --------------------------------------------------------------------------------------------
def gen_sites_json():
    opts = {o['key']: o for o in C.OPTIONS}
    sites = []
    for s in C.SITES:
        reps = []
        for k, v in s['choices']:
            c = C.CONDS[k]
            entry_ = {'word': f'0x{v:08X}', 'condition': k,
                      'options': [key for key, _ in c['opts']],
                      'optionValue': [val for _, val in c['opts']],
                      'master': {'armax': 'master_armax_codejunkies', 'cb': 'master_codebreaker_codemaster',
                                 'gs': ['master_gameshark_madcatz', 'master_gameshark_madcatz_alternate',
                                        'master_gameshark_madcatz_must_be_on']}[c['master']],
                      'cheats': [opts[key]['label'] for key, _ in c['opts']]}
            if 'joker' in c:
                entry_['joker'] = {'padHalfword': f'0x{c["joker"][0]:08X}', 'equals': f'0x{c["joker"][1]:04X}'}
            if 'latch' in c:
                entry_['latch'] = {'padHalfword': f'0x{c["latch"][0]:08X}', 'setWhen': f'0x{c["latch"][1]:04X}',
                                   'clearWhen': f'0x{c["latch"][2]:04X}'}
            reps.append(entry_)
        d = {'id': f'reo-cheats.{s["pc"]:08X}', 'image': s['image'], 'pc': f'0x{s["pc"]:08X}', 'kind': s['kind'],
             'original': f'0x{s["original"]:08X}', 'originalAsm': s['asm'],
             'guard': [{'address': f'0x{a:08X}', 'word': f'0x{w:08X}'} for a, w in s['guards']],
             'pnachGuard': s['pnach_guard'], 'replacements': reps}
        if s.get('note'):
            d['note'] = s['note']
        sites.append(d)
    doc = {
        'schemaVersion': 1,
        'mod': 'reo-cheats',
        'version': VERSION,
        'note': ('PRIVATE: code-patch sites of the owner\'s disc (SLUS-20765 v2.00), made from the owner\'s cheat files. '
                 'Keep outside any repository. Every word of game code REO_Cheats can write: the site (image, pc, '
                 'original word), the guard words that must hold, and each replacement word with the option(s) and '
                 'master code that switch it (the first replacement whose condition holds wins; none = original). '
                 'The mod writes these as memory writes (guard + write + restore); the game build compiles them in as '
                 'switchable sites so that the code stays native.'),
        'images': {
            'exe': 'sha256:06bd5fd7243144cd30cdd0c0023763a369738cb91b177b35e85f6a4782b4ca46',
            'game.bin': {'identity': 'xxh64:1b4bcbcfd81bd910', 'overlay': 'BIN\\2.DAT', 'codeStart': '0x00570040',
                         'codeEnd': '0x00708580'},
            'demo.bin': {'overlay': 'BIN\\1.DAT', 'codeStart': '0x00570040', 'codeEnd': '0x00588480',
                         'note': 'identity not computed here (the build takes it from the disc)'},
        },
        'sites': sites,
    }
    write('patches_sites.json', json.dumps(doc, indent=2, ensure_ascii=False) + '\n')


# ---- README.md -----------------------------------------------------------------------------------------------------
def md(s):
    return s.replace('|', '\\|').replace('\n', '<br>')


def gen_readme():
    tpl = open(os.path.join(HERE, 'README.template.md'), encoding='utf-8').read()
    rows = ['| # | Group | Cheat | Author | Your device code(s) | Plain code (your pnach) | On your disc | What the '
            'mod does, and the evidence | Save |', '|---|---|---|---|---|---|---|---|---|']
    n = 0
    for o in C.OPTIONS:
        if o['status'] == C.PARAM:
            continue
        if o['count']:
            n += 1
            num = str(n)
        else:
            num = '–'
        author = ', '.join(sorted({entry(r)['author'] for r in o['forms']})) if o['forms'] else '–'
        dev = '<br><br>'.join(md(form_text(r)) for r in o['forms']) or '–'
        pl = md(pnach_text(o)) or '–'
        what = o['what'] + (' ' + o['note'] if o['note'] else '')
        ev = (what + '<br>**Evidence:** ' + o['evidence']) if o['evidence'] else what
        save = o['save'] if o['status'] in ACTIVE else '–'
        rows.append(f'| {num} | {o["group"]} | **{md(o["label"])}** (`{o["key"]}`) | {md(author)} | {dev} | {pl} | '
                    f'**{STATUS_SHORT[o["status"]]}** | {md(ev)} | {md(save)} |')
    site_rows = ['| Site | Image | Original | Replacement(s) | Option(s) | Guard |', '|---|---|---|---|---|---|']
    for s in C.SITES:
        reps = '<br>'.join(f'0x{v:08X}' for _, v in s['choices'])
        keys = '<br>'.join('`' + '` / `'.join(k for k, _ in C.CONDS[c]['opts']) + '`' for c, _ in s['choices'])
        g = '<br>'.join(f'0x{a:08X} == 0x{w:08X}' for a, w in s['guards'])
        site_rows.append(f'| 0x{s["pc"]:08X} {md(s["asm"])} | {s["image"]} | 0x{s["original"]:08X} | {reps} | '
                         f'{keys} | {g} |')
    tables = '\n'.join(f'- {t}: values 0x00-0x{len(O.ITEM_TABLES[t]) - 1:02X}' for t in TABLES)
    text = (tpl.replace('{{VERSION}}', VERSION).replace('{{N_CHEATS}}', str(N_CHEATS))
            .replace('{{N_WORKS}}', str(BY[C.WORKS])).replace('{{N_ADAPTED}}', str(BY[C.ADAPTED]))
            .replace('{{N_SUBST}}', str(BY[C.SUBST]))
            .replace('{{N_NOT}}', str(BY[C.NOT])).replace('{{N_OPTIONS}}', str(len(C.OPTIONS)))
            .replace('{{N_ENTRIES}}', str(len(O.ENTRIES))).replace('{{CHEAT_TABLE}}', '\n'.join(rows))
            .replace('{{SITE_TABLE}}', '\n'.join(site_rows)).replace('{{ITEM_TABLES}}', tables)
            .replace('{{N_ITEM_NAMES}}', str(len(ITEM_KEYS))))
    assert '{{' not in text
    write('README.md', text)


if __name__ == '__main__':
    gen_mod_files()
    gen_header()
    gen_sites_json()
    gen_readme()
    print(f'{len(C.OPTIONS)} settings written ({N_CHEATS} cheats: {COUNT_TEXT}); {len(C.SITES)} code sites; '
          f'{len(ITEM_KEYS)} item names')
