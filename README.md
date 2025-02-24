# DEPI Data Analysis Project

# Human Resources Dataset Analysis Project

<p align="center">
  <img src="https://github.com/user-attachments/assets/ce724b50-7c5f-4248-b13c-32769d0fbad4" alt="Image">
</p>

**Prepared by:**
1. Abdelrahman Mohamed Ibrahim  
2. Ahmed Abdelazeem Ahmed  
3. Eslam Fadl Sayed  
4. Mohamed Mostafa Mohamed  
5. Yousef Mohamed Hussein  

---

## Data Analysis Project Documentation

**Project Deadline:** 4/11/2025

---

### 1. Project Introduction

#### 1.1 Overview
This data analysis project explores employee performance and satisfaction levels and their correlation with other factors such as education level, work-life balance, and training opportunities. By leveraging data analytics, we aim to derive actionable insights that can help improve workforce management and performance evaluation.

#### 1.2 Objectives
- **Analyze employee performance ratings** and their influencing factors.
- **Identify trends in job satisfaction and attrition.**
- **Correlate education levels with employee performance.**
- **Provide actionable insights for HR decision-making** using SQL, Python, and Power BI.

#### 1.3 Scope
- Focus solely on the data provided by the CSV files.
- Cover data extraction, cleaning, integration, and exploratory analysis.
- Provide recommendations based on the analysis for improved employee management practices.
- Limit the scope to internal HR performance analytics without integrating external data sources.

---

### 2. Project Plan

#### 2.1 Timeline (Gantt Chart)
![image](https://github.com/user-attachments/assets/78e12c15-8d26-480b-ac4b-37b1b7bdd4ce)


#### 2.2 Milestones
- **Milestone 1:** Data Cleaning & Preprocessing Completed.
- **Milestone 2:** EDA & Visualizations Developed.
- **Milestone 3:** Power BI Dashboard & KPI Insights Finalized.
- **Milestone 4:** Documentation & Final Report Ready.

#### 2.3 Deliverables
- Cleaned Dataset (Excel → SQL/Python Processed Data).
- SQL Queries & Python Scripts.
- Power BI Dashboard with Interactive Reports.
- Business Insights & KPI Reports.
- Final Documentation & Presentation.

#### 2.4 Resources
- **Team Members:** Data analysts.
- **Tools & Technologies:** Excel, Python, SQL, GitHub, Power BI, and data visualization libraries (Matplotlib, Seaborn).
- **Hardware:** Workstations capable of handling data processing tasks.

---

### 3. Task Assignment & Roles

| Task Name                                       | Start Date  | End Date    | Description                                                                                                                                      | Assigned to                                         |
|-------------------------------------------------|-------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **Project Planning & Management**               | 2/17/2025   | 2/24/2025   | Planning and defining the scope.                                                                                                                 | Abdelrahman Mohamed Ibrahim, Ahmed Abdelazeem Ahmed |
| **System Analysis & Design**                    | 2/17/2025   | 2/24/2025   | System and database structure design.                                                                                                            | Eslam Fadl Sayed, Mohamed Mostafa Mohamed            |
| **Data Import & Cleaning (Excel to SQL/Python/Power BI)** | 2/25/2025   | 3/3/2025    | 1. Load Excel files into Power BI & Python.  <br>2. Convert Excel sheets into SQL tables.  <br>3. Clean missing values.  <br>4. Ensure data consistency. | Yousef Mohamed Hussein, Abdelrahman Mohamed Ibrahim |
| **Exploratory Data Analysis (EDA) (SQL/Python)** | 3/4/2025    | 3/10/2025   | 1. Run SQL queries to analyze trends.  <br>2. Use Python Pandas for summary statistics.  <br>3. Identify outliers using boxplots in Power BI.  | Ahmed Abdelazeem Ahmed, Eslam Fadl Sayed             |
| **Data Transformation & Aggregation (SQL/Python)** | 3/11/2025  | 3/17/2025   | 1. Use SQL to merge data from multiple Excel sheets.  <br>2. Aggregate employee performance metrics (DAX).  <br>3. Standardize data types and create calculated fields. | Mohamed Mostafa Mohamed, Yousef Mohamed Hussein      |
| **Power BI Data Modeling & Relationships**      | 3/18/2025   | 3/24/2025   | 1. Establish relationships between tables.  <br>2. Optimize performance using Power Query Transformations & DAX.                                 | Abdelrahman Mohamed Ibrahim, Ahmed Abdelazeem Ahmed |
| **Power BI Dashboard Creation & Custom Reports**| 3/25/2025   | 3/31/2025   | 1. Create interactive dashboards for: <br>&nbsp;&nbsp;&nbsp;&nbsp;- Employee performance trends. <br>&nbsp;&nbsp;&nbsp;&nbsp;- Satisfaction levels per department. <br>&nbsp;&nbsp;&nbsp;&nbsp;- Attrition rate analysis. <br>2. Add filters & slicers for user interaction. <br>3. Generate customized Power BI reports.  | Eslam Fadl Sayed, Mohamed Mostafa Mohamed            |
| **Business Insights & KPI Analysis (Power BI)** | 4/1/2025    | 4/7/2025    | 1. Identify high vs. low-performing employees. <br>2. Compare education level vs. job performance. <br>3. Create HR-friendly visual reports to track company trends. | Yousef Mohamed Hussein, Ahmed Abdelazeem Ahmed       |
| **Final Report & Presentation (Power BI & Documentation)** | 4/8/2025 | 4/11/2025   | 1. Export Power BI dashboard as PDF/PPT. <br>2. Document findings in a structured report. <br>3. Present key insights to stakeholders.           | Abdelrahman Mohamed Ibrahim, Mohamed Mostafa Mohamed |

---

### 4. Stakeholder Analysis

#### 4.1 Key Stakeholders
- **Project Sponsor:** Executive leadership responsible for strategic decision-making.
- **Human Resources Department:** Primary beneficiary of the analysis to enhance employee management.
- **Employees:** Indirect stakeholders who benefit from improved HR practices.

#### 4.2 Stakeholder Needs
- **Project Sponsor:** Clear, actionable insights and robust, reproducible analysis.
- **Human Resources:** Detailed analyses linking performance with education and satisfaction, leading to informed policy decisions.
- **Employees:** Transparent performance assessments and potential opportunities for career growth.

---

### 5. ER Diagram

![image](https://github.com/user-attachments/assets/6f500c93-dc76-4bf1-a030-70e4c81887ff)

#### 5.2 Entities & Relationships Covered
- **Employee:** Linked to Department, Education Level, Performance, and Projects.
- **Performance Ratings:** Linked to Employee, Satisfaction, and Rating Levels.
- **Department & Projects:** Managing employee assignments.
- **Satisfaction & Ratings:** Tracking employee performance.
- **Many-to-Many relationships:** Employee-Project.

---

### 6. Research Questions
- What factors contribute to higher employee performance ratings?
- How does job satisfaction correlate with attrition rates?
- What is the impact of education level on performance ratings?
- How do training opportunities influence job satisfaction and performance?
- What trends exist in employee work-life balance and their effect on retention?
- Which departments have the highest and lowest satisfaction levels?
- How do different performance rating levels correlate with promotion frequency?

