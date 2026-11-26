# Changelog

## [0.1.19](https://github.com/hebus/komitt/compare/v0.1.18...v0.1.19) (2026-11-26)


### Features

* select several PRs/MRs and copy their links for Slack ([e3532ac](https://github.com/hebus/komitt/commit/e3532ac1c7e7ee6207ad94958c7b8a68f36f2cda))
* select several PRs/MRs and copy their links for Slack ([8421095](https://github.com/hebus/komitt/commit/8421095b73a4f62ff1c8cfcd1531ee2197f88c6e))

## [0.1.18](https://github.com/hebus/komitt/compare/v0.1.17...v0.1.18) (2026-11-25)


### Bug Fixes

* **ci:** restore platforms dropped from latest.json by concurrent macOS jobs ([6c98c60](https://github.com/hebus/komitt/commit/6c98c608c3edfaf9954642fad7087f32d99add2c))
* **ci:** restore platforms dropped from latest.json by concurrent macOS jobs ([fcf76eb](https://github.com/hebus/komitt/commit/fcf76eb8c581f6f924e536fad27cafbdaa28590c))

## [0.1.17](https://github.com/hebus/komitt/compare/v0.1.16...v0.1.17) (2026-11-25)


### Bug Fixes

* **ci:** add the `format` field to latest.json for the GPUI updater ([bc5575a](https://github.com/hebus/komitt/commit/bc5575a43958f79d584179f5268bd4a64bd4a0ab))
* **ci:** add the format field to latest.json for the GPUI updater ([286c326](https://github.com/hebus/komitt/commit/286c3260077704ddcd7c04bf6d4f734ce4368ec6))

## [0.1.16](https://github.com/hebus/komitt/compare/v0.1.15...v0.1.16) (2026-11-25)


### Bug Fixes

* **ci:** fetch full history before amending the release commit ([d688424](https://github.com/hebus/komitt/commit/d688424ccbbadd73d67b1b9e806b0a0fbe8e447d))
* **ci:** fetch full history before amending the release commit ([390c077](https://github.com/hebus/komitt/commit/390c07769202f745cca1139158f326a2b5644afd))


### Reverts

* back to Tauri + React, with the post-GPUI app features ([#32](https://github.com/hebus/komitt/issues/32)) ([e01bc2f](https://github.com/hebus/komitt/commit/e01bc2f4d943c5507668e504b1a26cdbf1de6cf8))

## [0.1.15](https://github.com/hebus/komitt/compare/v0.1.14...v0.1.15) (2026-11-24)


### Features

* **card:** highlight upmerge PRs with a badge and background ([5ac9bff](https://github.com/hebus/komitt/commit/5ac9bffe84154825d72b923e23ab0bfa404a5b9d))
* **card:** highlight upmerge PRs with a badge and background ([8ccd1d8](https://github.com/hebus/komitt/commit/8ccd1d80dc87a3d81416c467cf3889120bee3d20))

## [0.1.14](https://github.com/hebus/komitt/compare/v0.1.13...v0.1.14) (2026-11-24)


### Features

* **card:** add copy URL button next to the title ([1d2374c](https://github.com/hebus/komitt/commit/1d2374c3f7a6a955324b4de060eb5512de221ecb))
* **card:** add copy URL button next to the title ([5564d2a](https://github.com/hebus/komitt/commit/5564d2ac5d125409c25193dc42707859c0944676))

## [0.1.13](https://github.com/hebus/pr-dashboard/compare/v0.1.12...v0.1.13) (2026-11-15)


### Bug Fixes

* **card:** revert merge PR/MR button ([b9cf582](https://github.com/hebus/pr-dashboard/commit/b9cf58269fe4666f8d7889a973233d73c88133ab))

## [0.1.12](https://github.com/hebus/pr-dashboard/compare/v0.1.11...v0.1.12) (2026-11-13)


### Features

* **card:** merge PR/MR from the app when mergeable ([dca4124](https://github.com/hebus/pr-dashboard/commit/dca41243747fb5d2029103e8eeb4531c5b1bbc44))
* **card:** merge PR/MR from the app when mergeable ([395bf23](https://github.com/hebus/pr-dashboard/commit/395bf23a981d8f78db9f9feb5aefbc350bb4966d))

## [0.1.11](https://github.com/hebus/pr-dashboard/compare/v0.1.10...v0.1.11) (2026-11-12)


### Features

* **settings:** support github.com alongside GitHub Enterprise ([ff0dec5](https://github.com/hebus/pr-dashboard/commit/ff0dec570793f738e0f127521c9b12eeccce965b))
* **settings:** support github.com alongside GitHub Enterprise ([7ef133b](https://github.com/hebus/pr-dashboard/commit/7ef133b10efbd313cd9a4de64830c518433d1cbf))

## [0.1.10](https://github.com/hebus/pr-dashboard/compare/v0.1.9...v0.1.10) (2026-11-12)


### Bug Fixes

* **ui:** make the scrollbar follow the mouse wheel on the PR list ([2046319](https://github.com/hebus/pr-dashboard/commit/2046319c824326f210e6c9a1f852d6e8d07fdd78))
* **ui:** make the scrollbar follow the mouse wheel on the PR list ([bf9bfe0](https://github.com/hebus/pr-dashboard/commit/bf9bfe039219d9fd749ca6e031e043187ef41f44))

## [0.1.9](https://github.com/hebus/pr-dashboard/compare/v0.1.8...v0.1.9) (2026-11-12)


### Features

* **ui:** show scrollbars on the PR list, notifications and Settings ([c4ae00d](https://github.com/hebus/pr-dashboard/commit/c4ae00dbf2ac47c001c3116abcd10377c329eeb0))
* **ui:** show scrollbars on the PR list, notifications and Settings ([c1fd71f](https://github.com/hebus/pr-dashboard/commit/c1fd71f1341bc053135ad9e793b386e0c775e014))

## [0.1.8](https://github.com/hebus/pr-dashboard/compare/v0.1.7...v0.1.8) (2026-11-11)


### Bug Fixes

* **release:** sign the installer with `cargo packager signer sign` ([d609b8d](https://github.com/hebus/pr-dashboard/commit/d609b8d3455671dc2e7784a773f5e6aea47a12b7))
* **release:** sign the installer with cargo packager signer sign ([6fb24d3](https://github.com/hebus/pr-dashboard/commit/6fb24d36c75c51386f56136f1a84360b8f05dfae))

## [0.1.7](https://github.com/hebus/pr-dashboard/compare/v0.1.6...v0.1.7) (2026-11-11)


### Features

* rewrite the app in Rust with GPUI, replacing Tauri + React ([2cb34c4](https://github.com/hebus/pr-dashboard/commit/2cb34c4c33b3b644c39ba4d3d13c94fac06c0c27))
* rewrite the app in Rust with GPUI, replacing Tauri + React ([c19adcb](https://github.com/hebus/pr-dashboard/commit/c19adcba6a681fc8a85b9cd386023664e1bb3d90))

## [0.1.6](https://github.com/hebus/pr-dashboard/compare/v0.1.5...v0.1.6) (2026-11-07)


### Features

* **ui:** show a badge when the latest pipeline failed ([035784a](https://github.com/hebus/pr-dashboard/commit/035784a68e36649f518a7a530b1583c15716d267))
* **ui:** show a badge when the latest pipeline failed ([29b048d](https://github.com/hebus/pr-dashboard/commit/29b048dbcebb6a5222b938652f98747f0b212f82))

## [0.1.5](https://github.com/hebus/pr-dashboard/compare/v0.1.4...v0.1.5) (2026-11-06)


### Features

* **settings:** show the installed app version ([4709b4b](https://github.com/hebus/pr-dashboard/commit/4709b4bde6c71695e488f848eee0b47800172d08))
* **settings:** show the installed app version ([0a2988b](https://github.com/hebus/pr-dashboard/commit/0a2988b2f03e66fffde8858d606fbbabb0f314a4))

## [0.1.4](https://github.com/hebus/pr-dashboard/compare/v0.1.3...v0.1.4) (2026-11-06)


### Bug Fixes

* **ui:** mention MRs in the search placeholder ([9c76917](https://github.com/hebus/pr-dashboard/commit/9c769174c59f62e6e17793d719f81759c1591d62))
* **ui:** mention MRs in the search placeholder ([86fedb0](https://github.com/hebus/pr-dashboard/commit/86fedb0e6227f5c6252896aa60d6d6cd32747cb3))
