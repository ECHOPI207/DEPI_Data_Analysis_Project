import pandas as pd
import os

def main():
    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define relative paths
    dataset_path = os.path.join(current_dir, '..', 'data', 'raw', 'Employee.csv')
    output_path = os.path.join(current_dir, '..', 'data', 'processed', 'Cleaned_Employee.csv')

    # Load dataset
    df = pd.read_csv(dataset_path)

    # Fill missing numeric values with median
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Salary'] = df['Salary'].fillna(df['Salary'].median())

    # Fill missing categorical values with most frequent value (mode)
    df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

    # Drop columns with more than 50% missing values
    df.dropna(thresh=int(len(df) * 0.5), axis=1, inplace=True)

    # Convert data types
    df['Age'] = df['Age'].astype(int)
    df['Salary'] = df['Salary'].astype(float)
    df['HireDate'] = pd.to_datetime(df['HireDate'], errors='coerce')

    # Standardize text columns
    df['Department'] = df['Department'].str.title()
    df['FirstName'] = df['FirstName'].str.strip()
    df['LastName'] = df['LastName'].str.strip()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Combine FirstName and LastName into a new column called 'Name'
    df['Name'] = df['FirstName'] + " " + df['LastName']

    # Drop 'FirstName' and 'LastName' if not needed
    df.drop(columns=['FirstName', 'LastName'], inplace=True)

    # Save cleaned data to CSV file
    df.to_csv(output_path, index=False)

    print(f"✅ Data cleaning complete! Cleaned file saved as '{output_path}'")

if __name__ == "__main__":
    main()
