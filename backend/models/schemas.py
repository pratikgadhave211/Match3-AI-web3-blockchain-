from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class MatchUserRequest(BaseModel):
    name: str
    interests: list[str] = Field(default_factory=list)
    goals: list[str] | str = Field(default_factory=list)


class MatchCurrentUserRequest(BaseModel):
    wallet: str | None = None
    name: str | None = None


class UserResponse(BaseModel):
    wallet: str = ""
    name: str
    interests: list[str] = Field(default_factory=list)
    goals: list[str] = Field(default_factory=list)


class MatchItem(BaseModel):
    name: str = ""
    score: int | None = None
    reason: str | None = None


class MatchResponse(BaseModel):
    matches: list[MatchItem] = Field(default_factory=list)
    current_user: UserResponse | None = None
    raw: Any | None = None


class RefreshUsersResponse(BaseModel):
    success: bool
    message: str
    count: int


class IntroRequest(BaseModel):
    userA: UserResponse
    userB: UserResponse


class IntroResponse(BaseModel):
    message: str
