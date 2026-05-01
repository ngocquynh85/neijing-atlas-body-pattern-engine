# Architecture

## System overview

```text
Daily journal / check-in
→ SignalExtractor
→ PatternLensMapper
→ CanonEvidenceRetriever
→ SafetyReviewer
→ ReflectionGenerator
→ ObservationPlanBuilder
→ WeeklyCorrelationReporter
```

## Data model

Core entities:

- `canon_texts`
- `canon_passages`
- `translations`
- `concepts`
- `concept_edges`
- `body_signal_taxonomy`
- `journal_entries`
- `extracted_signals`
- `pattern_lens_runs`
- `evidence_links`
- `safety_flags`
- `reflection_reports`
- `review_notes`

## Pattern lens mapper

Signals are mapped to lenses with relevance scores and evidence, not diagnostic labels.

Example:

```json
{
  "lens": "cold_damp_relevance",
  "score": 0.62,
  "signals": ["cold_hands", "humid_weather", "post_meal_bloating"],
  "language": "medium relevance traditional lens, not diagnosis"
}
```

## Model routing

- Flash: extraction, normalization, lightweight safety check.
- Pro: concept reasoning, cross-reference, weekly synthesis.
- Omni: OCR for licensed scans/facsimiles in future phases.

## Auditability

Every output should store:

- input journal hash
- extracted signals
- pattern lenses
- evidence passages
- prompt version
- model name
- safety flags
- confidence score
- reviewer notes
