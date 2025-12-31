
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(current_dir, '..', '..', 'Datasets', 'HR', 'Employee.csv')

# Load dataset
df = pd.read_csv(dataset_path)

# Set up the plot size
plt.figure(figsize=(18, 15))

# 1. Scatter plot: Age vs Tenure (YearsAtCompany)
plt.subplot(5, 3, 1)
sns.scatterplot(data=df, x='Age', y='YearsAtCompany')
plt.title('Age vs Tenure (YearsAtCompany)')

# 2. Box plot: DistanceFromHome vs Attrition
plt.subplot(5, 3, 2)
sns.boxplot(data=df, x='Attrition', y='DistanceFromHome (KM)')
plt.title('DistanceFromHome vs Attrition')

# 3. Box plot: Salary vs Attrition
plt.subplot(5, 3, 3)
sns.boxplot(data=df, x='Attrition', y='Salary')
plt.title('Salary vs Attrition')

# 4. Count plot: BusinessTravel vs Attrition (Effect of frequent travel on retention)
plt.subplot(5, 3, 4)
sns.countplot(data=df, x='BusinessTravel', hue='Attrition')
plt.title('BusinessTravel vs Attrition')

# 5. Scatter plot: YearsInMostRecentRole vs Promotion Opportunities (YearsSinceLastPromotion)
plt.subplot(5, 3, 5)
sns.scatterplot(data=df, x='YearsInMostRecentRole', y='YearsSinceLastPromotion')
plt.title('YearsInMostRecentRole vs Promotion Opportunities')

# 6. Bar plot: Age groups and Attrition
plt.subplot(5, 3, 6)
sns.countplot(data=df, x='Age', hue='Attrition')
plt.title('Age Groups and Attrition')

# 7. Count plot: Attrition by Gender
plt.subplot(5, 3, 7)
sns.countplot(data=df, x='Gender', hue='Attrition')
plt.title('Attrition by Gender')

# 8. Box plot: EducationField vs JobRole and Salary
plt.subplot(5, 3, 8)
sns.boxplot(data=df, x='EducationField', y='Salary', hue='JobRole')
plt.title('EducationField vs JobRole and Salary')

# 9. Scatter plot: YearsWithCurrManager vs Attrition
plt.subplot(5, 3, 9)
sns.scatterplot(data=df, x='YearsWithCurrManager', y='Attrition')
plt.title('YearsWithCurrManager vs Attrition')

# Tight layout to ensure plots are well spaced
plt.tight_layout()
plt.show()
