#!/usr/bin/env python3
"""Add the `format` field to every platform of a Tauri `latest.json`.

`tauri-action` writes `{signature, url}` per platform. The GPUI builds of this
app (versions 0.1.7 to 0.1.15) read the same manifest with `cargo-packager-updater`,
which requires a `format` on *every* entry and rejects the whole file otherwise.
The Tauri updater ignores the extra field.

It also restores platforms that `tauri-action` lost: the two macOS jobs rewrite
`latest.json` at the same time and one of them can drop the other's entry. Missing
entries are rebuilt from the `.sig` files attached to the release.

Usage: add_updater_format.py latest.json [SIGS_DIR]   (rewrites the file in place)
  SIGS_DIR  folder with the release's `*.sig` files; without it nothing is restored.
"""
import json
import os
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


# Updater key -> release asset, as named by tauri-action for the product `pr-dashboard`.
# `{v}` is the version without the leading "v".
ASSETS = {
    "darwin-x86_64": "pr-dashboard_x64.app.tar.gz",
    "darwin-x86_64-app": "pr-dashboard_x64.app.tar.gz",
    "darwin-aarch64": "pr-dashboard_aarch64.app.tar.gz",
    "darwin-aarch64-app": "pr-dashboard_aarch64.app.tar.gz",
    "windows-x86_64-nsis": "pr-dashboard_{v}_x64-setup.exe",
    "windows-x86_64-msi": "pr-dashboard_{v}_x64_en-US.msi",
    "linux-x86_64": "pr-dashboard_{v}_amd64.AppImage",
    "linux-x86_64-appimage": "pr-dashboard_{v}_amd64.AppImage",
    "linux-x86_64-deb": "pr-dashboard_{v}_amd64.deb",
    "linux-x86_64-rpm": "pr-dashboard-{v}-1.x86_64.rpm",
}


def restore_missing(manifest: dict, sigs_dir: str) -> list:
    """Add the platforms whose installer and `.sig` are in the release but not in the manifest."""
    platforms = manifest["platforms"]
    if not platforms:
        return []
    # Same download folder as the entries tauri-action did write.
    base = next(iter(platforms.values()))["url"].rsplit("/", 1)[0]
    version = manifest["version"].lstrip("v")
    restored = []
    for key, template in ASSETS.items():
        if key in platforms:
            continue
        asset = template.format(v=version)
        sig_path = os.path.join(sigs_dir, asset + ".sig")
        if not os.path.isfile(sig_path):
            continue
        with open(sig_path, encoding="utf-8") as f:
            platforms[key] = {"signature": f.read().strip(), "url": f"{base}/{asset}"}
        restored.append(key)
    return restored


def main(path: str, sigs_dir: str = "") -> None:
    with open(path, encoding="utf-8") as f:
        manifest = json.load(f)
    platforms = manifest["platforms"]
    if sigs_dir:
        for key in restore_missing(manifest, sigs_dir):
            print(f"restored missing platform: {key}")
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
    main(*sys.argv[1:3])
