from Submission import Submission

class SubmissionManager:
    def __init__(self, _raw_data):
        self.raw_submissions = _raw_data
        self.valid_submissions = []
        self.real_submissions = []

        self.filter_valid_submissions()
        self.populate_real_submissions()

    def filter_valid_submissions(self):
        for index, row in self.raw_submissions.iterrows():
            if row["Highest Step Completed"] == "Submit":
                self.valid_submissions.append(row)

    def populate_real_submissions(self):
        for index, row in enumerate(self.valid_submissions):
            submission = Submission(int(row["Table Number"]), row["Project Title"], row["Submission Url"])
            self.real_submissions.append(submission)

    def get_raw_submissions(self):
        return self.raw_submissions

    def get_valid_submissions(self):
        return self.valid_submissions

    def get_real_submissions(self):
        return self.real_submissions

    def get_submission(self, submission_id):
        for submission in self.real_submissions:
            if submission.get_id() == submission_id:
                return submission

    def set_pods_for_submission(self, submission_id, pod_numbers):
        for submission in self.real_submissions:
            if submission.get_id() == submission_id:
                for pod_number in pod_numbers:
                    submission.assign_pod(pod_number)
                break