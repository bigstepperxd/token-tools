#!/usr/bin/env python3
"""
token_tracker.py
Reads tokens.json and prints a small report.
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("tokens.json")

def load_tokens():
    if not DATA_FILE.exists():
        DATA_FILE.write_text(json.dumps([
            {"symbol": "XPL", "notes": "Example presale token", "notes_url": ""},
            {"symbol": "BONK", "notes": "Community memecoin example", "notes_url": ""}
        ], indent=2))
    return json.loads(DATA_FILE.read_text())

def report(tokens):
    now = datetime.utcnow().isoformat() + "Z"
    print(f"token-tools report — {now}")
    print("-" * 40)
    for t in tokens:
        sym = t.get("symbol", "UNKNOWN")
        notes = t.get("notes", "")
        print(f"{sym:8} — {notes}")
    print("-" * 40)
    print(f"count: {len(tokens)}")

if __name__ == "__main__":
    tokens = load_tokens()
    report(tokens)
