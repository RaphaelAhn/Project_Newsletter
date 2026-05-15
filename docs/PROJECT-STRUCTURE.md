# Project Structure

`Project_Newsletter` currently uses a small root-level layout with shared docs,
scripts, templates, and draft content.

## Current Tree

```text
Project_Newsletter/
├─ .env                 # Local runtime settings copied from .env.example
├─ .env.example         # Safe template for environment values
├─ .gitignore
├─ README.md
├─ SECURITY-CHECKLIST.md
├─ SECURITY-GUIDE.md
├─ TONEGUIDE.md
├─ settings.json        # Editor/workspace settings used by the project root
├─ game.json            # Edition config (game)
├─ it.json              # Edition config (IT)
├─ crypto.json          # Edition config (crypto)
├─ soccer.json          # Edition config (soccer)
├─ .vscode/
│  └─ settings.json     # Optional VS Code editor preferences
├─ docs/
│  ├─ PROJECT-STRUCTURE.md
│  ├─ edition-strategy.md
│  ├─ fact-check-guide.md
│  └─ prompts.md
├─ drafts/
│  └─ SAMPLE-2026-05-14.md
├─ scripts/
│  ├─ create_issue.py
│  ├─ publish_edition.py
│  └─ sources.json
└─ templates/
   └─ newsletter-template.md
```

## What Each Folder Does

- `docs/`: reference guides for writing, fact-checking, prompts, and structure.
- `drafts/`: generated or example newsletter drafts.
- `scripts/`: small automation scripts for draft creation and publishing.
- `templates/`: the shared markdown template used to build editions.
- `.vscode/`: optional editor convenience settings for this repo.

## Keep / Optional / Cleanup

### Keep

- `docs/`
- `scripts/create_issue.py`
- `scripts/publish_edition.py`
- `scripts/sources.json`
- `templates/newsletter-template.md`
- `drafts/` if you want sample or working drafts inside the repo

### Optional

- `.vscode/settings.json`
  Keep it if you want shared editor behavior across machines.
- `drafts/SAMPLE-2026-05-14.md`
  Keep it if you want an example output for onboarding or QA.

### Removed During Cleanup

- `scripts/factcheck.json`
  It was empty and not connected to the current scripts or documented workflow.

## Notes

- `.env` is intentionally local-only and should stay untracked.
- `published/` is not present yet; `scripts/publish_edition.py` creates it when
  you publish a draft.
