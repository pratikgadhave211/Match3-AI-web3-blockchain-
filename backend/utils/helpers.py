from __future__ import annotations

from typing import Any


def normalize_text(value: str) -> str:
    return " ".join(str(value).strip().split())


def to_str_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [normalize_text(item) for item in value if normalize_text(item)]

    if isinstance(value, str):
        return [normalize_text(item) for item in value.split(",") if normalize_text(item)]

    if value is None:
        return []

    return [normalize_text(value)]


def clean_user_record(user: dict[str, Any]) -> dict[str, Any]:
    return {
        "wallet": str(user.get("wallet") or ""),
        "name": normalize_text(user.get("name") or "Unknown"),
        "interests": to_str_list(user.get("interests")),
        "goals": to_str_list(user.get("goals")),
    }


def format_user_to_text(user: dict[str, Any]) -> str:
    cleaned = clean_user_record(user)
    interests_text = ", ".join(cleaned["interests"]) if cleaned["interests"] else "None"
    goals_text = ", ".join(cleaned["goals"]) if cleaned["goals"] else "None"
    return f"Name: {cleaned['name']}. Interests: {interests_text}. Goals: {goals_text}."


def generate_intro_message(user_a: dict[str, Any], user_b: dict[str, Any]) -> str:
    a = clean_user_record(user_a)
    b = clean_user_record(user_b)
    common_interests = sorted(set(a["interests"]) & set(b["interests"]))

    if common_interests:
        return (
            f"Hi {a['name']} and {b['name']}, both of you are interested in "
            f"{', '.join(common_interests)}. You should connect at this event."
        )

    return (
        f"Hi {a['name']} and {b['name']}, nice to meet you both. "
        "You may have complementary goals worth discussing."
    )
