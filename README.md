# tkinter widget reference

A reference for Year 12 & 13 Digital Technology ākonga, covering the tkinter
widgets used to build a Python GUI — what each one is for, how to use it, and how
it maps onto the NCEA achievement standards (AS91896 at Level 2, AS91906 at Level 3).

## What's here

- `index.html` — the reference page students read (publish this with GitHub Pages).
- `styles.css` — the styling for the page. It must sit beside `index.html`; if the
  two are separated the page loads unstyled.
- One runnable demo per widget. Each is standalone and commented. Demos for
  interactive widgets include both a Level 2 version (runs by default) and a
  Level 3 class-based version with file persistence, switchable by one line at
  the bottom of the file.
- `capstone_app.py` — a complete class-based program combining many widgets with
  validation and JSON persistence; the bridge into Level 3 complexity.

### Layout of the guide

- **Foundations** — `foundations_demo.py` (the window, grid layout, control
  variables, event binding).
- **Core widgets (Level 2)** — Label, Button, Entry, Text, Frame, Checkbutton,
  Radiobutton, Combobox, Listbox, Scale/Spinbox, messagebox, filedialog.
- **Year 13 widgets (Level 3)** — Toplevel, Menu, Treeview, Scrollbar, Notebook,
  Canvas.
- **Capstone** — `capstone_app.py`.

## Conventions used throughout

So ākonga see one consistent style everywhere:

- The main window is always named `root` (the usual convention they will meet elsewhere).
- Every demo wraps its code in a function and runs it under `if __name__ == "__main__":`.
- Every code example on the reference page is a complete program — import, window,
  and `mainloop()` included — so it can be copied, pasted, and run as-is.
- All file operations use `encoding="utf-8"` so te reo Māori macrons (ā ē ī ō ū)
  read and write correctly. The reference snippets show this too.
- Widgets that exist in both the classic `tk` and themed `ttk` families include a
  short tk-vs-ttk comparison; `tk`-only and `ttk`-only widgets are flagged as such.

## Running the demos

tkinter ships with Python, so there is nothing extra to install. Open a demo in
VS Code with the Python extension and press Run, or from a terminal:

```
python entry_demo.py
```

Some demos (Entry/Listbox Level 3, the dialogs demo, and the capstone) write to
files — `names.txt`, `todo.txt`, `records.json` — in the folder you run them from.
That is expected. The included `.gitignore` keeps those generated files out of the
repository.

## Publishing the reference with GitHub Pages

1. Push these files to the repository (keep `index.html` in the root).
2. In the repo, go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**, select `main` and `/ (root)`,
   then **Save**.
4. After a minute the site is live at `https://<your-username>.github.io/<repo-name>/`.

Edit `index.html`, commit, and the live page updates automatically.

## One thing to update

The intro paragraph of `index.html` has a placeholder repo link
(`github.com/your-school/...`). Swap it for your real repo URL once it exists.
The per-widget demo links are already relative, so they work as soon as you push.
