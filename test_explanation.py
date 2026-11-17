
from modules.explanation import explain_prediction

# Sample farmer input
prediction, explanation = explain_prediction(
    90,
    42,
    43,
    20.87,
    82.00,
    6.50,
    202.93
)

print("\n===== CROP PREDICTION =====")
print("Recommended Crop:", prediction)

print("\n===== FEATURE SENSITIVITY EXPLANATION =====")
print(explanation.to_string(index=False))

print("\n===== MOST INFLUENTIAL FEATURE =====")
print(explanation.iloc[0]["Feature"])
