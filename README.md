# RiaGraph website

The website is built with [Pelican](https://getpelican.com/). Its content lives in:

- `content/pages/docs.md` and `content/pages/cheatsheet.md`: Markdown guides. Each section has an HTML wrapper to retain its styling and anchor; write paragraphs, headings, links, and fenced code blocks in Markdown inside it.
- `content/home.yaml`: the landing page copy. The page layout is in `theme/templates/home.html`.
- `content/navigation.yaml`: the on-page links for the guides.
- `content/assets/`: the existing stylesheet and artwork. Shared page layouts are in `theme/templates/`.

## Build and preview

Install Python 3.12 and run:

```sh
python -m venv .venv
```

Activate the environment (`.venv\Scripts\Activate.ps1` on Windows or `source .venv/bin/activate` on macOS/Linux), then run:

```sh
pip install -r requirements.txt
pelican -s pelicanconf.py
python scripts/check.py
python -m http.server 8000 --directory dist
```

Open `http://localhost:8000/`. Re-run the Pelican command after content changes. `dist/` is generated output and should not be committed. Links are relative so the site works both at the repository Pages path and at a domain root.

The GitHub Pages workflow builds and checks every pull request. Pushes to `main` build the site and deploy the generated `dist/` directory. GitHub Pages must use **GitHub Actions** as its source.

Content and structure were informed by the LadybugDB website.

## Artwork attribution

`content/assets/riacore.png` is the RiaCore desktop icon, copied from [RiaCore](https://github.com/cntSafety/RiaCore/tree/main/apps/desktop-host/logo). RiaCore is distributed under GPL-3.0-or-later; its license text is included in `third-party/RiaCore-GPL-3.0.txt`. The original source and attribution are available in that repository.
