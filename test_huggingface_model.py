from __future__ import annotations

import time

from app.core.huggingface_local_model import (
    generate_text,
    model_is_available,
)


def main() -> None:
    """Test the downloaded Hugging Face model."""

    print("=" * 68)
    print("ROX JARVIS LOCAL MODEL TEST")
    print("=" * 68)

    available = model_is_available()

    print(f"[MODEL AVAILABLE] {available}")

    if not available:
        print(
            "[ERROR] Model file was not found."
        )
        return

    print(
        "[STATUS] Loading model and generating response..."
    )

    started_at = time.perf_counter()

    response = generate_text(
        system_prompt=(
            "You are ROX JARVIS, a fast and helpful "
            "Windows desktop assistant. "
            "Respond using one short English sentence."
        ),
        user_prompt=(
            "Introduce yourself and say that you are ready."
        ),
        max_tokens=80,
    )

    elapsed_seconds = (
        time.perf_counter() - started_at
    )

    print("\n[ROX JARVIS RESPONSE]")
    print(response)

    print(
        f"\n[PROCESSING TIME] "
        f"{elapsed_seconds:.2f} seconds"
    )

    print("=" * 68)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[STATUS] Test cancelled.")
    except Exception as error:
        print(f"\n[ERROR] {error}")