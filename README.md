# amantambi.github.io

Personal website for Aman Tambi. Plain HTML/CSS built from Markdown and YAML by a
~150-line Python script. No JavaScript toolchain, no theme to fight.

## Edit content

Everything you would normally change lives in `content/`:

| File | What it holds |
| --- | --- |
| `content/site.yaml` | name, status line, tagline, intro paragraph, links, nav |
| `content/projects/*.md` | one file per project (front matter + Markdown body) |
| `content/experience.yaml` | jobs, newest first |
| `content/publications.yaml` | papers, newest first |
| `content/education.yaml` | degrees |
| `content/teaching.yaml` | teaching and mentorship |
| `content/about.md` | the "About" paragraphs |
| `files/` | PDFs (resume) — served at `/files/…` |
| `static/media/` | images and videos — served at `/media/…` |

### Project front matter

```yaml
---
title: Perceptive Locomotion for the Unitree A2
org: FieldAI
role: Robotics Research Intern          # optional
period: May – Aug 2026
venue: ICRA 2025                        # optional
order: 1                                # sort key; lower = earlier
featured: true                          # true = card on the home page, false = "More work" list
page: true                              # false = no page, link out instead (needs `link:`)
summary: One or two sentences for the card.
tags: [Legged locomotion, RL]
highlights:                             # optional; first two show on the card, all on the page
  - value: "80%"
    label: fewer limb contacts vs. the blind baseline
media:                                  # card thumbnail (16:9 works best)
  type: video                           # video | image | placeholder
  src: /media/a2/stairs.mp4
  poster: /media/a2/stairs.jpg
  alt: Unitree A2 climbing stairs
hero:                                   # optional; page hero. Defaults to `media`.
  type: video
  src: /media/a2/stairs_full.mp4
  poster: /media/a2/stairs_full.jpg
  controls: true                        # show player controls instead of muted autoplay loop
  caption: Optional caption.
links:
  - label: Paper
    url: https://…
---

## Markdown body starts here
```

Figures in the body are plain HTML:

```html
<figure>
<img src="/media/a2/map.jpg" alt="…" loading="lazy">
<figcaption>Caption.</figcaption>
</figure>

<figure>
<video data-autoplay muted loop playsinline preload="metadata" poster="/media/a2/clip.jpg"><source src="/media/a2/clip.mp4" type="video/mp4"></video>
<figcaption>Caption.</figcaption>
</figure>
```

### Media guidelines

- Card thumbnails and heroes are 16:9. Videos: H.264 MP4, 1280 px wide, no audio, under ~4 MB, 10–40 s.
- `data-autoplay` videos play muted while on screen and pause when scrolled away.
- Keep the whole repo under GitHub's 1 GB soft limit; big raw videos go on YouTube/Drive with a link.

## Build and preview

```bash
pip install -r requirements.txt   # once
python build.py --serve           # http://localhost:8000, rebuilds on every save
python build.py                   # one-off build into site/
```

## Deploy

Pushing to `main` (or `master`) runs `.github/workflows/deploy.yml`, which builds the
site and publishes `site/` to GitHub Pages. One-time setup in the repo:
**Settings → Pages → Build and deployment → Source: GitHub Actions**.

## Layout

```
build.py        the builder
content/        what you edit
templates/      Jinja2 HTML (base.html, index.html, project.html, work.html, 404.html, _*.html macros)
static/         css/style.css, js/main.js, favicon.svg, media/
files/          PDFs
site/           output (git-ignored)
```
