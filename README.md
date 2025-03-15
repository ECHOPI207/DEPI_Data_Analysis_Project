# DEPI Data Analysis Project

# Human Resources Dataset Analysis Project

<p align="center">
  <img src="https://github.com/user-attachments/assets/af28c623-f335-4318-92e8-624faba0067a" alt="Image">
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
# 📊 Data Analysis Project Plan

## **Week 1: Build Data Model, Data Cleaning and Preprocessing**
| Task Name                | Start Date  | End Date  | Description                                                              | Assigned to                                      | Tools            | Deliverables                                  |
|--------------------------|------------|----------|--------------------------------------------------------------------------|------------------------------------------------|-----------------|----------------------------------------------|
| **Project Planning & Management** | 2/17/2025  | 2/24/2025 | Planning and defining the scope.                                          | Abdelrahman Mohamed Ibrahim, Ahmed Abdelazeem Ahmed | -               | Project scope document                      |
| **Data Import & Cleaning**        | 2/25/2025  | 3/3/2025  | Load Excel files into Python, preprocess missing values, ensure consistency. | Yousef Mohamed Hussein, Abdelrahman Mohamed Ibrahim | -               | Cleaned dataset, Data preprocessing notebook |

## **Week 2: Analysis Questions Phase**
| Task Name                          | Start Date  | End Date  | Description                                                                                        | Assigned to                              | Tools                        | Deliverables                                      |
|-------------------------------------|------------|----------|--------------------------------------------------------------------------------------------------|----------------------------------------|-----------------------------|-------------------------------------------------|
| **Determine Data Analysis Questions** | 3/4/2025   | 3/10/2025 | Identify analysis questions relevant for decision-making.                                         | Ahmed Abdelazeem Ahmed, Eslam Fadl Sayed | Python (pandas, Matplotlib)  | A set of analysis questions that can be answered. |
| **Exploratory Data Analysis (EDA)**   | 3/4/2025   | 3/10/2025 | Analyze data trends, run descriptive statistics, identify outliers.                              | -                                      | Python (pandas, Matplotlib)  | Summary statistics and visual insights.           |

## **Week 3: Forecasting Questions Phase**
| Task Name                           | Start Date  | End Date  | Description                                                  | Assigned to                                   | Tools                                    | Deliverables                                  |
|--------------------------------------|------------|----------|--------------------------------------------------------------|-----------------------------------------------|-----------------------------------------|----------------------------------------------|
| **Determine Forecasting Questions**  | 3/11/2025  | 3/17/2025 | Identify key forecasting questions and trends in the dataset. | Mohamed Mostafa Mohamed, Yousef Mohamed Hussein | Python (scikit-learn, pandas, Tableau)  | A set of forecasting insights based on data trends. |
| **Data Transformation & Aggregation** | 3/11/2025  | 3/17/2025 | Merge and aggregate data to prepare for predictive modeling. | Mohamed Mostafa Mohamed, Yousef Mohamed Hussein | Python (pandas)                         | Standardized and aggregated dataset.         |

## **Week 4: Visualization Dashboard and Final Presentation**
| Task Name                           | Start Date  | End Date  | Description                                                                 | Assigned to                                   | Tools                                    | Deliverables                                      |
|--------------------------------------|------------|----------|-----------------------------------------------------------------------------|-----------------------------------------------|-----------------------------------------|-------------------------------------------------|
| **Data Modeling & Relationships**    | 3/18/2025  | 3/24/2025 | Establish relationships between tables, optimize performance.                | Abdelrahman Mohamed Ibrahim, Ahmed Abdelazeem Ahmed | Python (pandas, Matplotlib)            | Optimized data model                           |
| **Dashboard Creation & Reports**     | 3/25/2025  | 3/31/2025 | Create interactive dashboards, add filters & slicers.                        | Eslam Fadl Sayed, Mohamed Mostafa Mohamed    | Python (pandas, Matplotlib), Tableau  | Interactive dashboards and reports.            |
| **Business Insights & KPI Analysis** | 4/1/2025   | 4/7/2025  | Identify high vs. low-performing employees, analyze job performance.         | Yousef Mohamed Hussein, Ahmed Abdelazeem Ahmed | Python (pandas, Matplotlib), Tableau  | Business insights & KPI reports               |
| **Final Report & Presentation**      | 4/8/2025   | 4/11/2025 | Prepare a report summarizing project work, including data analysis.          | Abdelrahman Mohamed Ibrahim, Mohamed Mostafa Mohamed | Python (pandas, Matplotlib), Tableau  | Final report and presentation.                |

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

