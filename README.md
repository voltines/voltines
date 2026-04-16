# voltines

The official Python client for extremely professional live music.

`voltines` is a tiny promotional Python package for **The Voltines**, a UK covers band. It gives you a CLI, opens links, and launches a small local app that embeds the band's YouTube playlist.

## Why does this exist?

Because it is funny to be available on PyPI.

## Install

```bash
pip install voltines
```

For local development:

```bash
git clone <your-repo-url>
cd voltines-v2
pip install -e .
```

## Commands

```bash
voltines about
voltines watch
voltines app
voltines gigs
voltines music
voltines contact
voltines setlist
voltines request "Mr. Brightside"
voltines heckle
voltines api
voltines links
```

## What the app does

`voltines app` starts a tiny local HTTP server and opens your browser to a branded mini app with:

- embedded YouTube playlist
- quick links to music, gigs, and contact pages
- current sample repertoire
- tongue-in-cheek copy

## Notes

- The package does **nothing** during `pip install` beyond installing itself.
- It only opens a browser when you run a command that explicitly does that.
- It uses the current Voltines website links and public pages.

## Real-world branding hooks

You can put these on posters, stickers, bios, or your site:

- "Available on PyPI"
- "Install the band: `pip install voltines`"
- "Developer-friendly covers band middleware"
- "Danger High Voltage. Also available as a Python package."

## Publish checklist

1. Create a GitHub repo.
2. Update the README clone URL.
3. Build the package:
   ```bash
   python -m build
   ```
4. Upload to TestPyPI or PyPI:
   ```bash
   python -m twine upload dist/*
   ```
5. Verify the package name `voltines` is available on PyPI before publishing.

## Sources for current copy

The package text and links are grounded in the public Voltines site, including the home page tagline, repertoire examples, and public pages for music, gigs, and contact. The site currently describes The Voltines as an "electrifying covers band," uses the heading "Danger High Voltage," lists sample covers such as "Mr. Brightside" and "Sex on Fire," and says the 2025 schedule is currently being arranged. citeturn677806view0turn677806view1turn677806view2turn677806view3


## Notes

- `voltines app` starts a local web app and keeps running until you press `Ctrl+C`.
