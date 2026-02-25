# PHASE 1
#
# for custom quesrions on devpost
domain = "List All Of The Domain Names Your Team Has Registered With Domain.Com During This Hackathon."
schools = "List All Of The Universities Or Schools  That Your Team Members Currently Attend."
feedback = "Share Feedback About Any Of The Technology You Interacted With At This Hackathon. Make Sure You Mention What Tech You're Reviewing (E.G. Git Hub, De So, Etc.)."


CUSTOM_COLUMNS = [domain, schools, feedback]
# CUSTOM_COLUMNS = [schools]


SUBMISSION_COLUMNS = ["Project Title", "Submission Url", "Table Number", "Highest Step Completed"] + CUSTOM_COLUMNS  # update as needed


# PHASE 2


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

METADATA_COLUMNS = [
    "Judge Name",
    "Pod Number",
    "Project Name",
    "Project Number",
]

CRITERIA_COLUMNS = [
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

