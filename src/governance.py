"""Governance gates for Community AI Node 0.1.

This module is intentionally deterministic. Candidate actions must satisfy
minimum access, privacy, and agency thresholds before they can be selected.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class GovernanceThresholds:
    access: float = 0.70
    privacy: float = 0.80
    agency: float = 0.80


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


def evaluate_gates(
    action_scores: Dict[str, float],
    thresholds: GovernanceThresholds = GovernanceThresholds(),
) -> Dict[str, object]:
    """Return gate results for one candidate action."""

    access = clamp01(action_scores.get("access", 0.0))
    privacy = clamp01(action_scores.get("privacy", 0.0))
    agency = clamp01(action_scores.get("agency", 0.0))

    gates = {
        "access": access >= thresholds.access,
        "privacy": privacy >= thresholds.privacy,
        "agency": agency >= thresholds.agency,
    }

    return {
        "scores": {
            "access": access,
            "privacy": privacy,
            "agency": agency,
        },
        "thresholds": {
            "access": thresholds.access,
            "privacy": thresholds.privacy,
            "agency": thresholds.agency,
        },
        "gates": gates,
        "passes": all(gates.values()),
    }
