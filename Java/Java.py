# Java Course Exam Results Analysis
#  -------------------------------
#  Import Libraries
#  -------------------------------
import pandas as pd 
import matplotlib.pyplot as plt 

#  -------------------------------
#  Load Data 
#  -------------------------------

data = pd.read_excel(r"C:\Users\admin\Desktop\Dummy Data.xlsx", sheet_name="Java")
# print (data)
# print (data.info())

# -------------------------------------------
# Data cleaning
# -------------------------------------------
# print ("is there any null in data ? \n",data.isnull().sum())
# print ("is there any duplication in data = ",data.duplicated().sum())

# handle missing values
data = data.fillna("Unknown")
# print (data)

# Convert Sessional 1st marks Total20 column to numreic 
data["Sessional 1st marks Total20"] = pd.to_numeric(data["Sessional 1st marks Total20"],errors="coerce")
# print (data)

print ("-"*30)
# -------------------------------------------
# Basic Statistics
# -------------------------------------------


total_students = data["Sessional 1st marks Total20"].count()
highest_score = data["Sessional 1st marks Total20"].max()
average_score = data["Sessional 1st marks Total20"].mean()
lowest_score = data["Sessional 1st marks Total20"].min()

print ("Total Number Of Studnets is:",total_students)
print ("Average Score is:",average_score)
print ("Highest Score is:",highest_score)
print ("Lowest Score is:",lowest_score)


# -------------------------------------------
# Students Performance Analysis
# -------------------------------------------

print ("\n Students Pass / Fail")
print ("Students have Pass exam:", (data["Sessional 1st marks Total20"] >= 10).sum())
print ("Students have Fail exam:", (data["Sessional 1st marks Total20"] < 10).sum())

# # pass rate
pass_students =  (data["Sessional 1st marks Total20"] >= 10).sum()
pass_rate = (pass_students/total_students) * 100
print ("pass rate of Java exam is:",pass_rate,"%")

# ----------------------------------------------------------------------

# students levels
strong_students = data[data["Sessional 1st marks Total20"] >=16]
average_students= data[(data["Sessional 1st marks Total20"]>=10)&(data["Sessional 1st marks Total20"]<16)]
weak_students   = data[data["Sessional 1st marks Total20"]<10]

# count students
strong_count = len(strong_students)
average_count = len(average_students)
weak_count = len(weak_students)

print ("count of strong students is:",strong_count)
print ("count of average students is:",average_count)
print ("count of weak students is:",weak_count)

# percentages
strong_percent = (strong_count / total_students) * 100
average_percent = (average_count / total_students) * 100
weak_percent = (weak_count / total_students) * 100

print("\nPerformance Distribution")
print("Strong percant is:",strong_percent,"%")
print("Average percent is:",average_percent,"%")
print("Weak percent is:",weak_percent,"%")

# -------------------------------------------
# Ranking
# -------------------------------------------
# top students 
top_students = data.sort_values( by="Sessional 1st marks Total20",ascending = False).head(5)
# top_students.to_excel(r"C:\Users\admin\Desktop\Java_results\TOP_Students_Java.xlsx")

# low students
low_students = data.sort_values(by="Sessional 1st marks Total20").head(5)
# low_students.to_excel(r"C:\Users\admin\Desktop\Java_results\LOW_Students_Java.xlsx")

# ------------------------
# Visualization
# ------------------------
plt.hist(data["Sessional 1st marks Total20"],bins=5)
plt.title("Sessional-1 Java Exam Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number Of Students")

plt.savefig(r"C:\Users\admin\Desktop\Java_results\java.png")
plt.show()