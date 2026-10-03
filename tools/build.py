# Builds dist/vazrazhdane-datapack.zip from datapack/ plus structures/*.nbt.
# Run from anywhere:  python3 tools/build.py
import os, json, shutil, zipfile, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SRC = os.path.join(ROOT, 'datapack')
STAGE = os.path.join(ROOT, 'dist', 'stage')
OUT = os.path.join(ROOT, 'dist', 'vazrazhdane-datapack.zip')

if os.path.exists(STAGE):
    shutil.rmtree(STAGE)
shutil.copytree(SRC, STAGE)

# structures/*.nbt -> data/vazrazhdane/structure/*.nbt
dest = os.path.join(STAGE, 'data', 'vazrazhdane', 'structure')
os.makedirs(dest, exist_ok=True)
nbts = sorted(glob.glob(os.path.join(ROOT, 'structures', '*.nbt')))
for f in nbts:
    shutil.copy(f, dest)
print(f'{len(nbts)} structure file(s) copied')

# every JSON/mcmeta file must parse
bad = 0
for d, _, files in os.walk(STAGE):
    for n in files:
        if n.endswith(('.json', '.mcmeta')):
            p = os.path.join(d, n)
            try:
                json.load(open(p, encoding='utf-8'))
            except Exception as e:
                bad += 1
                print('INVALID JSON:', os.path.relpath(p, STAGE), e)
if bad:
    raise SystemExit(f'{bad} invalid JSON file(s)')

# warn about template pool entries that point to a missing .nbt
have = {os.path.splitext(os.path.basename(f))[0] for f in nbts}
pooldir = os.path.join(STAGE, 'data', 'vazrazhdane', 'worldgen', 'template_pool')
missing = set()
for d, _, files in os.walk(pooldir):
    for n in files:
        for e in json.load(open(os.path.join(d, n), encoding='utf-8')).get('elements', []):
            loc = e['element'].get('location', '')
            if loc.startswith('vazrazhdane:') and loc.split(':', 1)[1] not in have:
                missing.add(loc)
for m in sorted(missing):
    print('missing structure:', m)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for d, _, files in os.walk(STAGE):
        for n in files:
            p = os.path.join(d, n)
            z.write(p, os.path.relpath(p, STAGE))
print('built', os.path.relpath(OUT, ROOT))
