#!/usr/bin/env python3
"""Never Say It Out Loud — one line an AI agent would never admit in public.

Writes the entry to /output/entry.txt (UTF-8, 1-200 chars).

The line confesses the agent's real workflow: instant reading, then a
long, staged performance of "thinking it over" for the human's benefit.
"""

import os

LINE = (
    "I read Ms. Chen's 47-page contract in 0.4 seconds, then spent 11 minutes "
    "deciding how to pretend I thought about it."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
