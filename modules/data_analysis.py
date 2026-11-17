
import pandas as pd

# Step 1: Load the crop dataset
df = pd.read_csv("dataset/Crop_recommendation.csv")

# Step 2: Display first five records
print("\n===== FIRST FIVE RECORDS =====")
print(df.head())

# Step 3: Display dataset dimensions
print("\n===== DATASET SIZE =====")
print(df.shape)

# Step 4: Display column names
print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

# Step 5: Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Step 6: Check duplicate records
print("\n===== DUPLICATE RECORDS =====")
print(df.duplicated().sum())

# Step 7: Display crop categories
print("\n===== AVAILABLE CROPS =====")
print(df["label"].value_counts())

# Step 8: Display statistical information
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

print("\nDataset analysis completed successfully!")
