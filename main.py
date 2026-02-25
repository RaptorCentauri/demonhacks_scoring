import argparse
from phase_one import execute as execute_phase1
from phase_two import execute as execute_phase2

def run_phase1(args):
    execute_phase1(args)
    # phase 1 logic here
    # pass

def run_phase2(args):
    # phase 2 logic here
    execute_phase2(args)
    # pass

parser = argparse.ArgumentParser(description="DemonHacks Scoring System")
subparsers = parser.add_subparsers(dest="command")

# Phase 1
phase1_parser = subparsers.add_parser("phase1", help="Generate pod assignments")
phase1_parser.add_argument("--submissions", required=True, help="Path to submissions CSV")
phase1_parser.add_argument("--pods", type=int, required=True, help="Number of judging pods")
phase1_parser.add_argument("--reviews", type=int, required=True, help="Required reviews per project")

# Phase 2
phase2_parser = subparsers.add_parser("phase2", help="Calculate scores and top 5")
phase2_parser.add_argument("--submissions", required=True, help="Path to submissions CSV")
phase2_parser.add_argument("--scores", required=True, help="Path to judging sheet CSV")
phase2_parser.add_argument("--pods", type=int, required=True, help="Number of judging pods")
phase2_parser.add_argument("--threshold", type=float, required=True, help="Minimum pod score to advance")

args = parser.parse_args()

if args.command == "phase1":
    run_phase1(args)
elif args.command == "phase2":
    run_phase2(args)
else:
    parser.print_help()