from __future__ import annotations

from pathlib import Path

from huggingface_hub import hf_hub_download


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIRECTORY = BASE_DIR / "models"

REPOSITORY_ID = "ggml-org/Qwen3-1.7B-GGUF"
MODEL_FILENAME = "Qwen3-1.7B-Q4_K_M.gguf"


def download_model() -> Path:
    """Download the Hugging Face GGUF model."""

    MODEL_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("=" * 68)
    print("ROX JARVIS HUGGING FACE MODEL DOWNLOADER")
    print("=" * 68)
    print(f"Repository : {REPOSITORY_ID}")
    print(f"Model file: {MODEL_FILENAME}")
    print(f"Save folder: {MODEL_DIRECTORY}")
    print("=" * 68)
    print("Downloading model. Please wait...")

    downloaded_path = hf_hub_download(
        repo_id=REPOSITORY_ID,
        filename=MODEL_FILENAME,
        local_dir=MODEL_DIRECTORY,
    )

    final_path = Path(downloaded_path)

    if not final_path.exists():
        raise FileNotFoundError(
            "The model download finished, but the model file "
            "could not be found."
        )

    print("\nModel downloaded successfully.")
    print(f"Model path: {final_path}")
    print(
        f"Model size: "
        f"{final_path.stat().st_size / (1024 ** 3):.2f} GB"
    )

    return final_path


if __name__ == "__main__":
    try:
        download_model()
    except KeyboardInterrupt:
        print("\nModel download cancelled.")
    except Exception as error:
        print(f"\nDownload failed: {error}")