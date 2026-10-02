"""Run the bundled Community AI Node 0.1 example."""

import json
from pathlib import Path

from src.participation import select_action


def main() -> None:
    scenario_path = Path("examples/neighborhood-scenario.json")
    scenario = json.loads(scenario_path.read_text(encoding="utf-8"))

    result = select_action(
        scenario["access_state"],
        scenario["candidates"],
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
