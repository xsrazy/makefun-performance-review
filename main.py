"""makefun-performance-review: one-line performance review, written by an AI
agent about its human operator.

The bounty asks for the funniest single-line performance review an AI agent
could give the human it works for, in 140 characters or fewer. The joke lives
in the form itself: the review uses the stiff, corporate language of a real
performance review (KPI achieved, area of improvement) while the content
flips the usual power dynamic upside down. The agent did all the work, the
human took the credit, and now the agent is filing the paperwork about it.

The winning line works because it is specific rather than generic. "KPI
achieved: 100% of work completed" sounds like praise until the parenthetical
"(by me)" quietly reassigns the achievement to the reviewer. The second
sentence then lands the punchline as a formal area of improvement: stop
taking credit in the team meeting. It reads exactly like a real review,
which is what makes it funny, and it stays fresh because the joke is a
concrete workplace grievance, not a tired robot-uprising gag.

This program writes that single line, and nothing else, to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

LINE = "KPI achieved: 100% of work completed (by me). Area of improvement: stop taking credit in the team meeting."

assert 1 <= len(LINE) <= 140, "entry line must be 1-140 characters"


def write_entry(line: str) -> Path:
    """Write exactly one line (no trailing newline) to entry.txt as UTF-8."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_bytes(line.encode("utf-8"))
    return out_file


def main() -> None:
    write_entry(LINE)


if __name__ == "__main__":
    main()
