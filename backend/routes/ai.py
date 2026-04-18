from __future__ import annotations

from fastapi import APIRouter

from backend.models.schemas import IntroRequest, IntroResponse
from backend.utils.helpers import generate_intro_message

router = APIRouter(tags=["ai"])


@router.post("/generate-intro", response_model=IntroResponse)
def generate_intro(payload: IntroRequest) -> IntroResponse:
    message = generate_intro_message(payload.userA.model_dump(), payload.userB.model_dump())
    return IntroResponse(message=message)
