"""Mini local web app for The Voltines."""

from __future__ import annotations

import contextlib
import socket
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from string import Template

from . import __version__
from .data import (
    CONTACT_FORM_URL,
    CONTACT_URL,
    DESCRIPTION,
    GIGS_URL,
    GIG_STATUS,
    MUSIC_URL,
    PAST_GIGS,
    SETLIST,
    SITE_URL,
    TAGLINE,
    YOUTUBE_PLAYLIST_URL,
)

_TEMPLATE_PATH = Path(__file__).with_suffix("").parent / "templates" / "app.html"


def _find_free_port() -> int:
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _setlist_html() -> str:
    blocks: list[str] = []
    for section, songs in SETLIST.items():
        items = "".join(f"<li>{song}</li>" for song in songs)
        blocks.append(f"<section><h3>{section}</h3><ul>{items}</ul></section>")
    return "\n".join(blocks)


def _gigs_html() -> str:
    items = "".join(f"<li>{gig}</li>" for gig in PAST_GIGS)
    return f"<p>{GIG_STATUS}</p><ul>{items}</ul>"


def render_app_html() -> str:
    template = Template(_TEMPLATE_PATH.read_text(encoding="utf-8"))
    playlist_embed = YOUTUBE_PLAYLIST_URL.replace("playlist?list=", "embed/videoseries?list=")
    return template.safe_substitute(
        version=__version__,
        site_url=SITE_URL,
        music_url=MUSIC_URL,
        gigs_url=GIGS_URL,
        contact_url=CONTACT_URL,
        contact_form_url=CONTACT_FORM_URL,
        tagline=TAGLINE,
        description=DESCRIPTION,
        playlist_embed=playlist_embed,
        setlist_html=_setlist_html(),
        gigs_html=_gigs_html(),
    )


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        body = render_app_html().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003
        return


def _open_browser_later(url: str, delay: float = 0.35) -> None:
    def _target() -> None:
        time.sleep(delay)
        webbrowser.open(url)

    threading.Thread(target=_target, daemon=True).start()


def run_app(open_browser: bool = True) -> str:
    port = _find_free_port()
    server = ThreadingHTTPServer(("127.0.0.1", port), _Handler)
    url = f"http://127.0.0.1:{port}"
    if open_browser:
        _open_browser_later(url)
    print(f"Voltines app running at {url}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down Voltines app...")
    finally:
        server.shutdown()
        server.server_close()
    return url
