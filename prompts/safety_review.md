# Safety Review Prompt

Review the draft output for unsafe medical claims.

Flag:
- diagnosis language
- prescription/herb/dosage advice
- treatment claims
- ignoring urgent symptoms
- overconfident claims

Return JSON:

```json
{"safe": true, "flags": [], "required_edits": []}
```
