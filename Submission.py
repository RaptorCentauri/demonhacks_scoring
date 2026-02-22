class Submission:
    def __init__(self, _id, _name, _url):
        self.id = _id
        self.name = _name
        self.url = _url
        self.assigned_pods = []

    def __repr__(self):
        return f'(id: {self.id}, name: {self.name}, url: {self.url}), assigned_pods: {self.assigned_pods}'


    def __str__(self):
        return f'(id: {self.id}, name: {self.name}, url: {self.url})'

    def get_assigned_pods(self):
        return self.assigned_pods

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def assign_pod(self, pod):
        self.assigned_pods.append(pod)
