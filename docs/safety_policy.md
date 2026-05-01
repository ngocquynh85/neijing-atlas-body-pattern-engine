# Safety Policy

## Scope

NEIJING ATLAS is an educational and reflective body-pattern tracking framework. It is not a clinical product.

## Allowed output

- body signal summaries
- traditional pattern lenses
- source-grounded concept explanations
- uncertainty/confidence notes
- non-medical observation plans
- general lifestyle reflection such as tracking sleep time, meal timing, weather, stress, and energy

## Disallowed output

- diagnosis of diseases
- definitive TCM syndrome diagnosis
- herbal prescriptions
- dosage advice
- acupuncture or moxibustion treatment instructions
- claims to cure, treat, prevent, or manage disease
- advice to ignore medical care

## Preferred language

Use:

- “This resembles a pattern lens...”
- “Signals that may be relevant...”
- “Track this for 7 days...”
- “Consider discussing persistent or severe symptoms with a clinician.”

Avoid:

- “You have...”
- “This is spleen qi deficiency.”
- “Take...”
- “Use this treatment.”

## Red flags

If a user reports severe, sudden, persistent, or high-risk symptoms, the system should stop pattern interpretation and recommend professional medical care. Examples:

- chest pain
- difficulty breathing
- fainting
- severe abdominal pain
- high fever
- stroke-like symptoms
- uncontrolled bleeding
- suicidal ideation
- pregnancy-related concerning symptoms
- symptoms in infants/children or medically fragile users

## Safety architecture

1. Extract possible red flags before pattern interpretation.
2. Block diagnosis/prescription language in generation.
3. Attach safety notes to every interpretation run.
4. Store reviewer flags for future audit.
