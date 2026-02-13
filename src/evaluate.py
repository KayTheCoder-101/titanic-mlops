import pandas as pd
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Paths
features_path = "features/features.csv"
predictions_path = "results/predictions.csv"
metrics_path = "results/metrics.txt"

# Ensure results directory exists
os.makedirs("results", exist_ok=True)

# Load true labels
df = pd.read_csv(features_path)
y_true = df["Survived"]

# Load predictions
pred_df = pd.read_csv(predictions_path)
y_pred = pred_df["Prediction"]

# Calculate metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Save metrics to file
with open(metrics_path, "w") as f:
    f.write(f"Accuracy: {accuracy:.4f}\n")
    f.write(f"Precision: {precision:.4f}\n")
    f.write(f"Recall: {recall:.4f}\n")
    f.write(f"F1 Score: {f1:.4f}\n")

print("Evaluation completed and metrics saved successfully!")
