# AGENTS

## Mission

Maintain this repository as a durable, navigable, source-grounded wiki that an
LLM and a human can both operate reliably.

## Layer Contract

- `raw/` holds source artifacts or source pointers.
- `wiki/` holds maintained synthesis pages.
- `wiki/overview.md` is the first entry point.

Do not collapse raw and synthesis into one layer.

## Priority Order

1. User instructions in chat
2. This file (`AGENTS.md`)
3. `CLAUDE.md` or `CLAW.md`
4. Repository docs (`README.md`, `wiki/`)

## Canonical Behavior

1. Read `wiki/overview.md` first before editing content pages.
2. Prefer updating existing pages over creating near-duplicates.
3. Keep each claim tied to a concrete source in frontmatter or Source Map.
4. Keep page scope tight; split pages only when a topic becomes clearly
   overloaded.
5. Keep summaries current; do not let stale guidance remain unmarked.

## Page Quality Bar

- Include explicit sections (`Summary`, `Current Understanding`,
  `Important Evidence`, `Open Questions`, `Related Pages`, `Source Map`) when
  applicable.
- Keep bullets concrete and testable.
- Avoid transcript dumping.
- Avoid generic claims that cannot be traced.

## Update Loop

1. Capture new source in `raw/` (or add source references).
2. Update affected pages in `wiki/`.
3. Update `updated` date in frontmatter for changed pages.
4. Ensure `wiki/overview.md` links reflect current page set.
5. If structural issues are discovered, add them to `IMPROVEMENTS.md`.

## Public-Safe Rules

- Never store secrets, tokens, private credentials, or private personal data.
- Never include private file paths from local machines in committed content.
- When using this template for public repos, assume all content may be read by
  others.
