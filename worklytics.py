import pandas as pd          # to work with data
import numpy as np           # to create random numbers
import matplotlib.pyplot as plt  # to draw graphs
import seaborn as sns        # to draw better graphs

# Step 2: Create some fake employee data
# This is just for learning. In real life, you use Excel or CSV files
data = {
    'Name': ['Emp_1', 'Emp_2', 'Emp_3', 'Emp_4', 'Emp_5',
         'Emp_6', 'Emp_7', 'Emp_8', 'Emp_9', 'Emp_10'],                                           
    'Age': [25, 30, 28, 35, 40, 22, 45, 38, 27, 33],          
    'Department': ['HR', 'Tech', 'Sales', 'Tech', 'HR', 
                'Marketing', 'Sales', 'Tech', 'HR', 'Sales'],
    'TasksCompleted': [20, 35, 30, 40, 25, 18, 33, 42, 28, 37],
    'HoursWorked': [150, 160, 140, 170, 130, 145, 155, 165, 135, 150],
    'Salary': [40000, 60000, 50000, 70000, 45000, 42000, 55000, 68000, 46000, 52000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 
            'Male', 'Female', 'Male', 'Male', 'Female']
}

# Turn it into a table
df = pd.DataFrame(data)

# Step 3: Show first few rows of the data
print("First 5 rows of data:")
print(df.head())

# Step 4: Draw some charts

# Chart 1: How many tasks employees completed
plt.figure(figsize=(7, 4))
sns.barplot(x='Name', y='TasksCompleted', data=df)
plt.title("Tasks Completed by Employees")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 2: Compare salary between departments
plt.figure(figsize=(7, 4))
sns.boxplot(x='Department', y='Salary', data=df)
plt.title("Salary in Each Department")
plt.tight_layout()
plt.show()

# Chart 3: Hours worked vs Tasks completed
plt.figure(figsize=(6, 4))
sns.scatterplot(x='HoursWorked', y='TasksCompleted', hue='Gender', data=df)
plt.title("Hours Worked vs Tasks")
plt.tight_layout()
plt.show()

# Chart 4: Average tasks completed by department
plt.figure(figsize=(7, 4))
avg_tasks = df.groupby('Department')['TasksCompleted'].mean().reset_index()
sns.barplot(x='Department', y='TasksCompleted', data=avg_tasks)
plt.title("Average Tasks per Department")
plt.tight_layout()
plt.show()
