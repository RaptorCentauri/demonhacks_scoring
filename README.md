# DemonHacks Scoring System

A CLI tool for managing project assignments and score tallying at DemonHacks, a 24-hour hackathon hosted by DePaul's Computer Science Society and Upsilon Pi Epsilon chapter.

## Setup

**Requirements:** Python 3.9+

Create and activate a virtual environment:

```
python3.9 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

The tool runs in two phases corresponding to the two stages of the hackathon.

### Phase 1 — Generate Pod Assignments

Run this after the submission window closes, using the CSV exported from Devpost.

```
python main.py phase1 --submissions submissions.csv --pods 8 --reviews 3
```

**Arguments:**
- `--submissions` — path to the Devpost submissions CSV
- `--pods` — number of judging pods
- `--reviews` — number of pods each project must be reviewed by

**Output:** A timestamped folder inside `output/` containing a master assignment file and one file per pod listing their assigned projects.

### Phase 2 — Tally Scores and Get Top 5

Run this after judging is complete, using both the submissions CSV and the judging sheet CSV.

```
python main.py phase2 --submissions submissions.csv --scores Judging_Sheet.csv --pods 8 --threshold 75
```

**Arguments:**
- `--submissions` — path to the Devpost submissions CSV
- `--scores` — path to the judging sheet CSV
- `--pods` — number of judging pods
- `--threshold` — minimum pod score (0–100) for a project to advance to the collective

**Output:** A timestamped folder inside `output/` containing a `top_five.txt` file with the finalists for judge deliberation.

## How Scoring Works

1. Each judge scores a project across all criteria — their scores are summed into a total.
2. Each pod averages the judge totals for each project it reviewed.
3. Projects with a pod average above the threshold advance to the collective.
4. Duplicate projects across pods are merged by summing their pod scores.
5. The top 5 are returned. Ties at the cutoff expand the list automatically.

Scores are intentionally not shown in the final output to avoid anchoring judge deliberation.

## Notes

- Phase 1 is deterministic — the same inputs will always produce the same pod assignments.
- Phase 2 can reconstruct phase 1 internally, so both CSVs are sufficient to run the full pipeline.
- Output folders are timestamped so previous runs are never overwritten.
