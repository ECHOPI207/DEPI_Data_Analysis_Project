# Human Resources Dataset Analysis Project (DEPI)

This project explores employee performance, satisfaction levels, and their correlation with factors such as education, work-life balance, and training. By leveraging data analytics, we aim to derive actionable insights to improve workforce management.

## 👥 Team Members
- **Abdelrahman Mohamed Ibrahim**
- **Ahmed Abdelazeem Ahmed**
- **Eslam Fadl Sayed**
- **Mohamed Mostafa Mohamed**
- **Yousef Mohamed Hussein**

## 📊 Key Insights & Visualizations

Here are some of the key findings from our exploratory data analysis:

### 1. Salary Impact on Attrition
Analysis shows a significant difference in salary distribution between employees who left and those who stayed.
![Salary vs Attrition](00.%20Deliverables/03.%20Week%2003%20-%20EDA/0311.%20Salary_vs_Attrition.png)

### 2. Age Distribution & Attrition
Understanding which age groups are most likely to leave the company helps in targeted retention strategies.
![Age Distribution](00.%20Deliverables/03.%20Week%2003%20-%20EDA/033.%20Age_Distribution_by_Attrition.png)

### 3. Business Travel Effect
Does frequent travel lead to higher attrition? The data reveals interesting trends.
![Business Travel](00.%20Deliverables/03.%20Week%2003%20-%20EDA/034.%20BusinessTravel_vs_Retention.png)

### 4. Education Field vs. Salary
How education background influences compensation across different roles.
![Education Field vs Salary](00.%20Deliverables/03.%20Week%2003%20-%20EDA/037.%20EducationField_vs_Salary.png)

---

## 🎯 Objectives
1.  **Analyze Performance:** Investigate employee performance ratings and influencing factors.
2.  **Identify Trends:** Uncover patterns in job satisfaction and employee attrition.
3.  **Correlate Factors:** Study the relationship between education levels and performance.
4.  **Provide Insights:** Deliver actionable recommendations for HR decision-making using Python and Power BI.

## 📂 Project Structure & Timeline

The project is organized into weekly deliverables, simulating a real-world analytics project timeline:

### Week 1: Build Data Model, Data Cleaning and Preprocessing
- **Focus:** Data extraction, cleaning, and integration.
- **Key File:** `011. Data_Cleaning.py`
- **Output:** `Cleaned_Employee.csv`

### Week 2: Analysis Questions Phase
- **Focus:** Formulating key business questions and exploring relationships between variables.
- **Key Activities:** Identifying trends in Age vs. Salary, Attrition factors.

### Week 3: EDA & Forecasting Phase
- **Focus:** In-depth Exploratory Data Analysis (EDA) and preparing for forecasting.
- **Key File:** `031. Week 3 - EDA Phase.py`
- **Visualizations:** Attrition analysis, Salary distributions, Promotion delays.

### Week 4: Visualization Dashboard & Final Presentation
- **Focus:** Creating interactive dashboards and final reporting.
- **Deliverables:** Power BI Dashboard (`.pbix`), Final Project Report.

---

## 🛠 Prerequisites & Installation

Ensure you have Python installed. You can install the required libraries using:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

1.  **Data Cleaning:**
    Run the cleaning script to generate the processed dataset:
    ```bash
    python "00. Deliverables/01. Week 01 - Build Data Model, Data Cleaning and Preprocessing/011. Data_Cleaning.py"
    ```

2.  **Exploratory Data Analysis (EDA):**
    Run the EDA script to generate visualizations:
    ```bash
    python "00. Deliverables/03. Week 03 - EDA/031. Week 3 - EDA Phase.py"
    ```

## 🧰 Tools Used
- **Python:** Pandas, Matplotlib, Seaborn (Data Processing & Visualization)
- **Power BI:** Interactive Dashboarding
- **Excel:** Preliminary Data Inspection
