from __future__ import annotations

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:4173",
        "http://127.0.0.1:4173",
    ],
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
