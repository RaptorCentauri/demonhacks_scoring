from collections import namedtuple
from PodScore import PodScore
JudgeRow = namedtuple("JudgeRow", ["judge", "pod", "project", "score"])

class ScoreManager:
    def __init__(self, _raw_scores, _num_pods, _threshold):
        self.top_five = []
        self.raw_scores = _raw_scores
        self.judge_rows = []
        self.pod_scores = {}
        self.top_scores = []
        self.threshold = _threshold

        self.create_PodScores(_num_pods)
        self.collect_judge_totals()
        self.populate_pod_scores()
        self.collect_top_scores()
        self.simplify_top_scores()
        self.extract_top_five()


    def get_raw_submissions(self):
        return self.raw_scores

    def calculate_judge_total(self, row):
        creativity_score = row["Creativity"]
        complexity = row["Technical complexity"]
        readability_score = row["Code readability"]
        problem_score = row["Uniqueness of problem identified"]
        solution_score = row["Uniqueness of solution"]
        closeness_score = row["Closeness of solution to problem"]
        polish_score = row["Polish and Presentation"]
        documentation_score = row["Documentation/Readme"]
        usefulness_score = row["Usefulness"]

        raw_scores = [creativity_score, complexity, readability_score, problem_score, solution_score, closeness_score,
                      polish_score, documentation_score, usefulness_score]

        return sum(raw_scores)


    def collect_judge_totals(self):
        for index, row in self.raw_scores.iterrows():
            judge = row["Judge Name"]
            pod_num = row["Pod Number"]
            proj_num = row["Project Number"]
            judge_score = self.calculate_judge_total(row)

            row_named = JudgeRow(judge, pod_num, proj_num, judge_score)
            self.judge_rows.append(row_named)


    def create_PodScores(self, count):
        for i in range(count):
            self.pod_scores[i] = PodScore(i)

    def populate_pod_scores(self):
        for row in self.judge_rows:
            self.pod_scores[row.pod].add_judge_score(row.project, row.score)

    def collect_top_scores(self):
        for pod in self.pod_scores:
            self.pod_scores[pod].calculate_average_scores()
            self.pod_scores[pod].extract_top_scores(self.threshold)
            top_pod_scores = self.pod_scores[pod].get_top_scores()
            self.top_scores.extend(top_pod_scores)

    def simplify_top_scores(self):
        simplified = {}
        for submission_id, score in self.top_scores:
            if submission_id not in simplified:
                simplified[submission_id] = 0
            simplified[submission_id] += score
        self.top_scores = list(simplified.items())

    def extract_top_five(self):
        sorted_scores = sorted(self.top_scores, key=lambda x: x[1], reverse=True)
        if len(sorted_scores) <= 5:
            self.top_five = sorted_scores
            return
        cutoff_score = sorted_scores[4][1]
        self.top_five = [s for s in sorted_scores if s[1] >= cutoff_score]

    def get_top_five(self):
        return self.top_five