from __future__ import annotations

from typing import Any

from backend.main import app as backend_app


class StripApiPrefixApp:
    """ASGI wrapper to run backend routes behind Vercel /api path."""

    async def __call__(self, scope: dict[str, Any], receive: Any, send: Any) -> None:
        if scope.get("type") in {"http", "websocket"}:
            path = str(scope.get("path") or "")
            if path.startswith("/api"):
                updated_scope = dict(scope)
                updated_path = path[4:] or "/"
                updated_scope["path"] = updated_path
                scope = updated_scope

        await backend_app(scope, receive, send)


app = StripApiPrefixApp()
