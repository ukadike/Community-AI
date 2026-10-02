"""Participation objective for Community AI Node 0.1.

The prototype chooses among explicit candidate actions. It does not classify
people. Inputs describe community-declared access requirements and environmental
conditions.
"""

from typing import Dict, Iterable, List

from governance import GovernanceThresholds, evaluate_gates


ACCESS_DIMENSIONS = (
    "mobility",
    "pace",
    "reach",
    "sensory",
    "cognitive",
    "language",
    "environment",
    "agency",
)


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


def participation_score(
    access_state: Dict[str, float],
    action_support: Dict[str, float],
) -> float:
    """Score how well an action supports the current access state.

    Higher access-state values mean more support is currently required.
    The score weights action support by those requirements.
    """

    needs: List[float] = []
    supports: List[float] = []

    for dimension in ACCESS_DIMENSIONS:
        need = clamp01(access_state.get(dimension, 0.0))
        support = clamp01(action_support.get(dimension, 0.0))
        needs.append(need)
        supports.append(support)

    total_need = sum(needs)
    if total_need == 0:
        return sum(supports) / len(supports)

    weighted_support = sum(
        need * support for need, support in zip(needs, supports)
    )
    return weighted_support / total_need


def select_action(
    access_state: Dict[str, float],
    candidates: Iterable[Dict[str, object]],
    thresholds: GovernanceThresholds = GovernanceThresholds(),
) -> Dict[str, object]:
    """Select the highest-participation action that passes all governance gates."""

    evaluated = []

    for candidate in candidates:
        gates = evaluate_gates(candidate.get("governance", {}), thresholds)
        score = participation_score(
            access_state,
            candidate.get("supports", {}),
        )

        record = {
            "id": candidate.get("id"),
            "label": candidate.get("label"),
            "participation_score": round(score, 4),
            "governance": gates,
        }
        evaluated.append(record)

    eligible = [item for item in evaluated if item["governance"]["passes"]]

    if not eligible:
        return {
            "selected": None,
            "reason": "No candidate action passed all governance gates.",
            "evaluated": evaluated,
        }

    selected = max(eligible, key=lambda item: item["participation_score"])

    return {
        "selected": selected,
        "reason": "Selected the eligible action with the highest participation score.",
        "evaluated": evaluated,
    }
