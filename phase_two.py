
from ScoreManager import ScoreManager
from CSVManager import CSVManager
from SubmissionManager import SubmissionManager
from config import SCORE_COLUMNS, CRITERIA_COLUMNS, METADATA_COLUMNS
import os
from datetime import datetime

def create_output_folder():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = os.path.join("output", timestamp)
    os.makedirs(folder, exist_ok=True)
    return folder


def write_top_five_file(folder, top_five, submission_manager):
    filename = os.path.join(folder, "finalists.txt")
    with open(filename, "w") as f:
        f.write(f"Top {len(top_five)} Finalists\n")
        f.write("=======================\n")
        for i in top_five:
            ID = i[0]
            submission = submission_manager.get_submission(ID)
            f.write(f"Project ID: {ID}\n")
            f.write(f"Project Name: {submission.get_name()}\n")
            f.write(f"Project URL: {submission.get_url()}\n")
            f.write("\n")


def execute(args):
    SUBMISSION_COLUMNS = ["Project Title", "Submission Url", "Table Number",
                          "Highest Step Completed"]  # update as needed
    submission_data = CSVManager.extract_data(args.submissions, SUBMISSION_COLUMNS)

    submission_manager = SubmissionManager(submission_data)


    score_data = CSVManager.extract_data(args.scores, SCORE_COLUMNS)

    score_manager = ScoreManager(score_data, args.pods, args.threshold, CRITERIA_COLUMNS, METADATA_COLUMNS )
    top_five = score_manager.get_top_five()

    folder = create_output_folder()
    write_top_five_file(folder, top_five, submission_manager)
    print(f"Top {len(top_five)} saved to {folder}")



    print("Top Five:")
    print("=======================")

    for i in top_five:
        ID = i[0]
        submission = submission_manager.get_submission(ID)

        print(f"Project ID: {i[0]}")
        print(f"Project Name: {submission.get_name()}")
        print(f"Project URL: {submission.get_url()}")
        print()