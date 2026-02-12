import pandas as pd
import os

# Paths
input_path = "data/processed/titanic_processed.csv"
output_path = "features/features.csv"

# Ensure directory exists
os.makedirs("features", exist_ok=True)

# Load processed data
df = pd.read_csv(input_path)

# ---------------------------
# Feature Engineering
# ---------------------------

# 1. Create FamilySize feature
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# 2. Extract Title from Name
df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.")

# Simplify titles
df["Title"] = df["Title"].replace(
    ["Lady", "Countess","Capt","Col","Don","Dr","Major","Rev","Sir","Jonkheer","Dona"],
    "Rare"
)
df["Title"] = df["Title"].replace(["Mlle","Ms"], "Miss")
df["Title"] = df["Title"].replace(["Mme"], "Mrs")

# Encode Title
df = pd.get_dummies(df, columns=["Title"], drop_first=True)

# Drop columns not needed for modeling
df = df.drop(columns=["Name", "Ticket", "Cabin"], errors="ignore")

# Save engineered features
df.to_csv(output_path, index=False)

print("Feature engineering completed successfully!")
