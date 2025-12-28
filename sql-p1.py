# Install packages if you haven't already:
# pip install sqlalchemy mysql-connector-python pandas matplotlib seaborn

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Connect to MySQL ---
engine = create_engine("mysql+mysqlconnector://root:ANUpama%401216@localhost/sql_project1")
query = """
SELECT s.name, s.department, sub.subject_name, m.score, m.semester
FROM Marks m
JOIN Students s ON m.student_id = s.student_id
JOIN Subjects sub ON m.subject_id = sub.subject_id
"""
sample = pd.read_sql(query, engine)

# --- 2. Bar Plot: Average Marks per Subject ---
avg_subject = sample.groupby('subject_name')['score'].mean().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x='subject_name', y='score', data=avg_subject)
plt.title('Average Marks per Subject')
plt.ylabel('Average Score')
plt.xlabel('Subject')
plt.tight_layout()
plt.show()

# --- 3. Pie Chart: Student Distribution by Department ---
dept_count = sample[['name','department']].drop_duplicates().groupby('department').count()
plt.figure(figsize=(6,6))
plt.pie(dept_count['name'], labels=dept_count.index, autopct='%1.1f%%', startangle=140)
plt.title('Student Distribution by Department')
plt.show()

# --- 4. Scatter Plot: Scores vs Semester ---
plt.figure(figsize=(8,5))
sns.scatterplot(x='name', y='score', hue='department', marker = '*',data=sample, s=100)
plt.title('Scores vs Students at gLance')
plt.xlabel('Student Name')
plt.ylabel('Score')
plt.legend(title='Department')
plt.tight_layout()
plt.grid()
plt.show()

# --- 5. Line Plot: Semester-wise Average Score ---
semester_avg = sample.groupby('semester')['score'].mean().reset_index()
plt.figure(figsize=(6,4))
sns.lineplot(x='semester', y='score', data=semester_avg, marker='o')
plt.title('Semester-wise Average Score')
plt.xlabel('Semester')
plt.ylabel('Average Score')
plt.xticks(sorted(sample['semester'].unique()))
plt.tight_layout()
plt.show()

# --- 6. Heatmap: Subject Difficulty by Department ---
heatmap_data = sample.pivot_table(index='department', columns='subject_name', values='score', aggfunc='mean')
plt.figure(figsize=(10,6))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='YlGnBu')
plt.title('Subject Difficulty by Department (Average Score)')
plt.tight_layout()
plt.show()
# --- 7. Box Plot: Score Distribution by Department ---
plt.figure(figsize=(8,5))   
sns.boxplot(x='department', y='score', data=sample)
plt.title('Score Distribution by Department')   
plt.xlabel('Department')
plt.ylabel('Score') 
plt.tight_layout()
plt.show()  
