from SubmissionManager import SubmissionManager
from JudgingPodManager import JudgingPoddManager
from ScoreManager import ScoreManager

submission_manager = SubmissionManager("submissions.csv")
submission_manager.validate()

# print(submission_manager.get_real_submissions())

#
valid_submissions = submission_manager.get_real_submissions()

judging_pod_manager = JudgingPoddManager(8,3)
#
judging_pod_manager.distribute_projects_to_pods(valid_submissions)
#
judging_pod_manager.get_submission_count_per_judging_pod()
#
# judging_pod_manager.validate_submission_distribution()
#
#
judging_pod_manager.print_judging_assignments()

score_manager = ScoreManager("Judging_Sheet.csv")
# print(score_manager.get_raw_submissions())
score_manager.get_scores()

# score_manager.get_scores_for_pod(3)