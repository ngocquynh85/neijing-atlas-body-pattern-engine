# Decisions

## D-001 — Safety positioning

Use “traditional body-pattern tracking / reflection” instead of “TCM diagnosis”.

Accepted language:
- pattern lens
- signal cluster
- relevance
- observation plan
- source-grounded reflection

Rejected language:
- diagnose
- treat
- prescribe
- cure
- you have spleen qi deficiency

## D-002 — Project architecture

Use a small Python scaffold for credibility and portability. Keep the pipeline mockable so reviewers can run it without API credentials.

## D-003 — Corpus policy

Use small sample passages only. Store source references and licensing status in a manifest. Full corpus ingestion must use public-domain, licensed, or approved sources.
