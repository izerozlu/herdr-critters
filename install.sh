#!/bin/sh
# Copy the mods into the Herdr app home and add the layout's keys. A symlink
# doesn't work: Herdr doesn't load a mod's images through one. Run again after
# each change.
set -eu
root="$(cd "$(dirname "$0")" && pwd)"
home="${HERDR_APP_HOME:-$HOME/.config/herdr-app}"

# The pane collapse mods share collapse.js (mods can't import across folders).
for mod in pane-collapse-menu; do
  cmp -s "$root/mods/pane-collapse/collapse.js" "$root/mods/$mod/collapse.js" ||
    { echo "mods/*/collapse.js differ; make them equal first." >&2; exit 1; }
done

for mod in herdr-critters pane-collapse pane-collapse-menu; do
  dest="$home/mods/$mod"
  mkdir -p "$dest"
  rsync -a --delete --exclude jsconfig.json --exclude gpui-kit.d.ts "$root/mods/$mod/" "$dest/"
  herdr-app check "$dest"
done

# Add the keys from keys.json that are not bound yet. Never replace a binding.
python3 - "$root/keys.json" "$home/keys.json" <<'PY'
import json, os, sys
src, dest = sys.argv[1:3]
theirs = json.load(open(dest)) if os.path.exists(dest) else {}
added = False
for section, binds in json.load(open(src)).items():
    have = theirs.setdefault(section, {})
    for key, action in binds.items():
        if key not in have:
            have[key] = action
            added = True
            print(f"keys.json: added {section} {key} = {action}")
        elif have[key] != action:
            print(f"keys.json: kept {section} {key} = {have[key]} (not {action})")
if added:
    tmp = dest + ".tmp"
    with open(tmp, "w") as f:
        json.dump(theirs, f, indent=2)
        f.write("\n")
    os.replace(tmp, dest)
PY
