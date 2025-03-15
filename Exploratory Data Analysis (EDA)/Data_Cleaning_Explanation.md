# 📊 Human Resources Dataset Analysis - Data Understanding & Cleaning

## **Step 1: Understanding the Data**
Before cleaning the dataset, I analyzed its structure and contents.

### **📌 Research Questions**
1. What factors contribute to higher employee performance ratings?
2. How does job satisfaction correlate with attrition rates?
3. What is the impact of education level on performance ratings?
4. How do training opportunities influence job satisfaction and performance?
5. What trends exist in employee work-life balance and their effect on retention?
6. Which departments have the highest and lowest satisfaction levels?
7. How do different performance rating levels correlate with promotion frequency?

### **📌 Dataset Information**
- **Source:** Human Resources Employee Dataset (`Employee.csv`)
- **Columns Included:** Employee ID, Age, Salary, Job Role, Department, Attrition, Performance Rating, Work-Life Balance, Education, etc.
- **Goal:** Analyze and clean the data for further insights and visualization.
- [Human Resources Dataset Analysis Project Metadata.pdf](https://github.com/user-attachments/files/19260500/Human.Resources.Dataset.Analysis.Project.Metadata.pdf)


---

## **Step 2: Data Cleaning Process**
To ensure data consistency and accuracy, I performed the following **data cleaning steps** using **Python (pandas)**:

### **✅ 1. Load the Dataset**
```python
import pandas as pd

# Load dataset
df = pd.read_csv(r"E:\Desktop\Datasets\Datasets\HR\Employee.csv")

# Show first few rows
print(df.head())
```

### ✅ 2. Check for Missing Values
```python
# Check missing values per column
print("Missing values per column:\n", df.isnull().sum())

# Show total missing values
print(f"Total missing values: {df.isnull().sum().sum()}")
```

### ✅ 3. Handle Missing Values
🔹 Numerical Columns:
Fill missing values using the median.
🔹 Categorical Columns:
Fill missing values using the most frequent value (mode).
```python
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
```
🔹 Drop Columns with More Than 50% Missing Values
```python
df.dropna(thresh=int(len(df) * 0.5), axis=1, inplace=True)
```

### ✅ 4. Convert Data Types
🔹Convert age to integer and salary to float.
🔹Convert Hire Date to datetime format.
```python
df['Age'] = df['Age'].astype(int)
df['Salary'] = df['Salary'].astype(float)
df['HireDate'] = pd.to_datetime(df['HireDate'], errors='coerce')
```

### ✅ 5. Standardize Text Columns
🔹Convert department names to title case.
🔹Remove extra spaces from names.
```python
df['Department'] = df['Department'].str.title()
df['FirstName'] = df['FirstName'].str.strip()
df['LastName'] = df['LastName'].str.strip()
```
### ✅ 6. Check for Duplicates
```python
# Check for duplicate rows
print(f"Duplicate rows before: {df.duplicated().sum()}")

# Remove duplicates
df.drop_duplicates(inplace=True)

print(f"Duplicate rows after: {df.duplicated().sum()}")
```

### ✅ 7. Combine First Name & Last Name
```python
df['Name'] = df['FirstName'] + " " + df['LastName']
df.drop(columns=['FirstName', 'LastName'], inplace=True)
```

### ✅ 8. Save the Cleaned Dataset
```python
df.to_csv(r"E:\Desktop\Datasets\Datasets\HR\Cleaned_Employee.csv", index=False)
print("✅ Data cleaning complete! Cleaned file saved as 'Cleaned_Employee.csv'")
```

### Result
![Output](https://github.com/user-attachments/assets/ce52fba0-2e1f-4469-ab52-b23a26a2e8aa)
