# pcninja.pro

Source of the PcNinja website, served by GitHub Pages at https://www.pcninja.pro

- `index.html` – the landing page (plain HTML + CSS, no build step). Tool versions refresh
  themselves from each repo's latest GitHub release; the numbers in the HTML are the fallback.
- `assets/` – images (logo, desk photo, favicons)
- `robots.txt`, `sitemap.xml` – search-engine hints
- `CNAME` – tells GitHub Pages which custom domain this site answers on

To add a tool: copy one `<article class="tool">` block in `index.html`, change the name,
description, repo name in `data-repo`, and the two links.

Any push to `main` is published automatically within a minute or two.
