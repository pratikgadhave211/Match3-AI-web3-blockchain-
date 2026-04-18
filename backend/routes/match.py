from __future__ import annotations

from fastapi import APIRouter, HTTPException

from backend.models.schemas import MatchCurrentUserRequest, MatchItem, MatchResponse, MatchUserRequest, UserResponse
from backend.services.rag_service import resolve_current_user, run_match
from backend.utils.helpers import clean_user_record

router = APIRouter(tags=["match"])


@router.post("/match-user", response_model=MatchResponse)
def match_user(payload: MatchUserRequest) -> MatchResponse:
    new_user = clean_user_record(
        {
            "name": payload.name,
            "interests": payload.interests,
            "goals": payload.goals,
        }
    )

    try:
        matches, raw = run_match(new_user)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Matching failed: {exc}") from exc

    return MatchResponse(
        matches=[MatchItem(**item) for item in matches],
        current_user=UserResponse(**new_user),
        raw=raw,
    )


@router.post("/match-current-user", response_model=MatchResponse)
def match_current_user(payload: MatchCurrentUserRequest) -> MatchResponse:
    try:
        current_user = resolve_current_user(wallet=payload.wallet, name=payload.name)
        matches, raw = run_match(current_user)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Matching failed: {exc}") from exc

    return MatchResponse(
        matches=[MatchItem(**item) for item in matches],
        current_user=UserResponse(**current_user),
        raw=raw,
    )
