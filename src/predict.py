import pandas as pd
import os
import joblib

# Paths
features_path = "features/features.csv"
model_path = "models/model.pkl"
output_path = "results/predictions.csv"

# Ensure results directory exists
os.makedirs("results", exist_ok=True)

# Load features
df = pd.read_csv(features_path)

# Separate features (drop target)
X = df.drop("Survived", axis=1)

# Load trained model
model = joblib.load(model_path)

# Generate predictions
predictions = model.predict(X)

# Save predictions
output_df = pd.DataFrame({"Prediction": predictions})
output_df.to_csv(output_path, index=False)

print("Predictions generated and saved successfully!")
