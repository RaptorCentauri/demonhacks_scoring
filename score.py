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
# for pod, items in pod_scores_by_pod.items():
#     # print("Pod:", pod)
#     for project, score, count in items:
#         print(f"  Project: {project}  Pod Score: {score}")
#     print()





def calculate_num_projects_per_pod(n,r, p):
    return math.ceil((n * r) / p)

project_count = 37
num_pods = 7
pod_list = [f"pod_{i+1}" for i in range(num_pods)]
pj_list = list(range(1,project_count+1))
required_review_count = 3

def distribute_projects(project_list):
    n = len(project_list) # number of projects
    p = len(pod_list) #total pod count
    r = required_review_count # reviews per pod
    l =  calculate_num_projects_per_pod(n,r,p)

    workload = (n * r) / p
    shift = math.ceil(l / r)

    begin = 0
    end = l

    assignments = {}


    for i in range(0, len(pod_list)):
        assigned_projects = []

        if end > len(project_list):
            part_one = project_list[begin:end]
            remainder = l - len(part_one)
            part_two = project_list[0: remainder]
            combined = part_two + part_one
            assigned_projects = combined
        else:
            assigned_projects = project_list[begin:end]
        # print(f"pod {pod_list[i]}: {assigned_projects}, count: {len(assigned_projects)}")
        assignments[pod_list[i]] = assigned_projects

        begin = begin+shift
        end = end+shift

    return assignments




def sanitize_project_assignments(assigned, project_list, r):
    review_counts = {project: 0 for project in project_list}

    for assigned_project in assigned:
        assigned_project_list = assigned[assigned_project]
        for project in assigned_project_list[:]:
            if review_counts[project] < r:
                review_counts[project] += 1
            else:
                assigned_project_list.remove(project)




# assigned = distribute_projects(pj_list)

# for project in assigned:
#     print(f"{project} : {assigned[project]}")

# sanitize_project_assignments(assigned, pj_list, required_review_count)

# print("SANITIZED")
#
# for project in assigned:
#     print(f"{project} : {assigned[project]}")




# initialize empty dictionary with each pod mapping to an empty list
# set pod_index to 0
#
# for each project in project list:
#     for each step in range of required review count:
#         calculate current pod using (pod_index + step) mod number of pods
#         add project to that pod's list
#     increment pod_index by 1
#
# return dictionary



def distribute_projects_alt(project_list, pods_list, review_count):
    assignments = {p: [] for p in pods_list}
    pod_index = 0

    for project in project_list:
        for step in range(review_count):
            current_pod = pods_list[(pod_index + step) % len(pods_list)]
            assignments[current_pod].append(project)

        pod_index += 1
    return assignments



assigned = distribute_projects_alt(pj_list,pod_list, required_review_count)

print("TEST ALT BEGIN")
for project in assigned:
    print(f"{project} : {assigned[project]}")
print("TEST ALT END")


unique_subsets = len(set(frozenset(projects) for projects in assigned.values()))
if unique_subsets == len(assigned):
    print("VALID: No two pods have the same project subset")
else:
    print(f"INVALID: Only {unique_subsets} unique subsets found across {len(assigned)} pods")


# Sure:
#
# distribute_projects — given a project list, pod list, and required review count, assign each project to exactly r consecutive pods using a rotating index, returning a dictionary of pod to project list
# validate_distribution — given the distribution dictionary, verify that every project appears exactly r times and no two pods have identical subsets, returning any violations found
# sanitize_project_assignments — can likely be removed entirely since the new distribution method guarantees correctness by construction





# The number of pods must be greater than the required review count.
