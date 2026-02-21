class JudgingPod:
    def __init__(self, _pod_name):
        self.pod_name = _pod_name
        self.assigned_project_list = []


    def set_assigned_project_list(self, _assigned_project_list):
        self.assigned_project_list = _assigned_project_list


    def get_assigned_project_list(self):
        return self.assigned_project_list


