# Data and Source Policy

## Principle

The project separates ancient/classical source facts from modern editions, translations, commentaries, and scans that may have copyright or licensing restrictions.

## Current repository data

The repository includes only small sample fixtures for pipeline validation. These fixtures are not a critical edition and are not intended as a full corpus.

## Source strategy

Candidate sources are stored in `data/source_manifest.jsonl` with license status and intended usage.

Full ingestion should use only:

- public-domain texts
- permissively licensed texts
- user-provided licensed texts
- approved scans or facsimiles
- bibliographic references where redistribution is not allowed

## Why not bundle a full corpus now?

Many versions and translations of the *Huangdi Neijing* exist online, but their licensing status differs. The project’s value is not owning a text copy; it is alignment, concept mapping, safe modernization, and source-grounded interpretation.
