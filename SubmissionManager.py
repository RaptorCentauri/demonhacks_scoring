
from CSVManager import CSVManager
from Submission import Submission

SUBMISSION_COLUMNS = ["Project Title", "Submission Url", "Highest Step Completed"]  # update as needed

class SubmissionManager:
    def __init__(self, _filename):
        self.raw_submissions = CSVManager.extract_data(_filename, SUBMISSION_COLUMNS)
        self.valid_submissions = []
        self.real_submissions = []

    def get_raw_submissions(self):
        return self.raw_submissions

    def validate(self):
        for index, row in self.raw_submissions.iterrows():
            if row["Highest Step Completed"] == "Submit":
                submission_tuple = (row["Project Title"], row["Submission Url"])
                self.valid_submissions.append(submission_tuple)
                submission = Submission(index, row["Project Title"], row["Submission Url"] )
                self.real_submissions.append(submission)

    def get_valid_submissions(self):
        return self.valid_submissions

    def get_real_submissions(self):
        return self.real_submissions