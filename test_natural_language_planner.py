from __future__ import annotations

import time

from app.core.natural_language_planner import (
    plan_natural_language_command,
)


TEST_COMMAND = (
    "Open Chrome, create a new tab, and search Google "
    "for AI engineering internships in India."
)


def main() -> None:
    """Test the local Hugging Face task planner."""

    print("=" * 68)
    print("ROX JARVIS HUGGING FACE PLANNER TEST")
    print("=" * 68)
    print(f"[COMMAND] {TEST_COMMAND}")
    print("[STATUS] Creating task plan...")

    started_at = time.perf_counter()

    result = plan_natural_language_command(
        TEST_COMMAND
    )

    elapsed_seconds = (
        time.perf_counter() - started_at
    )

    print("\n" + "=" * 68)
    print(f"[SUCCESS] {result.get('success', False)}")
    print(f"[STATUS] {result.get('status', 'unknown')}")
    print(f"[INTENT] {result.get('intent', '')}")
    print(f"[MESSAGE] {result.get('message', '')}")
    print(
        f"[PLANNING TIME] "
        f"{elapsed_seconds:.2f} seconds"
    )

    details = result.get("details")

    if details:
        print(f"\n[ERROR DETAILS]\n{details}")

    steps = result.get("steps", [])

    if steps:
        print("\n[PLANNED STEPS]")

        for step_number, step in enumerate(
            steps,
            start=1,
        ):
            print(
                f"\nStep {step_number}: "
                f"{step.get('description', '')}"
            )
            print(
                f"Tool: "
                f"{step.get('tool_name', '')}"
            )
            print(
                f"Arguments: "
                f"{step.get('arguments', {})}"
            )
    else:
        print("\n[PLANNED STEPS] No steps generated.")

    print("\n" + "=" * 68)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[STATUS] Planner test cancelled.")
    except Exception as error:
        print(f"\n[TEST ERROR] {error}")