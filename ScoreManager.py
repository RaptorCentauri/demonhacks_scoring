from CSVManager import CSVManager
from collections import namedtuple

SCORE_COLUMNS = [
"Judge Name",
"Pod Number",
"Project Name",
"Project Number",
"Creativity",
"Technical complexity",
"Code readability",
"Uniqueness of problem identified",
"Uniqueness of solution",
"Closeness of solution to problem",
"Polish and Presentation",
"Documentation/Readme",
"Usefulness"
]


JudgeRow = namedtuple("JudgeRow", ["judge", "pod", "project", "score"])

class ScoreManager:
    def __init__(self, _filename):
        self.raw_scores = CSVManager.extract_data(_filename, SCORE_COLUMNS)
        self.judge_rows = []

    def get_raw_submissions(self):
        return self.raw_scores


    def get_judge_score(self, row):
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



    def get_scores(self):
        for index, row in self.raw_scores.iterrows():
            judge = row["Judge Name"]
            pod_num = row["Pod Number"]
            proj_num = row["Project Number"]
            judge_score = self.get_judge_score(row)

            row_named = JudgeRow(judge, pod_num, proj_num, judge_score)
            self.judge_rows.append(row_named)




    def get_scores_for_pod(self, pod_num):
        for row in self.judge_rows:
            if row.pod == pod_num:
                print(row)





