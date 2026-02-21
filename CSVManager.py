import pandas as pandas

class CSVManager:
    @staticmethod
    def extract_data(csv_file, columns):
        return pandas.read_csv(csv_file, usecols=columns)