from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]

@dataclass
class Signal:
    axis: str
    signal: str
    evidence: str
    confidence: float

@dataclass
class PatternLens:
    key: str
    label: str
    relevance: float
    signals: list[str]
    note: str

RED_FLAG_TERMS = ["chest pain", "difficulty breathing", "faint", "suicidal", "severe pain", "bleeding"]

class MockNeijingAtlasPipeline:
    """Runnable deterministic scaffold for the future model-backed pipeline."""

    def load_journal(self, path: str | Path | None = None) -> dict:
        path = Path(path) if path else ROOT / "fixtures" / "sample_daily_journal.json"
        return json.loads(path.read_text())

    def extract_signals(self, journal: dict) -> tuple[list[Signal], list[dict]]:
        text = (journal.get("free_text") or "").lower()
        checkin = journal.get("structured_checkin", {})
        flags = []
        for term in RED_FLAG_TERMS:
            if term in text:
                flags.append({"flag": term, "severity": "high", "action": "seek professional medical care"})

        signals: list[Signal] = []
        if "01:30" in str(checkin) or "slept at 1:30" in text:
            signals.append(Signal("rhythm", "late_sleep", "Slept at 1:30am", 0.95))
        if checkin.get("wake_energy", 10) <= 4 or "woke tired" in text:
            signals.append(Signal("energy", "morning_fatigue", "woke tired", 0.9))
        if "bloating" in str(checkin) or "bloated" in text:
            signals.append(Signal("digestion", "post_meal_bloating", "felt bloated after lunch", 0.88))
        if "cold_hands" in str(checkin) or "hands were cold" in text:
            signals.append(Signal("temperature", "cold_hands", "hands were cold in the morning", 0.9))
        if "humid" in str(checkin) or "humid" in text:
            signals.append(Signal("environment", "humid_weather", "rainy and humid", 0.86))
        if "irritable" in str(checkin) or "irritable" in text:
            signals.append(Signal("emotion", "irritability", "irritable in the afternoon", 0.82))
        return signals, flags

    def map_lenses(self, signals: list[Signal]) -> list[PatternLens]:
        keys = {s.signal for s in signals}
        lenses: list[PatternLens] = []
        if {"late_sleep", "morning_fatigue"} & keys:
            lenses.append(PatternLens("rhythm_strain", "Rhythm strain lens", 0.78, [s.signal for s in signals if s.axis in ["rhythm", "energy"]], "Late sleep and low morning energy suggest a rhythm/recovery observation lens."))
        if {"cold_hands", "humid_weather", "post_meal_bloating"} & keys:
            lenses.append(PatternLens("cold_damp_relevance", "Cold/damp relevance lens", 0.64, [s.signal for s in signals if s.signal in ["cold_hands", "humid_weather", "post_meal_bloating"]], "Cold sensation, humid context, and heaviness/bloating can be explored through a cold/damp traditional lens."))
        if {"post_meal_bloating", "morning_fatigue"} & keys:
            lenses.append(PatternLens("digestion_energy_link", "Digestion-energy link lens", 0.69, [s.signal for s in signals if s.axis in ["digestion", "energy"]], "Post-meal heaviness and fatigue are tracked together rather than as isolated metrics."))
        if "irritability" in keys:
            lenses.append(PatternLens("emotion_qi_movement", "Emotion-qi movement lens", 0.55, ["irritability"], "Irritability is mapped as an emotion-body coupling signal, not a diagnosis."))
        return lenses

    def retrieve_evidence(self, lenses: list[PatternLens]) -> list[dict]:
        rows = [json.loads(line) for line in (ROOT / "fixtures" / "sample_canon_passages.jsonl").read_text().splitlines() if line.strip()]
        wanted = set()
        for lens in lenses:
            if lens.key == "rhythm_strain":
                wanted.update(["yin_yang_rhythm", "regular_living", "avoid_overstrain"])
            if lens.key == "cold_damp_relevance":
                wanted.update(["seasonal_adaptation", "environment"])
            if lens.key == "emotion_qi_movement":
                wanted.update(["emotion_qi_relationship", "stress_body_coupling"])
        evidence = []
        for row in rows:
            if wanted.intersection(row.get("concepts", [])):
                evidence.append(row)
        return evidence

    def build_report(self, journal: dict) -> dict:
        signals, flags = self.extract_signals(journal)
        if flags:
            return {
                "journal_id": journal.get("journal_id"),
                "safe_to_interpret": False,
                "red_flags": flags,
                "message": "Some reported symptoms may require professional medical care. Pattern reflection is paused.",
            }
        lenses = self.map_lenses(signals)
        evidence = self.retrieve_evidence(lenses)
        return {
            "journal_id": journal.get("journal_id"),
            "safe_to_interpret": True,
            "not_diagnosis": True,
            "signals": [asdict(s) for s in signals],
            "pattern_lenses": [asdict(l) for l in lenses],
            "canon_evidence": evidence,
            "seven_day_observation_plan": [
                "bedtime and wake energy",
                "dinner timing and post-meal heaviness",
                "warm/cold drink preference",
                "stool tendency and bloating",
                "weather/humidity",
                "afternoon irritability or tension",
                "light movement after lunch",
            ],
            "safety_note": "Educational reflection only. This is not medical diagnosis, treatment, or prescription advice.",
        }

    def estimate(self) -> dict:
        return {
            "daily_entries": 10000,
            "stages_per_entry": 7,
            "weekly_reports": 1500,
            "canon_passage_processing": 20000,
            "estimated_model_calls": 10000 * 7 + 1500 * 4 + 20000 * 5,
            "estimated_tokens_pilot": "1B-5B",
            "estimated_tokens_scaled": "50B-200B+",
            "note": "Planning estimate only; real usage depends on context size, languages, safety review, and corpus alignment.",
        }
