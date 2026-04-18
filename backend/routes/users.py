from __future__ import annotations

from fastapi import APIRouter, HTTPException

from backend.models.schemas import RefreshUsersResponse, UserResponse
from backend.services.data_service import load_users, save_users
from backend.services.web3_service import fetch_all_users_from_chain

router = APIRouter(tags=["users"])


@router.get("/users", response_model=list[UserResponse])
def get_users() -> list[UserResponse]:
    users = load_users()
    return [UserResponse(**user) for user in users]


@router.post("/refresh-users", response_model=RefreshUsersResponse)
def refresh_users() -> RefreshUsersResponse:
    try:
        users = fetch_all_users_from_chain()
        save_users(users)
        return RefreshUsersResponse(
            success=True,
            message="Blockchain users fetched and cached in users.json",
            count=len(users),
        )
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Refresh failed: {exc}") from exc
