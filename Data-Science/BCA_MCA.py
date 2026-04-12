# ------------------------------
# BCA + MCA Analysis
# ------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load Data
data = pd.read_excel(r"C:\Users\admin\Desktop\Dummy Data.xlsx",
                     sheet_name="DS",
                     header=1)

# Select BCA and MCA
df = data[data["program"].isin(["BCA","MCA"])]

# Data Cleaning
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# ------------------------
# Basic Statistics
# ------------------------
total_students = len(df)
average_score = df["Marks"].mean()
highest_score = df["Marks"].max()
lowest_score = df["Marks"].min()

print("BCA + MCA Analysis")
print("Marks Students:", total_students)
print("Average Score:", average_score)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)


# ------------------------
# Students Performance Analysis
# ------------------------
# Pass / Fail
pass_students = df[df["Marks"] >= 10]
fail_students = df[df["Marks"] < 10]
absent_students = df[df["Marks"].isna()]


print("Pass:", len(pass_students))
print("Fail:", len(fail_students))
print("Absent:", len(absent_students))

# pass rate
pass_students = (df["Marks"] >= 10).sum()
pass_rate = (pass_students / total_students) * 100
print("Pass rate:", pass_rate,"%")


# students levels
strong_students = df[df["Marks"] >= 16]
average_students = df[(df["Marks"] >= 10) & (df["Marks"] < 16)]
weak_students = df[df["Marks"] < 10]

# count students
strong_count = len(strong_students)
average_count = len(average_students)
weak_count = len(weak_students)

print("Strong students is :", strong_count)
print("Average students is :", average_count)
print("Weak students is :", weak_count)

# percentages
strong_percent = (strong_count / total_students) * 100
average_percent = (average_count / total_students) * 100
weak_percent = (weak_count / total_students) * 100

print("\nPerformance Distribution")
print("Strong:", strong_percent, "%")
print("Average:", average_percent, "%")
print("Weak:", weak_percent, "%")

# # ------------------------
# # Ranking
# # ------------------------

# # top students 
top_students = df.sort_values(by="Marks", ascending=False).head(5)
# print(top_students)
top_students.to_excel(r"C:\Users\admin\Desktop\DS_results\TOP_S_BCA_MCA__in_DS.xlsx")

# # lowest students
low_students = df.sort_values(by="Marks").head(5)
# print(low_students)
low_students.to_excel(r"C:\Users\admin\Desktop\DS_results\LOW__S_BCA_MCA__in_DS.xlsx")

# Chart
plt.hist(df["Marks"])
plt.title("BCA + MCA Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.savefig(r"C:\Users\admin\Desktop\DS_results\DS.png")
plt.show()