import pandas as pd

def load_data(path ="C:/Users/dell/PycharmProjects/student_grades_project/data/student_data.csv" ):
    return pd.read_csv(path)