# Exploratory Data Analysis (EDA)
# ==============================================================
# This script performs EDA to answer key business questions and prepares the data for further
# visualization in PowerBI and Tableau.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a visual style for the plots
sns.set_style("whitegrid")


def main():
    # Get the directory where the script is located
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define relative path to the dataset
    dataset_path = os.path.join(current_dir, '..', 'data', 'processed', 'Cleaned_Employee.csv')
    figures_dir = os.path.join(current_dir, '..', 'reports', 'figures')
    
    # Create figures directory if it doesn't exist
    os.makedirs(figures_dir, exist_ok=True)

    # Load the cleaned dataset
    df = pd.read_csv(dataset_path)

    # Display basic dataset information
    print("Dataset Info:")
    print(df.info())
    print("\nDataset Description:")
    print(df.describe())

    # 1. Distance from Home (KM) vs. Attrition
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Attrition", y="DistanceFromHome (KM)", data=df)
    plt.title("Distance from Home vs. Employee Attrition")
    plt.xlabel("Attrition")
    plt.ylabel("Distance from Home (KM)")
    plt.savefig(os.path.join(figures_dir, "Distance_from_Home_vs_Attrition.png"))
    plt.close()

    # 2. Salary Impact on Attrition
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Attrition", y="Salary", data=df)
    plt.title("Salary Impact on Attrition")
    plt.xlabel("Attrition")
    plt.ylabel("Salary")
    plt.savefig(os.path.join(figures_dir, "Salary_vs_Attrition.png"))
    plt.close()

    # 3. Effect of Business Travel on Employee Retention
    plt.figure(figsize=(8, 5))
    sns.countplot(x="BusinessTravel", hue="Attrition", data=df)
    plt.title("Effect of Business Travel on Employee Retention")
    plt.xlabel("Business Travel")
    plt.ylabel("Count")
    plt.savefig(os.path.join(figures_dir, "BusinessTravel_vs_Retention.png"))
    plt.close()

    # 4. Years in Most Recent Role vs. Promotion Opportunities
    # Here, we use 'YearsSinceLastPromotion' as a proxy for promotion frequency.
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="YearsSinceLastPromotion", y="YearsInMostRecentRole", data=df)
    plt.title("Years in Most Recent Role vs. Promotion Opportunities")
    plt.xlabel("Years Since Last Promotion")
    plt.ylabel("Years in Most Recent Role")
    plt.savefig(os.path.join(figures_dir, "YearsInMostRecentRole_vs_Promotion.png"))
    plt.close()

    # 5. Age Groups Most Likely to Leave
    plt.figure(figsize=(8, 5))
    # Plot histograms for employees who left vs. retained
    sns.histplot(df[df["Attrition"] == "Yes"]["Age"], bins=20, color="red",
                 label="Attrition", kde=True, stat="density", alpha=0.6)
    sns.histplot(df[df["Attrition"] == "No"]["Age"], bins=20, color="blue",
                 label="Retained", kde=True, stat="density", alpha=0.6)
    plt.title("Age Distribution by Attrition")
    plt.xlabel("Age")
    plt.ylabel("Density")
    plt.legend()
    plt.savefig(os.path.join(figures_dir, "Age_Distribution_by_Attrition.png"))
    plt.close()

    # 6. Gender and Attrition Rates
    plt.figure(figsize=(8, 5))
    sns.countplot(x="Gender", hue="Attrition", data=df)
    plt.title("Attrition Rates by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.savefig(os.path.join(figures_dir, "Gender_vs_Attrition.png"))
    plt.close()

    # 7. Education Field Influence on Job Roles and Salary
    plt.figure(figsize=(12, 5))
    sns.boxplot(x="EducationField", y="Salary", data=df)
    plt.title("Education Field vs. Salary")
    plt.xlabel("Education Field")
    plt.xticks(rotation=45)
    plt.ylabel("Salary")
    plt.savefig(os.path.join(figures_dir, "EducationField_vs_Salary.png"))
    plt.close()

    # 8. Years with Current Manager and Attrition
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Attrition", y="YearsWithCurrManager", data=df)
    plt.title("Years with Current Manager vs. Attrition")
    plt.xlabel("Attrition")
    plt.ylabel("Years with Current Manager")
    plt.savefig(os.path.join(figures_dir, "YearsWithCurrManager_vs_Attrition.png"))
    plt.close()

    # 9. Stock Option Levels and Employee Retention
    plt.figure(figsize=(8, 5))
    sns.countplot(x="StockOptionLevel", hue="Attrition", data=df)
    plt.title("Stock Option Levels vs. Employee Retention")
    plt.xlabel("Stock Option Level")
    plt.ylabel("Count")
    plt.savefig(os.path.join(figures_dir, "StockOptionLevel_vs_Retention.png"))
    plt.close()

    # 10. Relationship Between Education and Years in Current Job Role
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Education", y="YearsInMostRecentRole", data=df)
    plt.title("Education Level vs. Years in Most Recent Role")
    plt.xlabel("Education Level")
    plt.ylabel("Years in Most Recent Role")
    plt.savefig(os.path.join(figures_dir, "Education_vs_YearsInMostRecentRole.png"))
    plt.close()

    # 11. Marital Status and Attrition
    plt.figure(figsize=(8, 5))
    sns.countplot(x="MaritalStatus", hue="Attrition", data=df)
    plt.title("Marital Status vs. Attrition")
    plt.xlabel("Marital Status")
    plt.ylabel("Count")
    plt.savefig(os.path.join(figures_dir, "MaritalStatus_vs_Attrition.png"))
    plt.close()

    # 12. Promotion Delay and its Effect on Attrition
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Attrition", y="YearsSinceLastPromotion", data=df)
    plt.title("Delay in Promotion vs. Attrition")
    plt.xlabel("Attrition")
    plt.ylabel("Years Since Last Promotion")
    plt.savefig(os.path.join(figures_dir, "PromotionDelay_vs_Attrition.png"))
    plt.close()


if __name__ == "__main__":
    main()
