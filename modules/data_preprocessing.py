
import pandas as pd

from sklearn.model_selection import train_test_split

# STEP 1: Load dataset

df = pd.read_csv("dataset/Crop_recommendation.csv")

print("Dataset loaded successfully!")


# STEP 2: Separate input features (X)

X = df.drop("label", axis=1)


# STEP 3: Separate output label (y)

y = df["label"]


# STEP 4: Display input and output information

print("\nINPUT FEATURES:")
print(X.head())

print("\nOUTPUT LABELS:")
print(y.head())


# STEP 5: Divide dataset into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# STEP 6: Display dataset sizes

print("\n===== DATA SPLIT RESULTS =====")

print("Total records:", len(df))

print("Training records:", len(X_train))

print("Testing records:", len(X_test))


# STEP 7: Verify crop distribution

print("\nTRAINING CROP DISTRIBUTION:")
print(y_train.value_counts())

print("\nTESTING CROP DISTRIBUTION:")
print(y_test.value_counts())


# STEP 8: Final confirmation

print("\nData preprocessing completed successfully!")
print("Dataset is ready for Machine Learning.")
