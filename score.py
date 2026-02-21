import math

import pandas as pd
from collections import namedtuple

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

    # print("Pod: ", pod_number)
    # print("Project: ", project_number)
    # print("Pod Score: ", pod_score)
    # print("Rows Contributed:", count)
    # print("+++++++++++++++++++++++++")
    # print()




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

    # optional: sort highest score first
    # pod_scores_by_pod[pod].sort(key=lambda x: x[1], reverse=True)


# print it
for pod, items in pod_scores_by_pod.items():
    print("Pod:", pod)
    for project, score, count in items:
        print(f"  Project: {project}  Pod Score: {score}")
    print()





def calculate_num_projects_per_pod(n,r, p):
    return math.ceil((n * r) / p)


pod_list = ["A", "B", "C", "D", "E", "F"]
pj_list = list(range(1,60+1))

def distribute_projects(project_list):
    n = len(project_list) # number of projects
    p = len(pod_list) #total pod count
    r = 3 # reviews per pod
    l =  calculate_num_projects_per_pod(n,r,p)
    print("L= ", l)

    workload = (n * r) / p
    shift = math.ceil(l / r)



    begin = 0
    end = l

    print("Shift", shift)

    for i in range(0, len(pod_list)):
        if end > len(project_list):
            part_one = project_list[begin:end]
            remainder = l - len(part_one)
            part_two = project_list[0: remainder]
            combined = part_two + part_one
            print(f"pod {pod_list[i]}: {combined}, count: {len(combined)}")
        else:
            print(f"pod {pod_list[i]}: {project_list[begin:end]}, count: {len(project_list[begin:end])}")
        begin = begin+shift
        end = end+shift



        #handle wrap around




distribute_projects(pj_list)















