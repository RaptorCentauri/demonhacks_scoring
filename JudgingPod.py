class JudgingPod:
    def __init__(self, _pod_number):
        self.pod_number = _pod_number
        self.assigned_project_list = []
        self.pod_name = f"Pod-{_pod_number}"

    def set_assigned_project_list(self, _assigned_project_list):
        self.assigned_project_list = _assigned_project_list


    def get_assigned_project_list(self):
        return self.assigned_project_list

    def get_pod_number(self):
        return self.pod_number

    def get_pod_name(self):
        return self.pod_name

    def get_project_count(self):
        return len(self.assigned_project_list)

    def assign_project_to_pod(self, project):
        self.assigned_project_list.append(project)


