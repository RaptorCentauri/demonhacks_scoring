from Assigner import Assigner
from SubmissionManager import SubmissionManager
from JudgingPodManager import JudgingPodManager
from CSVManager import CSVManager
import os
from datetime import datetime

def create_output_folder():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = os.path.join("output", timestamp)
    os.makedirs(folder, exist_ok=True)
    return folder

# def write_pod_file(folder, pod_number, submissions):
#     filename = os.path.join(folder, f"pod_{pod_number}.txt")
#     with open(filename, "w") as f:
#         f.write(f"Submissions for Pod {pod_number}\n")
#         f.write("=====================\n")
#         for submission in submissions:
#             f.write(f"{submission}\n")

def write_pod_file(folder, pod_number, submissions):
    filename = os.path.join(folder, f"pod_{pod_number}.txt")
    with open(filename, "w") as f:
        f.write(f"Submissions for Pod {pod_number}\n")
        f.write("=====================\n")
        for submission in submissions:
            f.write(f"{submission}\n")
            for key, value in submission.get_custom_fields().items():
                f.write(f"  {key}: {value}\n")
            f.write("\n")

def write_master_file(folder, assigner, num_pods):
    filename = os.path.join(folder, "pod_all.txt")
    with open(filename, "w") as f:
        for i in range(num_pods):
            f.write(f"Submissions for Pod {i}\n")
            f.write("=====================\n")
            for submission in assigner.get_full_submissions_for_pod(i):
                f.write(f"{submission}\n")
            f.write("\n")

def execute(args):
    # for custom quesrions on devpost
    domain = "List All Of The Domain Names Your Team Has Registered With Domain.Com During This Hackathon."

    CUSTOM_COLUMNS = [domain]

    SUBMISSION_COLUMNS = ["Project Title", "Submission Url", "Table Number", "Highest Step Completed"] + CUSTOM_COLUMNS  # update as needed


    submission_data = CSVManager.extract_data(args.submissions, SUBMISSION_COLUMNS)

    submission_manager = SubmissionManager(submission_data, CUSTOM_COLUMNS)

    judging_pod_manager = JudgingPodManager(args.pods, args.reviews)

    assigner = Assigner(submission_manager, judging_pod_manager)

    assigner.assign()

    folder = create_output_folder()
    write_master_file(folder, assigner, args.pods)

    for i in range(args.pods):
        submissions = assigner.get_full_submissions_for_pod(i)
        write_pod_file(folder, i, submissions)

    print(f"Pod Assignments saved to {folder}")






