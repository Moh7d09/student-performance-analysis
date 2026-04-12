
# CAO Course Exam Results Analysis
# ------------------------
#  Import Libraries
# ------------------------
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------
#  Load Data
# ------------------------

data = pd.read_excel(r"C:\Users\admin\Desktop\Dummy Data.xlsx", sheet_name="CAO")

# ------------------------
#  Load Data
# ------------------------

# handle missing values
data = data.fillna("UnKnown")

# convert Total column to numeric
data["Total"] = pd.to_numeric(data["Total"], errors="coerce")

# ------------------------
# Basic Statistics
# ------------------------

total_students = data["Total"].count()
average_score = data["Total"].mean()
highest_score = data["Total"].max()
lowest_score = data["Total"].min()

print("Total number of students:", total_students)
print("Average score:", average_score)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)


# ------------------------
# Students Performance Analysis
# ------------------------
print("\nStudents Pass / Fail")

print("Pass:", (data["Total"] >= 10).sum())
print("Not Pass:", (data["Total"] < 10).sum())

# pass rate
pass_students = (data["Total"] >= 10).sum()
pass_rate = (pass_students / total_students) * 100

print("Pass rate:", pass_rate,"%")

# students levels
strong_students = data[data["Total"] >= 16]
average_students = data[(data["Total"] >= 10) & (data["Total"] < 16)]
weak_students = data[data["Total"] < 10]

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


# ------------------------
# Ranking
# ------------------------

# top students 
top_students = data.sort_values(by="Total", ascending=False).head(5)
# top_students.to_excel(r"C:\Users\admin\Desktop\TOP_S_CAO.xlsx")

# lowest students
low_students = data.sort_values(by="Total").head(10)
low_students.to_excel(r"C:\Users\admin\Desktop\LOW_S_CAO.xlsx")

# # rank column
# data["Rank"] = data["Total"].rank(ascending=False)

# ------------------------
# Visualization
# ------------------------
plt.hist(data["Total"], bins=5)
plt.title("Sessional-1 Exam Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")

# plt.savefig(r"C:\Users\admin\Desktop\score_distribution.png")
plt.show()