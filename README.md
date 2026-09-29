# Personal Website

Source for my personal website: career, expertise, selected work and contact.

This is a static site (plain HTML, CSS and JavaScript) with no build step.

## Structure

```
index.html   Landing page markup (content lives here)
styles.css   Design tokens, layout and components
main.js      Sticky nav, mobile menu, scroll reveal
```

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
python -m http.server 8000
```

## Editing content

Every placeholder is wrapped in square brackets, e.g. `[Company]`, `[Outcome with a number]`.
Search for `[` in `index.html` to find them all. Colors and fonts are set as CSS variables at the top
of `styles.css`.

## Deploy (GitHub Pages)

1. In the repo, go to **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**, then pick `main` / `(root)`.
3. The site goes live at `https://<username>.github.io/<repo>/`.
4. To use a custom domain, add it under **Custom domain** and point your DNS at GitHub Pages.
