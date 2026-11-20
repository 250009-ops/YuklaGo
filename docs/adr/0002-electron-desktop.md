# ADR 0002 — Electron is the filing client

## Status

Accepted. Implements DEC-23 and DEC-28. Supersedes the automation review's preference for an extension-first client.

## Context

ed2 cannot be iframed (`X-Frame-Options: SAMEORIGIN`, observed 18.11.2026). Filling has to happen in a top-level window on the user's machine, because the ERI token is there. The automation review marked E-IMZO inside embedded Chromium as unknown.

## Decision

- Main filing client: Electron 45, Windows first, macOS next.
- The cabinet is a `BrowserView` / `WebContentsView` with `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true`, no remote-debugging port.
- Domain allow-list: mock cabinet always; `ed2.customs.uz`, `ed1.customs.uz`, and `cargo.customs.uz` only when `ED2_LIVE_AUTOMATION` is on.
- MV3 extension is the fallback when the app cannot be installed, and when E-IMZO does not work in the Electron window (`DESKTOP_EIMZO_COMPAT`, [UNVERIFIED]).
- YuklaGo code does not open a socket to `127.0.0.1:64443`. The cabinet page may.

## Consequences

- AC-14.8 is a release gate per OS: a key holder logs in to the mock and to ed2 with PFX, USB-TOKEN, and BAIK-TOKEN, and the signing dialog opens. Until that passes, that OS ships only with the extension fallback in place.
- Users must trust the desktop app because it hosts the page. Ship code-signed builds and signed auto-update. Mapping packs are signed too.
