#!/bin/sh
# Copy the herdr-critters mod into the Herdr app home. A symlink doesn't work:
# Herdr doesn't load a mod's images through one. Run again after each change.
set -eu
src="$(cd "$(dirname "$0")" && pwd)/mods/herdr-critters"
dest="${HERDR_APP_HOME:-$HOME/.config/herdr-app}/mods/herdr-critters"
mkdir -p "$dest"
rsync -a --delete --exclude jsconfig.json --exclude gpui-kit.d.ts "$src/" "$dest/"
herdr-app check "$dest"
