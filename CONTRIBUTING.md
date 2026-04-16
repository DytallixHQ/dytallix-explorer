# Contributing To dytallix-explorer

This repository is a docs-only service-surface map for the live explorer.

## Change Scope

- update the documented explorer page URL, API surface, and observed response
  shapes
- keep the repo honest about what is and is not publicly published
- do not present this repo as the hosted frontend source

## Validation

Run the alignment check before opening a PR:

```bash
python3 scripts/check_public_alignment.py
```

If the live response shape changed, update `public-surface.json` and the README
examples in the same PR.