# Kirill Lalayants — personal website

Static, bilingual portfolio for GitHub Pages. English (default): `/`; Russian: `/ru/`. The old `/en/` address redirects to `/`.
The pages work without JavaScript and use system fonts with no third-party runtime dependencies.

## Update

Edit the content in `scripts/build.py`, then run:

```sh
python3 scripts/build.py
```

Commit both generated HTML files. Edit presentation in `assets/css/style.css`.
Replace the PDFs in `assets/cvs/` when the CV changes; their existing filenames are preserved for inbound links.
The November 2026 update uses the English and Russian CVs from the local CV project.

## Preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. A build service and package installation are unnecessary.

## Search and deployment

The production origin is `https://lalayants.github.io`. Each language has a self-referencing canonical and reciprocal hreflang links. Both pages include profile structured data and social preview metadata. `robots.txt` declares `sitemap.xml`.

Serve the repository root with GitHub Pages. Keep `.nojekyll` so the generated files are served directly. If the domain changes, update `ORIGIN` in `scripts/build.py`, `robots.txt`, and `sitemap.xml`, then regenerate the HTML.

After publication, submit `https://lalayants.github.io/sitemap.xml` in the owner's Google Search Console and Yandex Webmaster accounts. Verification and search indexing depend on those services and are not performed by the static site.
