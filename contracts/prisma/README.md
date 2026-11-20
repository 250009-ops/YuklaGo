# Prisma contract

`schema.prisma` is the database contract for Prisma ORM 7.10.1 (ADR 0008). It is not applied to a database in this repository yet.

When you scaffold `services/api`:

- Depend on `prisma@7.10.1` and `@prisma/client@7.10.1` exactly.
- Point the generator output at the API's generated folder, or leave the output path in this file and import from there.
- Put the connection string in `prisma.config.ts`. The database for staging and production is in Uzbekistan.
- Generate SQL migrations from this schema and commit the SQL.

Do not add a column for a passport image, an ERI key, a PIN, or a cabinet cookie.
