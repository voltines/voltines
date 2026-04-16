# voltines

The official Python client for extremely professional live music.

`voltines` is a tiny promotional Python package for **The Voltines**, a UK covers band. It gives you a CLI, opens links, and launches a small local app that embeds the band's YouTube playlist.

## Why does this exist?

Because it is fun to be available on PyPI.

## Install

```bash
pip install voltines
```

For local development:

```bash
git clone <your-repo-url>
cd voltines
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
- current covers repertoire

The app keeps running until you press `Ctrl+C`.

## Notes

- The package does **nothing** during `pip install` beyond installing itself.
- It only opens a browser when you run a command that explicitly does that.
- It uses the current Voltines website links and public pages.