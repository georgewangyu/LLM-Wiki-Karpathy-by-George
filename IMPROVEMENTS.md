# IMPROVEMENTS

## Philosophy + Workflow

- Add a `PHILOSOPHY.md` page that explains the layer model in one place:
  `raw` vs `wiki`, provenance, and why context windows are not durable memory.
- Add a `WORKFLOW.md` page with practical operating loops:
  source capture, synthesis updates, and review cadence.

## Automation

- Add a small script to rebuild `wiki/overview.md` from page metadata.
- Add an optional script to lint frontmatter consistency (`created`, `updated`,
  `sources`, `tags`).
- Add a script to flag pages with missing `Source Map` sections.

## Templates

- Add additional starter pages for `project`, `entity`, and `decision` types.
- Add a change-log template for major wiki restructuring events.
- Add a public-safe extraction template for sharing sanitized writeups.

## Safety

- Add a public-safe validation script to block accidental secret commits.
- Add a checklist for removing private identifiers before open-sourcing.
- Add pre-commit hooks for sensitive-pattern scanning.

## Onboarding

- Add a first-day setup checklist for new users and teams.
- Add examples for how to migrate an existing notes folder into this layout
  without losing history.
