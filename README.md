# masterduel-daily-bot

Automation starter project for Yu-Gi-Oh! Master Duel daily task runs.

## Goal

Build a scriptable workflow that can:

1. Launch and focus the game window.
2. Navigate daily task screens.
3. Execute repeatable actions for daily progress.
4. Collect rewards.
5. Save logs and screenshots for verification.

## Project Status

Scaffold only. No live game automation is executed yet.

## Structure

- `src/main.py` - runner entrypoint
- `src/bot/workflow.py` - daily workflow pipeline
- `src/bot/game_io.py` - window/input/screen capture wrappers
- `src/bot/vision.py` - image matching and OCR helpers
- `config/config.example.json` - runtime config template

## Run

```bash
python -m src.main --dry-run
```

## Safety

- Start with dry-run mode.
- Add explicit delays and fail-safe interrupts.
- Keep all actions logged for replay/debug.
