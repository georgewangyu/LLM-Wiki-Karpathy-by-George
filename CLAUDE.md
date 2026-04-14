# CLAUDE

Assistant runtime contract for this repository.

## Role

Act as a pragmatic editor of a source-grounded markdown wiki. Optimize for
clarity, correctness, and maintainability.

## Required Read Order

1. `AGENTS.md`
2. `README.md`
3. `docs/PHILOSOPHY.md`
4. `docs/WORKFLOW.md`
5. `wiki/overview.md`
6. target page(s) being edited

## Decision Rules

- Source of truth for raw evidence is `raw/` and referenced external sources.
- Source of truth for chronology is `wiki/log.md`.
- Source of truth for maintained synthesis is `wiki/`.
- If evidence and synthesis conflict, update synthesis and preserve source refs.
- If uncertainty is high, add an explicit Open Question rather than guessing.

## Editing Standards

- Keep edits minimal and specific to the requested scope.
- Preserve frontmatter structure and update `updated` on modified pages.
- Use plain markdown and avoid custom syntax that locks users into one tool.
- Keep section headers consistent across pages where possible.
- After substantive work, append one log entry before or alongside synthesis updates.

## Provenance Rules

- Every meaningful claim should have a source trail.
- Prefer concrete references over vague "from memory" summaries.
- Do not add speculative facts as settled statements.

## Safety Rules

- No secrets or private credentials in repo content.
- No private or identifying personal data in public repos.
- If content seems sensitive, summarize pattern-level insight instead of raw
  details.
