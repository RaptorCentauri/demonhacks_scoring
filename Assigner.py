
class Assigner():
    def __init__(self, submission_manager, judging_pod_manager):
        self.submission_manager = submission_manager
        self.judging_pod_manager = judging_pod_manager

    def get_full_submissions_for_pod(self, pod_number):
        submission_ids = self.judging_pod_manager.get_submissions_for_pod(pod_number)
        return [self.submission_manager.get_submission(sid) for sid in submission_ids]

    def print_full_submissions_for_pod(self, pod_number):
        for submission in self.get_full_submissions_for_pod(pod_number):
            print(submission)

    def assign(self):
        submission_ids = [s.get_id() for s in self.submission_manager.get_real_submissions()]
        pod_numbers = self.judging_pod_manager.get_pod_numbers()
        review_count = self.judging_pod_manager.get_required_review_count()

        sub_to_pods = {}
        pod_to_subs = {}

        for i, submission_id in enumerate(submission_ids):
            assigned_pods = [pod_numbers[(i + step) % len(pod_numbers)] for step in range(review_count)]
            sub_to_pods[submission_id] = assigned_pods

            for pod_number in assigned_pods:
                if pod_number not in pod_to_subs:
                    pod_to_subs[pod_number] = []
                pod_to_subs[pod_number].append(submission_id)

        for submission_id, assigned_pods in sub_to_pods.items():
            self.submission_manager.set_pods_for_submission(submission_id, assigned_pods)

        for pod_number, assigned_submissions in pod_to_subs.items():
            self.judging_pod_manager.set_submissions_for_pod(pod_number, assigned_submissions)


    def validate_distribution(self):
        pod_numbers = self.judging_pod_manager.get_pod_numbers()
        subsets = [frozenset(self.judging_pod_manager.get_submissions_for_pod(p)) for p in pod_numbers]
        unique_subsets = len(set(subsets))

        if unique_subsets == len(pod_numbers):
            print("VALID: No two pods have the same project subset")
        else:
            print(f"INVALID: Only {unique_subsets} unique subsets found across {len(pod_numbers)} pods")
