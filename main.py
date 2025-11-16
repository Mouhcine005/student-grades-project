from src.load_data import load_data
from src.clean_data import clean_data
from src.transform_data import add_average_grade

df = clean_data(load_data())
df = add_average_grade(df)

df.to_csv("data/student_data_cleaned.csv", index=False)