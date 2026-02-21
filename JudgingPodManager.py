from JudgingPod import JudgingPod

class JudgingPoddManager:
    def __init__(self, _num_pods, _required_review_count):
        # self.pod_list = [f"pod_{i + 1}" for i in range(_num_pods)]
        self.pod_list = []

        self.required_review_counts = _required_review_count
        self.judging_assignments = {}
        self.num_pods = _num_pods

        self.initialize_pods()

    def initialize_pods(self):
        for i in range(self.num_pods):
            pod = JudgingPod(i)
            self.pod_list.append(pod)




    def set_required_review_count(self, _review_count):
        self.required_review_count = _review_count



    # def distribute_projects_to_pods(self, project_list):
    #     assignments = {p: [] for p in self.pod_list}
    #     pod_index = 0
    #
    #     for project in project_list:
    #         for step in range(self.required_review_counts):
    #             current_pod = self.pod_list[(pod_index + step) % len(self.pod_list)]
    #             assignments[current_pod].append(project)
    #
    #         pod_index += 1
    #
    #     self.judging_assignments = assignments


    def distribute_projects_to_pods(self, project_list):
        # assignments = {p: [] for p in self.pod_list}
        pod_index = 0

        for project in project_list:
            for step in range(self.required_review_counts):
                current_pod = self.pod_list[(pod_index + step) % len(self.pod_list)]
                print("NAME", current_pod.get_pod_name())
                current_pod.distribute_project(step)
                # assignments[current_pod].append(project)

            pod_index += 1

        self.judging_assignments = assignments



    def get_judging_assignments(self):
        return self.judging_assignments

    def print_judging_assignments(self):
        print("JUDGING ASSIGNMENTS")
        for pod in self.judging_assignments:
            print(f"{pod.get_pod_name()} : {pod.get_assigned_project_list()}")


    def get_submission_count_per_judging_pod(self):
        for pod in self.judging_assignments:
            print(f"{pod.get_pod_name()} : {pod.get_project_count()}")



    def validate_submission_distribution(self):
        #Validate unique distribution
        unique_subsets = len(set(frozenset(projects) for projects in self.judging_assignments.values()))
        if unique_subsets == len(self.judging_assignments):
            print("VALID: No two pods have the same project subset")
        else:
            print(f"INVALID: Only {unique_subsets} unique subsets found across {len(self.judging_assignments)} pods")



