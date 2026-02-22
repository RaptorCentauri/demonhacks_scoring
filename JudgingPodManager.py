from JudgingPod import JudgingPod

class JudgingPoddManager:
    def __init__(self, _num_pods, _required_review_count):
        self.pod_list = []
        self.required_review_counts = _required_review_count
        self.num_pods = _num_pods

        self.initialize_pods()

    def initialize_pods(self):
        for i in range(self.num_pods):
            pod = JudgingPod(i)
            self.pod_list.append(pod)


    def get_pod_list(self):
        return self.pod_list


    def set_required_review_count(self, _review_count):
        self.required_review_counts = _review_count

    def get_required_review_count(self):
        return self.required_review_counts

    def get_pod_numbers(self):
        return [pod.get_pod_number() for pod in self.pod_list]


    def print_judging_assignments(self):
        for pod in self.pod_list:
            print(f"{pod.get_pod_name()} : {pod.get_assigned_project_list()}")

    def get_submission_count_per_judging_pod(self):
        for pod in self.pod_list:
            print(f"{pod.get_pod_name()} : {pod.get_project_count()}")

    def set_submissions_for_pod(self, pod_number, submission_ids):
        for pod in self.pod_list:
            if pod.get_pod_number() == pod_number:
                for submission_id in submission_ids:
                    pod.assign_project_to_pod(submission_id)
                break

    def get_submissions_for_pod(self, pod_number):
            return self.pod_list[pod_number].get_assigned_project_list()