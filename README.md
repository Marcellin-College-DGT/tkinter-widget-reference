# tkinter widget reference

A reference for Year 12 & 13 Digital Technology ākonga, covering the tkinter
widgets used to build a Python GUI — what each one is for, how to use it, and how
it maps onto the NCEA achievement standards (AS91896 at Level 2, AS91906 at Level 3).

## What's here

- `index.html` — the reference page (this is what students read).
- `label_demo.py`, `entry_demo.py`, `listbox_demo.py` — runnable demos, one per
  widget. Each is standalone and heavily commented. The Entry and Listbox demos
  include both a Level 2 version (runs by default) and a Level 3 class-based
  version with file persistence, switchable by one line at the bottom of the file.

## Running the demos

tkinter ships with Python, so there is nothing extra to install. Open a demo in
VS Code with the Python extension and press Run, or from a terminal:

```
python entry_demo.py
```

## Publishing the reference with GitHub Pages

1. Push these files to the repository (keep `index.html` in the root).
2. In the repo, go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**, select `main` and `/ (root)`,
   then **Save**.
4. After a minute the site is live at `https://<your-username>.github.io/<repo-name>/`.

Edit `index.html`, commit, and the live page updates automatically.

## Status

This is the pattern draft — three widgets (Label, Entry, Listbox) — built for review
before the full widget set is added.
