# LLM Wiki Karpathy by George

Public starter for running a markdown wiki as an agent-managed knowledge layer.

This repository is intentionally data-free. It captures structure, operating
contracts, and templates that came out of a real private implementation, but it
does not include private notes, personal logs, or credentials.

## Why This Exists

A context window is not durable memory.

The practical pattern is to separate layers:

- `raw/`: source artifacts (notes, exports, references, logs)
- `wiki/`: maintained current-best synthesis pages
- agent docs (`AGENTS.md`, `CLAUDE.md`, `CLAW.md`): operating behavior

This avoids two common failure modes:

1. Storing only transcripts and hoping retrieval will stay good.
2. Over-structuring too early and turning the system into schema overhead.

## Philosophy

- Keep synthesis pages small, explicit, and source-backed.
- Prefer incremental updates to existing pages over duplicate page creation.
- Separate canonical source material from derived understanding.
- Preserve provenance so any claim can be traced back to evidence.
- Keep the public template generic and reusable.

## Journey Notes (Sanitized)

This template reflects lessons from building a larger private wiki:

- a derived wiki works best when updated during normal work, not only in batch jobs
- daily logs are high-signal chronological input for synthesis
- lightweight frontmatter is easier to keep consistent and Obsidian-friendly
- operating docs matter as much as folder structure

None of the private content is included here; only the reusable method.

## Included Structure

```text
LLM-Wiki-Karpathy-by-George/
  AGENTS.md
  CLAUDE.md
  CLAW.md
  IMPROVEMENTS.md
  raw/
    README.md
  wiki/
    overview.md
    page-template.md
```

## Recommended Operating Loop

1. Add source artifacts (or references) to `raw/`.
2. Update affected pages in `wiki/` using `wiki/page-template.md`.
3. Refresh `wiki/overview.md` links when pages are added/renamed.
4. Track open system upgrades in `IMPROVEMENTS.md`.

## Frontmatter Convention

Use lightweight frontmatter on wiki pages:

- `title`
- `type` (`index`, `topic`, `project`, `entity`, etc.)
- `created`
- `updated`
- `sources`
- `tags`

## Public Safety

- Never commit secrets, private exports, credentials, or personal identifiers.
- If you need private overlays, keep them in a separate private repository.
- Treat this template as shareable by default.
