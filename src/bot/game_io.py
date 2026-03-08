from __future__ import annotations

from datetime import datetime


class GameIO:
    def __init__(self, config: dict) -> None:
        self.config = config

    def focus_game_window(self) -> None:
        self.log("focus_window", {"title": self.config.get("window_title")})

    def log(self, event: str, payload: dict) -> None:
        ts = datetime.utcnow().isoformat(timespec="seconds") + "Z"
        print(f"[{ts}] {event}: {payload}")
