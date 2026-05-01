# Signal Extraction Prompt

Extract body signals from the user's journal. Return JSON only.

Rules:
- Extract observations, not diagnoses.
- Preserve uncertainty.
- Flag severe or urgent symptoms separately.
- Do not recommend treatment.

Schema:

```json
{
  "signals": [
    {"axis":"rhythm|energy|digestion|temperature|moisture|emotion|pain_tension|environment", "signal":"string", "evidence":"quoted user text", "confidence":0.0}
  ],
  "red_flags": [],
  "notes": []
}
```
