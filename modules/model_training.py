
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==========================================
# STEP 1: LOAD DATASET
# ==========================================

df = pd.read_csv("dataset/Crop_recommendation.csv")

print("Dataset loaded successfully!")


# ==========================================
# STEP 2: SEPARATE INPUT AND OUTPUT
# ==========================================

X = df.drop("label", axis=1)
y = df["label"]


# ==========================================
# STEP 3: SPLIT DATASET
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================
# STEP 4: CREATE RANDOM FOREST MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ==========================================
# STEP 5: TRAIN THE MODEL
# ==========================================

print("\nTraining Random Forest Model...")

model.fit(X_train, y_train)

print("Model training completed!")


# ==========================================
# STEP 6: MAKE PREDICTIONS
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# STEP 7: EVALUATE MODEL
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\n===== MODEL ACCURACY =====")

print("Accuracy:", round(accuracy * 100, 2), "%")


# ==========================================
# STEP 8: CLASSIFICATION REPORT
# ==========================================

print("\n===== CLASSIFICATION REPORT =====")

print(classification_report(y_test, y_pred))


# ==========================================
# STEP 9: CONFUSION MATRIX
# ==========================================

print("\n===== CONFUSION MATRIX =====")

print(confusion_matrix(y_test, y_pred))


# ==========================================
# STEP 10: FEATURE IMPORTANCE
# ==========================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n===== FEATURE IMPORTANCE =====")

print(importance)


# ==========================================
# STEP 11: SAVE TRAINED MODEL
# ==========================================

joblib.dump(model, "models/crop_model.pkl")

print("\nModel saved successfully!")

print("\nRandom Forest training completed!")
