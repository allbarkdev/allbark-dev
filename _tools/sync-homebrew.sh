#!/bin/sh
# Copy the homebrew tools (allbark.dev/homebrew/) from a Cerberus checkout.
# They're built from allbarkdev/cerberus apps/homebrew; never edit homebrew/ by hand.
#   _tools/sync-homebrew.sh ../cerberus
set -eu
src="${1:?usage: _tools/sync-homebrew.sh <path to cerberus checkout>}"
(cd "$src" && pnpm install --frozen-lockfile && pnpm --filter homebrew build)
rm -rf homebrew
cp -R "$src/apps/homebrew/dist" homebrew
echo "Copied homebrew/ from $(cd "$src" && git rev-parse --short HEAD)"
