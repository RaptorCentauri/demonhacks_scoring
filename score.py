import math

import pandas as pd
from collections import namedtuple
from pprint import pprint

NEEDED = [
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


df = pd.read_csv(
    "Judging_Sheet.csv",
    usecols=NEEDED,          # only load these headers
)



def getJudgeScore(row):
    creativity_score = row["Creativity"]
    complexity = row["Technical complexity"]
    readability_score = row["Code readability"]
    problem_score = row["Uniqueness of problem identified"]
    solution_score = row["Uniqueness of solution"]
    closeness_score = row["Closeness of solution to problem"]
    polish_score = row["Polish and Presentation"]
    documentation_score = row["Documentation/Readme"]
    usefulness_score = row["Usefulness"]

    raw_scores = [creativity_score,complexity,readability_score,problem_score,solution_score,closeness_score,polish_score,documentation_score,usefulness_score]

    return sum(raw_scores)


def getPodScoreForProject(judge_rows, pod_number, project_number):
    pod_score = 0
    count = 0
    for jr in judge_rows:
        if jr.pod == pod_number and jr.project == project_number:
            pod_score += jr.score
            count += 1


JudgeRow = namedtuple("JudgeRow", ["judge", "pod", "project", "score"])



judge_rows = []

for index, row in df.iterrows():
    judge = row["Judge Name"]
    pod_num = row["Pod Number"]
    proj_num = row["Project Number"]
    judge_score = getJudgeScore(row)

    row_named = JudgeRow(judge, pod_num, proj_num, judge_score)
    judge_rows.append(row_named)



seen = set((jr.pod, jr.project) for jr in judge_rows)

for pod, project in seen:
    getPodScoreForProject(judge_rows, pod, project)



pod_project_totals = {}  # pod -> project -> {"score": X, "count": N}

for jr in judge_rows:
    pod = jr.pod
    project = jr.project

    if pod not in pod_project_totals:
        pod_project_totals[pod] = {}

    if project not in pod_project_totals[pod]:
        pod_project_totals[pod][project] = {"score": 0.0, "count": 0}

    pod_project_totals[pod][project]["score"] += jr.score
    pod_project_totals[pod][project]["count"] += 1


# Convert to: pod -> list of (project, total_score, rows_contributed)
pod_scores_by_pod = {}
for pod, projects in pod_project_totals.items():
    pod_scores_by_pod[pod] = [
        (project, data["score"], data["count"])
        for project, data in projects.items()
    ]



# print it
for pod, items in pod_scores_by_pod.items():
    print("Pod:", pod)
    for project, score, count in items:
        print(f"  Project: {project}  Pod Score: {score}")
    print()



