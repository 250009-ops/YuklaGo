# ADR 0008 — Prisma ORM 7.10.1

## Status

Accepted.

## Context

On 20 November 2026 the `prisma` package's `latest` dist-tag is the 8.0.0 release candidate. The last general-availability line is 7.10.1. Prisma 8 also splits the client libraries (`@prisma/orm-postgres` and others) and still changes API details.

## Decision

The database contract is `contracts/prisma/schema.prisma`, written for Prisma 7.10.1. The connection URL lives in `prisma.config.ts` at implementation time, not in the schema, which matches Prisma 7.

Do not upgrade to Prisma 8 until it is generally available and an ADR replaces this one. The schema file remains the contract either way: migrate it deliberately, do not regenerate it from a different ORM without a review.

## Consequences

- Contributors install `prisma@7.10.1` and `@prisma/client@7.10.1` explicitly. `pnpm add prisma` would pick the release candidate.
- SQL migrations generated from this schema are the thing that runs against PostgreSQL. The schema is the review surface.
