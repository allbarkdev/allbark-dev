# Working on allbark.dev

This is the source for [allbark.dev](https://allbark.dev), All Bark's site. It's public, so
everything committed here is world-readable, drafts and branches included.

## How the site is built

GitHub Pages builds `main` with its built-in Jekyll. There is no Actions workflow, no plugins and
no theme to maintain.

- HTML files **without** front matter (`/byte/*`, `/social/*`) are copied byte-for-byte. Keep
  them that way. App stores and platform reviewers link to these URLs, and they must never move:
  `/`, `/byte/privacy/`, `/byte/terms/`, `/byte/support/`, `/social/privacy/`, `/social/terms/`.
- Files **with** front matter (the home page and the devlog) go through Jekyll and Liquid.
- The home page (`index.html`, layout `_layouts/home.html`) leads with the latest Bark Blog post,
  then an **Apps** section with each public app's support, privacy and terms links. When an app gets
  new policy pages, add them as plain HTML under `/<app>/` and link them from its card there.
  `/social/*` is for our internal publishing tools: those pages stay live for platform review but
  aren't linked from the home page.
- Each public app has its own page, `/<app>/index.html` with `layout: app` (`/cerberus/`,
  `/byte/`), linked from its home card. It says what the app does with real screenshots only, and
  links that app's policy pages. Its link-preview card is rendered with
  `python3 _tools/og_image.py <app>/index.html`, using the page's `og_brand` and `og_url` in place of
  the blog's brand line and footer. Keep public claims in step with what the app's notes allow
  (no release dates, prices or untested features).
- The "Follow along" links in every footer come from `follow:` in `_config.yml`. Add a service
  there, not in a layout.
- Every page follows the visitor's system light/dark setting and falls back to dark when there
  isn't one. Dark tokens are the default in `assets/devlog/devlog.css` and in each policy page's
  inline `<style>`; light tokens sit under `prefers-color-scheme: light`.
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

1. **File name.** `_posts/2026-10-11-w41-short-slug.md`. The date is the day the post is drafted,
   in Pacific time (the site's `timezone`). The weekly routine runs Sunday at 8pm Pacific, so that's
   the Sunday that closes the ISO week, even though it's already Monday in UTC.
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
- Write from the developer's point of view. "I" is the developer (never named): their calls, their
  ideas, what they tested. "We" is the developer and the AI models working together. Be honest,
  specific and a bit funny. No hype, no marketing fluff, no personal framing like "after bedtime".
- Be open about the AI work without forcing it. When a model's part comes up naturally, name it
  ("Opus built...", "Fable handled..."). Check who did what in the app repo's `Co-Authored-By`
  commit trailers; don't guess.
- Sound like the developer talking, not a press release. Casual and conversational: contractions,
  short sentences, plain words ("tweaked", "tossed", "nope"), a little self-deprecating, with an
  occasional "honestly" or "pretty". Game references are welcome when they come from the notes.
  Keep the jokes in captions and asides, not in the facts.
- Don't quote the developer's feedback directly. Tell it in first person ("I wanted...") in the
  post's own voice, so the story keeps the why without publishing private messages.
- Keep posts to the dev work. Don't name other people (testers are "our Android tester" and so on).
- No AI-generated art in posts; every image is a real screenshot. The site covers more than one
  app, so don't claim "no AI art" for All Bark as a whole, only for the app a post is about when
  that's true.
- Feedback from the developer, testers or users is told as what was good and what we built on.
  Never frame it as someone getting the rules (or anything else) wrong.
- Only use facts that are in that week's notes (plus the commit trailers above for who built what).
  If something is unclear, ask in the notes repo instead of guessing. Nothing marked "Not public
  yet" goes in a post, a file name, an alt text or a commit message, except AI tooling and model
  names, which the developer has cleared.
- Don't name an unannounced app until its name is confirmed. Use a plain description ("our 5E
  character builder"). Cerberus is confirmed and can be named.
- Don't use "Dungeons & Dragons", D&D logos, or Wizards of the Coast trademarks or art. "5E" and
  "compatible with fifth edition" are fine.

### Workflow

1. The app project commits weekly notes to the private `allbarkdev/allbark-content` repo at
   `devlog/notes/YYYY-Www.md` (plus screenshots) on Sunday evening.
2. On Sunday at 8pm (Pacific), after the notes land, a routine checks for a `status: ready` notes
   file with no post yet. If it finds one, it drafts the post on a local branch and **shows it in the
   project thread for review**, rendered as it will look. It pushes nothing yet, because this repo is public.
   Questions about the notes go to `devlog/questions/YYYY-Www.md` in the notes repo.
3. After the owner OKs the draft in the thread, it becomes a PR here. **Merging the PR publishes
   the post.** Only the owner merges, and nothing is pushed straight to `main`.
4. After a post merges, its URL is added to `devlog/published.md` in the notes repo so the app
   project can link to it.
