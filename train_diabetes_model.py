# train_diabetes_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Set random seed for reproducibility
np.random.seed(0)

# 2. Simulate dataset of 768 samples with 6 health features
num_samples = 768
data = pd.DataFrame({
    'Age': np.random.randint(21, 80, size=num_samples),
    'BMI': np.random.uniform(18, 45, size=num_samples),
    'Glucose': np.random.randint(70, 200, size=num_samples),
    'BloodPressure': np.random.randint(50, 120, size=num_samples),
    'Insulin': np.random.randint(15, 276, size=num_samples),
    'SkinThickness': np.random.randint(7, 99, size=num_samples),
})

# 3. Create a synthetic target: 1 (diabetic), 0 (not diabetic)
# Rule: diabetic if at least 2 of 3 risk factors are true
data['Outcome'] = (
    (data['Glucose'] > 130).astype(int) +
    (data['BMI'] > 30).astype(int) +
    (data['Age'] > 45).astype(int)
) > 1

data['Outcome'] = data['Outcome'].astype(int)

# 4. Define features and label
X = data[['Age', 'BMI', 'Glucose', 'BloodPressure', 'Insulin', 'SkinThickness']]
y = data['Outcome']

# 5. Split into train/test (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 7. Export model to .pkl file
joblib.dump(model, "diabetes_model.pkl")

# 8. Notify user
print("✅ Model training complete!")
print("📦 'diabetes_model.pkl' has been saved in your current directory.")
