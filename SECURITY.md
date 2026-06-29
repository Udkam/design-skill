# Security Policy

## Reporting

Open an issue or contact the maintainer through the repository's public contact channel if one is provided.

Do not include secrets, private screenshots, private repository links, customer data, or local machine paths in public issues.

## Repository Hygiene

This repository is intended for public reuse. Do not commit:

- API keys, tokens, passwords, or private keys;
- `.env` files with real values;
- private screenshots or recordings;
- local browser/session notes;
- personal user paths;
- private account names;
- machine-specific logs or cache files.

Run before publishing:

```bash
python scripts/check_public_hygiene.py .
```

The scanner is heuristic. Passing it does not guarantee that no sensitive data exists; review changes manually before release.
