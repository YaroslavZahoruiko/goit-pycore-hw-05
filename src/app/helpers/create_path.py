from pathlib import Path


def create_path(file_path):
    path = Path(file_path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"Path not found: {path}")

    return path
