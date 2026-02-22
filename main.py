from Assigner import Assigner
from SubmissionManager import SubmissionManager
from JudgingPodManager import JudgingPoddManager
from ScoreManager import ScoreManager
from CSVManager import CSVManager


SUBMISSION_COLUMNS = ["Project Title", "Submission Url", "Highest Step Completed"]  # update as needed
submission_data = CSVManager.extract_data("submissions.csv", SUBMISSION_COLUMNS)


submission_manager = SubmissionManager(submission_data)

judging_pod_manager = JudgingPoddManager(8,3)

assigner = Assigner(submission_manager, judging_pod_manager)

# assigner.distribute_projects_to_pods()
assigner.assign()

assigner.validate_distribution()





print("Submissions for Pod 0")
assigner.print_full_submissions_for_pod(0)











#

#
# valid_submissions = submission_manager.get_real_submissions()
#
# judging_pod_manager = JudgingPoddManager(8,3)
# #
# judging_pod_manager.distribute_projects_to_pods(valid_submissions)
# #
# judging_pod_manager.get_submission_count_per_judging_pod()
#
# # judging_pod_manager.print_judging_assignments()
#
#
# score_manager = ScoreManager("Judging_Sheet.csv")
# # print(score_manager.get_raw_submissions())
# score_manager.get_scores()
#
# score_manager.get_scores_for_pod(3)