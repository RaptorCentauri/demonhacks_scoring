class PodScore:
    def __init__(self, _pod_number):
        self.pod_number = _pod_number
        self.scores = {}
        self.top_scores = []

    def add_judge_score(self, submission_id, judge_score):
        if submission_id not in self.scores:
            self.scores[submission_id] = {"judge_scores": []}

        self.scores[submission_id]["judge_scores"].append(judge_score)

    def get_score_data(self, submission_id):
        return self.scores[submission_id]

    def get_avg_score(self, submission_id):
        return self.scores[submission_id]["average"]

    def extract_top_scores(self, threshold):
        for submission_id, score in self.scores.items():
            if score["average"] > threshold:
                score_tuple = (submission_id, score["average"])
                self.top_scores.append(score_tuple)

    def calculate_average_scores(self):
        for submission_id, scores in self.scores.items():
            avg_score = self.calculate_submission_average(scores["judge_scores"])
            self.scores[submission_id]["average"] = avg_score

    def calculate_submission_average(self, score_list):
        return round(sum(score_list) / len(score_list), 2)

    def get_top_scores(self):
        return self.top_scores

