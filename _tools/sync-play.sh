#!/bin/sh
# Copy the Cerberus web app (allbark.dev/play/) from a Cerberus checkout.
# It's built from allbarkdev/cerberus apps/app; never edit play/ by hand.
#   _tools/sync-play.sh ../cerberus
set -eu
src="${1:?usage: _tools/sync-play.sh <path to cerberus checkout>}"
(cd "$src" && pnpm install --frozen-lockfile &&
	CERBERUS_BASE=/play pnpm --filter app exec vite build --mode web)
rm -rf play
cp -R "$src/apps/app/dist" play
echo "Copied play/ from $(cd "$src" && git rev-parse --short HEAD)"
