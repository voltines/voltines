"""CLI for The Voltines."""

from __future__ import annotations

import argparse
import json
import random
import sys
import textwrap
import webbrowser

from . import __version__
from .app import run_app
from .data import (
    CONTACT_FORM_URL,
    CONTACT_URL,
    DESCRIPTION,
    FACEBOOK_URL,
    GIGS_URL,
    GIG_STATUS,
    INSTAGRAM_URL,
    MUSIC_URL,
    SETLIST,
    SITE_URL,
    TAGLINE,
    YOUTUBE_PLAYLIST_URL,
)

HECKLES = [
    "Play Wonderwall!",
    "Free Bird, but professionally!",
    "Can you make this wedding 12% more dangerous?",
    "More reverb. Less fear.",
    "This setlist needs additional voltage.",
]

BANNER = r"""
__     __   _ _   _
\ \   / /__| | |_(_)_ __   ___  ___
 \ \ / / _ \ | __| | '_ \ / _ \/ __|
  \ V /  __/ | |_| | | | |  __/\__ \
   \_/ \___|_|\__|_|_| |_|\___||___/
"""


def _print(text: str = "") -> None:
    print(text)


def cmd_about(_: argparse.Namespace) -> int:
    _print(BANNER)
    _print(TAGLINE)
    _print()
    _print(DESCRIPTION)
    _print()
    _print(f"Website:  {SITE_URL}")
    _print(f"Music:    {MUSIC_URL}")
    _print(f"Gigs:     {GIGS_URL}")
    _print(f"Contact:  {CONTACT_URL}")
    _print(f"YouTube:  {YOUTUBE_PLAYLIST_URL}")
    _print(f"Version:  {__version__}")
    return 0


def cmd_watch(_: argparse.Namespace) -> int:
    webbrowser.open(YOUTUBE_PLAYLIST_URL)
    _print("Opening the Voltines YouTube playlist...")
    return 0


def cmd_music(_: argparse.Namespace) -> int:
    webbrowser.open(MUSIC_URL)
    _print("Opening the music page...")
    return 0


def cmd_gigs(_: argparse.Namespace) -> int:
    webbrowser.open(GIGS_URL)
    _print("Opening the gigs page...")
    _print(GIG_STATUS)
    return 0


def cmd_contact(args: argparse.Namespace) -> int:
    target = CONTACT_FORM_URL if args.form else CONTACT_URL
    webbrowser.open(target)
    _print("Opening the contact page..." if not args.form else "Opening the booking form...")
    return 0


def cmd_app(_: argparse.Namespace) -> int:
    run_app(open_browser=True)
    return 0


def cmd_setlist(args: argparse.Namespace) -> int:
    if args.json:
        _print(json.dumps(SETLIST, indent=2))
        return 0
    for section, songs in SETLIST.items():
        _print(section)
        _print("-" * len(section))
        for song in songs:
            _print(f"- {song}")
        _print()
    return 0


def cmd_request(args: argparse.Namespace) -> int:
    song = " ".join(args.song).strip()
    if not song:
        _print("Please provide a song request.")
        return 2
    _print(f"Request logged: {song}")
    _print("Official response: excellent taste.")
    _print(f"To ask the actual humans, use: {CONTACT_FORM_URL}")
    return 0


def cmd_heckle(_: argparse.Namespace) -> int:
    _print(random.choice(HECKLES))
    return 0


def cmd_api(_: argparse.Namespace) -> int:
    payload = {
        "name": "The Voltines",
        "tagline": TAGLINE,
        "description": DESCRIPTION,
        "links": {
            "site": SITE_URL,
            "music": MUSIC_URL,
            "gigs": GIGS_URL,
            "contact": CONTACT_URL,
            "youtube": YOUTUBE_PLAYLIST_URL,
            "instagram": INSTAGRAM_URL,
            "facebook": FACEBOOK_URL,
        },
        "gigs_status": GIG_STATUS,
        "setlist_sections": list(SETLIST.keys()),
        "version": __version__,
    }
    _print(json.dumps(payload, indent=2))
    return 0


def cmd_links(_: argparse.Namespace) -> int:
    links = {
        "site": SITE_URL,
        "music": MUSIC_URL,
        "gigs": GIGS_URL,
        "contact": CONTACT_URL,
        "booking_form": CONTACT_FORM_URL,
        "youtube": YOUTUBE_PLAYLIST_URL,
        "instagram": INSTAGRAM_URL,
        "facebook": FACEBOOK_URL,
    }
    for key, value in links.items():
        _print(f"{key:12} {value}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="voltines",
        description="The official Python client for dangerously high-voltage covers.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """
            Examples:
              voltines app
              voltines watch
              voltines request "Mr. Brightside"
              voltines setlist --json
            """
        ),
    )
    parser.add_argument("--version", action="version", version=f"voltines {__version__}")

    subparsers = parser.add_subparsers(dest="command", required=True)

    commands = {
        "about": cmd_about,
        "watch": cmd_watch,
        "music": cmd_music,
        "gigs": cmd_gigs,
        "app": cmd_app,
        "heckle": cmd_heckle,
        "api": cmd_api,
        "links": cmd_links,
    }
    for name, func in commands.items():
        subparsers.add_parser(name).set_defaults(func=func)

    contact_parser = subparsers.add_parser("contact")
    contact_parser.add_argument("--form", action="store_true", help="Open the booking form directly.")
    contact_parser.set_defaults(func=cmd_contact)

    setlist_parser = subparsers.add_parser("setlist")
    setlist_parser.add_argument("--json", action="store_true", help="Print the setlist as JSON.")
    setlist_parser.set_defaults(func=cmd_setlist)

    request_parser = subparsers.add_parser("request")
    request_parser.add_argument("song", nargs=argparse.REMAINDER, help="Song title to request.")
    request_parser.set_defaults(func=cmd_request)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    func = args.func
    return int(func(args))


if __name__ == "__main__":
    sys.exit(main())
