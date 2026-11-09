# allbark.dev

The website for All Bark, a one-person indie studio. Served by GitHub Pages from `main`.

- `/` home: the latest Bark Blog posts, then an Apps section linking each app's page
- `/cerberus/` and `/byte/` app pages: what each app does, with real screenshots
- `/play/` the Cerberus web app, installable as a PWA (built in allbarkdev/cerberus, copied by `_tools/sync-play.sh`); `/t/<code>` table links without the app land in it
- `/homebrew/` homebrew pack checker and format guide for Cerberus (built in allbarkdev/cerberus, copied by `_tools/sync-homebrew.sh`)
- `/byte/*` and `/social/*` app policy and support pages (hand-written HTML, URLs fixed)
- `/devlog/` The Bark Blog, our weekly devlog (Jekyll posts in `_posts/`)

See [CONTRIBUTING.md](CONTRIBUTING.md) for how the site is built and how devlog posts are written.
