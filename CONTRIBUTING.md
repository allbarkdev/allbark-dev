# Working on allbark.dev

This is the source for [allbark.dev](https://allbark.dev), All Bark's site. It's public, so
everything committed here is world-readable, drafts and branches included.

## How the site is built

GitHub Pages builds `main` with its built-in Jekyll. There is no Actions workflow, no plugins and
no theme to maintain.

- HTML files **without** front matter (`/`, `/byte/*`, `/social/*`) are copied byte-for-byte. Keep
  them that way. App stores and platform reviewers link to these URLs, and they must never move:
  `/`, `/byte/privacy/`, `/byte/terms/`, `/byte/support/`, `/social/privacy/`, `/social/terms/`.
- Files **with** front matter (the devlog) go through Jekyll and Liquid.
- `_config.yml` holds site settings and the devlog name. `README.md`, this file, `Gemfile` and
  `_tools/` are excluded from the build.

Local preview, if you want one: `bundle install && bundle exec jekyll serve`, then open
<http://localhost:4000/devlog/>. The `Gemfile` pins the same `github-pages` gem Pages uses.

## The Bark Blog (devlog)

A weekly deep dive into what got built that week, told from the developer's side. Tough outside,
kind heart: a scrappy, good-natured guard dog.

| Thing | Where |
| --- | --- |
| Index | `devlog/index.html` → `/devlog/` |
| Atom feed | `devlog/feed.xml` → `/devlog/feed.xml` |
| Post layout | `_layouts/post.html` (wraps `_layouts/devlog.html`) |
| Styles | `assets/devlog/devlog.css` (same parchment and green tokens as the rest of the site, with dark mode) |
| Posts | `_posts/YYYY-MM-DD-wNN-slug.md` → `/devlog/YYYY/wNN-slug/` |
| Screenshots and OG card | `assets/devlog/YYYY-wNN/` |

### Writing a post

1. **File name.** `_posts/2026-10-12-w41-short-slug.md`. The date is the day the post is drafted.
   **Never use a future date**, because Jekyll silently skips future-dated posts and the merge would
   publish nothing. The slug becomes the URL, so keep it short and don't change it after merging.
2. **Front matter.**

   ```yaml
   ---
   title: "The spell list that wouldn't stop scrolling"
   description: One sentence for the index, feed and link previews.
   week: 2026-W41
   app: 5E character builder
   image: /assets/devlog/2026-w41/og.png
   image_alt: What the link-preview card shows
   og_shot: /assets/devlog/2026-w41/spell-list.png   # optional, a screenshot to put on the card
   ---
   ```

3. **Screenshots.** Copy only the screenshots the post actually uses into `assets/devlog/YYYY-wNN/`.
   Use real captures from the app, never generated art. Embed them with:

   ```liquid
   {% include shot.html src="/assets/devlog/2026-w41/spell-list.png" alt="Describe what's on screen" caption="Optional caption" %}
   ```

   Phone captures display phone-sized. Add `wide=true` for landscape or desktop captures. Alt text
   is required: describe what the screenshot shows, not what it is. Crop very tall full-page
   captures to the part the paragraph is about.

   Short real screen recordings (MP4) use `{% include clip.html src=... poster=... label=... %}`.
   They never autoplay. Make the poster with
   `ffmpeg -ss 0.2 -i clip.mp4 -frames:v 1 clip-poster.png`.
4. **Open Graph card.** Run `python3 _tools/og_image.py _posts/<post>.md` (it needs Pillow). It
   writes the 1200×630 PNG named in `image`, with the title, the week badge and `og_shot` if one is
   set. Commit it with the post. `python3 _tools/og_image.py --default` rebuilds the card for the
   index.

### Voice and content rules

- Lead with the work. Pick the strongest one or two stories of the week and go deep rather than
  listing everything. Cover what shipped, the problem it solved, why we went that direction, the
  feedback that kicked it off or changed course, and what broke and how we fixed it.
- Write as "we". Be honest, specific and a bit funny. No hype, no marketing fluff, no personal
  framing like "after bedtime".
- Keep posts to the dev work. Don't name the developer, and don't discuss how the work gets done
  (tooling, process). That openness about being a one-person studio building with AI tooling
  belongs on the site's other pages, not in posts.
- No AI-generated art in posts; every image is a real screenshot. The site covers more than one
  app, so don't claim "no AI art" for All Bark as a whole, only for the app a post is about when
  that's true.
- Feedback from the developer, testers or users is told as what was good and what we built on.
  Never frame it as someone getting the rules (or anything else) wrong.
- Only use facts that are in that week's notes. If something is unclear, ask in the notes repo
  instead of guessing. Nothing marked "Not public yet" goes in a post, a file name, an alt text or a
  commit message.
- Don't name an unannounced app until its name is confirmed. Use a plain description ("our 5E
  character builder").
- Don't use "Dungeons & Dragons", D&D logos, or Wizards of the Coast trademarks or art. "5E" and
  "compatible with fifth edition" are fine.

### Workflow

1. The app project commits weekly notes to the private `allbarkdev/allbark-content` repo at
   `devlog/notes/YYYY-Www.md` (plus screenshots) on Sunday evening.
2. On Monday morning (Pacific), a routine checks for a `status: ready` notes file with no post yet.
   If it finds one, it drafts the post on a local branch and **shows it in the project thread for
   review**, rendered as it will look. It pushes nothing yet, because this repo is public.
   Questions about the notes go to `devlog/questions/YYYY-Www.md` in the notes repo.
3. After the owner OKs the draft in the thread, it becomes a PR here. **Merging the PR publishes
   the post.** Only the owner merges, and nothing is pushed straight to `main`.
4. After a post merges, its URL is added to `devlog/published.md` in the notes repo so the app
   project can link to it.
