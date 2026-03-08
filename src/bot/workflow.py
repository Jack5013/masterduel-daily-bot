from __future__ import annotations

from .game_io import GameIO
from .vision import Vision


class DailyWorkflow:
    def __init__(self, config: dict) -> None:
        self.config = config
        self.io = GameIO(config)
        self.vision = Vision(config)

    def run(self) -> None:
        self.io.log("workflow_start", self.config)
        self.io.focus_game_window()
        self.io.log("workflow_end", {"status": "scaffold_only"})
