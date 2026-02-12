import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Paths
input_path = "features/features.csv"
model_path = "models/model.pkl"

# Ensure models directory exists
os.makedirs("models", exist_ok=True)

# Load feature data
df = pd.read_csv(input_path)

# Separate target and features
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize model
model = RandomForestClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, model_path)

print("Model training completed and saved successfully!")
