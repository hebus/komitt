#!/usr/bin/env python3
"""Add the `format` field to every platform of a Tauri `latest.json`.

`tauri-action` writes `{signature, url}` per platform. The GPUI builds of this
app (versions 0.1.7 to 0.1.15) read the same manifest with `cargo-packager-updater`,
which requires a `format` on *every* entry and rejects the whole file otherwise.
The Tauri updater ignores the extra field.

Usage: add_updater_format.py latest.json   (rewrites the file in place)
"""
import json
import sys

# `cargo-packager-updater` only knows these four values.
NSIS, WIX, APPIMAGE, APP = "nsis", "wix", "appimage", "app"


def format_for(key: str, url: str) -> str:
    name = url.lower().split("?")[0]
    if name.endswith(".exe") or key.endswith("-nsis"):
        return NSIS
    if name.endswith(".msi") or key.endswith("-msi"):
        return WIX
    if key.startswith("darwin"):
        return APP
    # AppImage, and deb/rpm which the packager does not know: no GPUI build ever
    # ran on Linux, so those entries only need to parse.
    return APPIMAGE


def main(path: str) -> None:
    with open(path, encoding="utf-8") as f:
        manifest = json.load(f)
    platforms = manifest["platforms"]
    # Tauri points the bare `windows-x86_64` key at the MSI; the GPUI builds were
    # installed with NSIS and an MSI would install next to them, not over them.
    if "windows-x86_64-nsis" in platforms:
        platforms["windows-x86_64"] = dict(platforms["windows-x86_64-nsis"])
    for key, platform in platforms.items():
        platform["format"] = format_for(key, platform["url"])
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1])
