# Autologging

This template supports autologging without hardcoding private platform details.

## Goal

After each substantive chat or action batch:

- append a structured entry to `wiki/log.md`
- then update canonical wiki pages as needed

## Included Script

- `scripts/autolog_wiki_log.py`

The script appends a log block with:

- date
- topic
- concise summary
- optional source refs

## Example

```bash
python3 scripts/autolog_wiki_log.py \
  --date 2026-04-13 \
  --topic "ingest" \
  --summary "Added initial topic pages from source exports." \
  --source "raw/exports/notes-2026-04-13.md" \
  --source "wiki/overview.md"
```

## Integration Ideas

- call script from your chat agent after meaningful task completion
- call script from a local wrapper/CLI that processes conversation transcripts
- use manual mode when updates are high-stakes and should be reviewed first

## Guardrails

- autolog only substantive milestones
- avoid logging secrets or private identifiers
- keep summaries short and factual
- treat log as chronology, not full synthesis
