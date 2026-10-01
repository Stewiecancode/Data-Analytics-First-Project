import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_real.csv", sep=";")

# Understand the dataset
print(df.head())
print("Rows and columns:", df.shape)
print("Missing values:", df.isna().sum().sum())

# Calculate basic results
print("Average final grade:", round(df["G3"].mean(), 2))
print("Average absences:", round(df["absences"].mean(), 2))

# Explore absences and final grades
df.plot.scatter(x="absences", y="G3", alpha=0.5)
plt.title("School absences and final grades")
plt.xlabel("Number of absences")
plt.ylabel("Final grade (out of 20)")
plt.tight_layout()
plt.show()

average_grades = df.groupby("studytime")["G3"].mean()
print(average_grades)

average_grades.plot.bar()
plt.title("Average final grade by weekly study time")
plt.xlabel("Study-time category")
plt.ylabel("Average grade (out of 20)")
plt.tight_layout()
plt.show()