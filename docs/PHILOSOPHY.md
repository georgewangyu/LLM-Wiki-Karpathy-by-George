# Philosophy

This template is based on one simple principle:

A context window is a working set, not durable memory.

Durable systems need files, explicit provenance, and repeatable update loops.

## Layered Model

- `raw/`: source artifacts and references
- `wiki/log.md`: chronological record of meaningful actions and decisions
- `wiki/*.md` (topic/project/entity pages): maintained synthesis

Each layer has a different job.

## Why Not Transcript-Only

- retrieval degrades as history grows
- unresolved contradictions accumulate silently
- important decisions become hard to find

Chronological log plus maintained synthesis avoids this drift.

## Design Principles

- evidence over vibes
- explicit uncertainty over fabricated certainty
- update existing canonical pages before creating new ones
- keep pages compact and navigable
- preserve source map for every meaningful claim

## Private/Public Boundary

This public template intentionally contains no private data.

For real deployments:

- keep private overlays in a separate private repo
- keep this structure reusable and shareable
- port methods, not sensitive content
