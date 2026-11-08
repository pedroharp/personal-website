# Pedro H. Pinto — Personal Website

Source for [pedroharp.github.io/personal-website](https://pedroharp.github.io/personal-website/): career, expertise,
selected work and contact.

This is a static site (plain HTML, CSS and JavaScript) with no build step.

## Structure

```
index.html   Landing page markup (content lives here)
styles.css   Design tokens, layout and components (case-study styles at the end)
main.js      Sticky nav, mobile menu, scroll reveal
assets/      Photos
```

There is deliberately no résumé on the site: résumés are tailored per application and sent directly.

## What can go public

The site names Dell and describes products by what they do. It leaves out internal project names, partner and
vendor names, and project-level dollar figures. FY26 totals are the only dollar figures on the site.

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
python -m http.server 8000
```

## Editing content

All copy lives in `index.html`; photos live in `assets/`. Colors and fonts
are set as CSS variables at the top of `styles.css`.

## Deploy (GitHub Pages)

1. In the repo, go to **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**, then pick `main` / `(root)`.
3. The site goes live at `https://<username>.github.io/<repo>/`.
4. To use a custom domain, add it under **Custom domain** and point your DNS at GitHub Pages.

Full-length case-study pages are parked on the `case-studies-draft` branch.
