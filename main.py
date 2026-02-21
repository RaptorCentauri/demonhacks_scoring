from SubmissionManager import SubmissionManager
from JudgingPodManager import JudgingPoddManager

submission_manager = SubmissionManager("submissions.csv")
submission_manager.validate()

valid_submissions = submission_manager.get_valid_submissions()

print(len(valid_submissions))


judging_pod_manager = JudgingPoddManager(8,3)

judging_pod_manager.distribute_projects_to_pods(valid_submissions)

judging_pod_manager.get_submission_count_per_judging_pod()

judging_pod_manager.validate_submission_distribution()


judging_pod_manager.print_judging_assignments()