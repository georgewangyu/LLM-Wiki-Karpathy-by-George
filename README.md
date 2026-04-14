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
  docs/
    PHILOSOPHY.md
    WORKFLOW.md
    AUTOLOGGING.md
  raw/
    README.md
  scripts/
    autolog_wiki_log.py
  wiki/
    log.md
    overview.md
    page-template.md
```

## Recommended Operating Loop

1. Add source artifacts (or references) to `raw/`.
2. Append a chronological entry to `wiki/log.md` for substantive work.
3. Update affected canonical pages in `wiki/` using `wiki/page-template.md`.
4. Refresh `wiki/overview.md` links when pages are added/renamed.
5. Track open system upgrades in `IMPROVEMENTS.md`.

## Logging Model

The log is intentionally separate from canonical pages:

- `wiki/log.md` is append-only chronology
- topic/project/entity pages are maintained current understanding

This mirrors the pattern used in larger private deployments:

- chronology first
- synthesis second
- explicit source map in both layers

## Autologging

This template includes a script skeleton:

- `scripts/autolog_wiki_log.py`

It can append a structured log entry after each substantive chat (or each
batch of actions) without coupling to any private platform details.

See:

- `docs/AUTOLOGGING.md`
- `docs/WORKFLOW.md`
- `AGENTS.md`

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

## Where To Start

1. Read `AGENTS.md` and `docs/PHILOSOPHY.md`.
2. Review `wiki/overview.md`.
3. Add your first log entry in `wiki/log.md`.
4. Create or update one canonical page in `wiki/`.
