import pandas as pd

df = pd.read_csv("student_performance_real.csv", sep=";")

print(df.head())
print(df.shape)
print(df.describe())