from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config import get_runtime_settings
from backend.routes.ai import router as ai_router
from backend.routes.match import router as match_router
from backend.routes.users import router as users_router

app = FastAPI(
    title="AI + Web3 Event Matchmaker",
    version="1.0.0",
    description="FastAPI backend for blockchain user refresh and local-cache RAG matching.",
)


def _get_allowed_origins() -> list[str]:
    static_origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:4173",
        "http://127.0.0.1:4173",
    ]

    configured = os.getenv("FRONTEND_ORIGIN", "").strip()
    if configured:
        static_origins.extend([origin.strip() for origin in configured.split(",") if origin.strip()])

    # Preserve order while removing duplicates.
    return list(dict.fromkeys(static_origins))

app.add_middleware(
    CORSMiddleware,
    allow_origins=_get_allowed_origins(),
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$|^https://([a-zA-Z0-9-]+\.)*vercel\.app$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(match_router)
app.include_router(ai_router)


@app.get("/")
def root() -> dict[str, object]:
    return {
        "status": "ok",
        "message": "Backend is live",
        "settings": get_runtime_settings(),
    }
