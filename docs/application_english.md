# NEIJING ATLAS — Token Application Draft

## Project name

NEIJING ATLAS — Traditional Body Pattern Intelligence Framework

## Short summary

NEIJING ATLAS is an AI-assisted body-signal tracking and reflection framework inspired by the *Huangdi Neijing* and classical Chinese medicine systems thinking.

The project does not diagnose or treat disease. Instead, it helps users organize everyday observations — sleep rhythm, energy, digestion, temperature, moisture, emotion, pain/tension, season, and work rhythm — into source-grounded traditional pattern lenses with confidence scores, safety boundaries, and 7-day observation plans.

## Why this matters

Modern health trackers usually collect isolated metrics: steps, calories, sleep hours, heart rate, glucose, or HRV. Those metrics are useful, but many people still struggle to understand how daily life patterns connect: late sleep with morning fatigue, stress with digestion, humid weather with heaviness, cold exposure with stiffness, or emotional tension with body discomfort.

Classical Chinese medical thought, especially the *Huangdi Neijing*, is pattern-first. It observes relationships between rhythm, food, emotion, climate, temperature, fluids, movement, and body sensation. NEIJING ATLAS explores how AI can transform that traditional systems lens into a safe, auditable self-observation framework for modern users.

## What the system builds

For each daily journal or check-in, the system:

1. Extracts body signals from free-form text and structured inputs.
2. Maps signals to non-diagnostic traditional pattern lenses.
3. Retrieves relevant classical concepts and passages.
4. Generates an accessible explanation with uncertainty and evidence.
5. Runs safety checks for medical red flags and prohibited advice.
6. Produces a 7-day observation plan.
7. Aggregates multi-day entries into weekly correlation reports.

## Safety boundary

NEIJING ATLAS is not a TCM diagnosis bot, herbal prescription bot, or medical treatment advisor.

It avoids claims such as “you have spleen qi deficiency” or “take this herb”. It uses safer language such as “spleen-stomach lens relevance”, “cold/damp signal cluster”, or “rhythm strain pattern”. The output is framed as educational reflection, not medical certainty. Severe, urgent, unusual, or high-risk symptoms are routed to professional medical care.

## Why this fits MiMo

The project requires several MiMo-relevant capabilities:

- **Deep reasoning** over ambiguous traditional concepts and modern journal language.
- **Long-context consistency** across concepts, passages, translations, and weekly logs.
- **Multilingual output** in English, Vietnamese, and Chinese.
- **Safety review** to prevent diagnosis, treatment, or prescription claims.
- **Structured batch processing** for journal entries, concept graphs, source passages, and review logs.
- **Optional multimodal OCR** for scanned classical editions or facsimile pages in later phases.

Planned model routing:

- **MiMo-V2.5-Pro** for concept reasoning, cross-reference, weekly synthesis, and multilingual explanation.
- **MiMo-V2.5-Flash** for signal extraction, JSON normalization, safety pre-checks, and cheaper batch review.
- **MiMo-V2.5-Omni** for OCR and visual analysis of scanned classical editions when licensed source images are available.

## Why this needs a large token allocation

The challenge is not simply translating the *Huangdi Neijing*. Many text copies and translations already exist. The hard problem is alignment and safe modernization:

- align passages across versions and translations
- normalize terminology across classical Chinese, modern Chinese, English, and Vietnamese
- build a concept graph from traditional categories
- map free-form daily journals into structured body signals
- retrieve source-grounded concepts for each interpretation
- generate safe, accessible explanations without medical diagnosis
- review outputs for red flags and prohibited claims
- summarize repeated correlations across multiple days or weeks

A single user-facing reflection may require extraction, concept mapping, source retrieval, translation comparison, safety review, explanation, and JSON validation. Weekly reports multiply that context across entries. Full corpus and multi-user pilot workflows can scale into very large token usage.

## Current stage

The repository is a serious pilot scaffold. It includes:

- product and safety documentation
- source/data policy
- token justification
- relational schema
- prompt templates
- sample canon passages
- sample daily journal fixture
- runnable mock pipeline
- public interactive prototype demo

Full model-backed processing will run after API quota is available.
