"""
## Week 2: Analysis Questions Phase
Determine Data Analysis Questions: The goal is to identify key analysis questions that can provide valuable insights
for decision-makers in the organization.
These questions should focus on exploring relationships between different variables in the dataset
(e.g., How do age and salary relate to job satisfaction?).

Step 1: Exploring Relationships: We will explore possible relationships between numerical and categorical variables.
- Understand potential relationships between numerical and categorical variables (e.g., Age vs. Salary).
- Check for correlation between YearsAtCompany and Attrition.
- Analyze if JobRole or Gender affects Salary.

Other questions may focus on specific factors like MaritalStatus, OverTime, or Education and their impact on key metrics like Attrition or JobSatisfaction.

Step 2: Data Exploration and Initial Analysis:
- Calculate descriptive statistics (Mean, Median, Std Dev) for numerical columns.
- Visualize relationships using scatter plots, boxplots, and correlation heatmaps.

Step 3: Formulating Analysis Questions:
- Based on the data exploration, we will formulate a set of analytical questions to be answered.

Let's start by exploring the data and identifying potential analysis questions. I will calculate basic statistics and
explore the relationships visually.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define relative path to the cleaned dataset
cleaned_data_path = os.path.join(current_dir, '..', 'data', 'processed', 'Cleaned_Employee.csv')

# Load dataset
df = pd.read_csv(cleaned_data_path)

# Show first few rows
print(df.columns)

# Generate summary statistics for numerical columns
summary_stats = df.describe()

# Plotting some basic visualizations to explore relationships between variables
plt.figure(figsize=(15, 10))

# Scatter plot: Age vs Salary
plt.subplot(2, 2, 1)
sns.scatterplot(data=df, x='Age', y='Salary')
plt.title('Age vs Salary')

# Box plot: Salary by Gender
plt.subplot(2, 2, 2)
sns.boxplot(data=df, x='Gender', y='Salary')
plt.title('Salary by Gender')

# Box plot: Attrition by JobRole
plt.subplot(2, 2, 3)
sns.boxplot(data=df, x='Attrition', y='Salary')
plt.title('Attrition by Salary')

# Correlation heatmap: Numeric features correlation
plt.subplot(2, 2, 4)

# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')

plt.tight_layout()
plt.show()

# Displaying the summary statistics
print(summary_stats)

"""
Summary of Data Exploration
Based on the visualizations and statistics:
- Age vs. Salary: No clear linear relationship, but clusters exist, suggesting Age isn't the sole factor for Salary.
- Salary by Gender: Noticeable differences in salary distribution. Deep analysis is needed to check for a gender pay gap.
- Attrition by Salary: There is a difference in salary distribution between those who left (Attrition=Yes) and those who stayed. Salary likely impacts retention.
- Education vs. Salary: Correlation exists between Education Level and Salary, requiring further analysis.
- Correlation Heatmap: Relationships observed between YearsAtCompany, Salary, and YearsWithCurrManager.

Formulating Analysis Questions:
Based on the data, we propose the following analytical questions:

1. What is the relationship between employee age and tenure at the company?
2. Is there a correlation between the distance from home (DistanceFromHome) and employee attrition?
3. How does salary impact employee attrition rates?
4. What is the effect of frequent business travel (BusinessTravel) on employee retention?
5. How does the number of years in the most recent role (YearsInMostRecentRole) relate to promotion opportunities?
6. Which age groups are most likely to leave the company?
"""