import pandas as pd
import os

# Paths
input_path = "data/raw/titanic.csv"
output_path = "data/processed/titanic_processed.csv"

# Create directory if not exists
os.makedirs("data/processed", exist_ok=True)

# Load data
df = pd.read_csv(input_path)

# Handle missing values
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Encode categorical variables
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

# Save processed data
df.to_csv(output_path, index=False)

print("Preprocessing completed successfully!")
