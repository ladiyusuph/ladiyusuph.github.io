# ladiyusuph.github.io

My personal portfolio: React Native work, how each project was built, and my open source library.

Live at https://ladiyusuph.github.io/

## Editing

- `index.html` is the source for the whole site. Every project page lives in it as a section that opens from its `#id` link, so there is one file to edit.
- `assets/` holds the favicon and the share image (`share.png`, 1200×630) that link previews show.

## Building

```
python3 build.py
```

This writes the finished site to `site/`, adding the page head (title, description, share image tags). Pushing to `main` builds and deploys it to GitHub Pages through `.github/workflows/pages.yml`.
