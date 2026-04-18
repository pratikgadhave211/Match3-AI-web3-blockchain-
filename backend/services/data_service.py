from __future__ import annotations

import json
from typing import Any

from backend.config import DATA_DIR, DATA_FILE_PATH


def ensure_data_store() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE_PATH.exists():
        DATA_FILE_PATH.write_text("[]\n", encoding="utf-8")


def load_users() -> list[dict[str, Any]]:
    ensure_data_store()
    try:
        content = DATA_FILE_PATH.read_text(encoding="utf-8")
        parsed = json.loads(content)
    except (OSError, json.JSONDecodeError):
        return []

    if not isinstance(parsed, list):
        return []

    return [item for item in parsed if isinstance(item, dict)]


def save_users(users: list[dict[str, Any]]) -> None:
    ensure_data_store()
    safe_users = [item for item in users if isinstance(item, dict)]
    serialized = json.dumps(safe_users, indent=2, ensure_ascii=False)
    DATA_FILE_PATH.write_text(serialized, encoding="utf-8")
