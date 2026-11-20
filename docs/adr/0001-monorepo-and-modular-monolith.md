# ADR 0001 — Monorepo and a modular monolith

## Status

Accepted.

## Context

One contributor builds web, desktop, mobile shell, staff console, and API. The domains share the draft, the calculation, and the role rules. Splitting services per feature would duplicate the RBAC guards.

## Decision

One pnpm workspace. One NestJS API process with modules. A separate worker process consumes BullMQ jobs and imports the same packages. Clients are separate apps because they ship differently (browser, Electron, staff origin).

## Consequences

- `packages/calc`, `packages/checks`, `packages/domain`, and `packages/i18n` are imported by the API and, for calc display types, by the web app. The web app does not reimplement the fee formula.
- Horizontal scale is a later copy of the API process. It is not a microservice split.
- The staff console is a separate app so its origin and CSP stay apart from the client.
