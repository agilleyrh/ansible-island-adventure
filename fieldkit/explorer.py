"""Run one SQL query against a fresh in-memory copy of the explorers' log."""

import sqlite3
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit('Usage: python3 fieldkit/explorer.py "SELECT ..."')
with sqlite3.connect(":memory:") as database:
    database.executescript((Path(__file__).parent / "data/explorers.sql").read_text())
    for row in database.execute(sys.argv[1]):
        print(*row, sep=" | ")
