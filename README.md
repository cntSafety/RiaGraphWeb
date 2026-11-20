# RiaGraph website

A static website for RiaGraph. Open `site/index.html` locally, or serve the `site` directory with any static HTTP server. Run `python scripts/check.py` to validate local links.

The Pages workflow checks pull requests and publishes the `site` directory on pushes to `main`. In GitHub repository settings, set Pages > Build and deployment > Source to **GitHub Actions**. The default project Pages URL includes the repository name; all local links are relative so the site works at that path.

Content and structure were informed by the LadybugDB website. The RiaCore icon is from the RiaCore project and is used here as a visual reference; consult its project licensing when distributing this site.

## Artwork attribution

`site/riacore.png` is the RiaCore desktop icon, copied from [RiaCore](https://github.com/cntSafety/RiaCore/tree/main/apps/desktop-host/logo). RiaCore is distributed under GPL-3.0-or-later; its license text is included in `third-party/RiaCore-GPL-3.0.txt`. The original source and attribution are available in that repository.
