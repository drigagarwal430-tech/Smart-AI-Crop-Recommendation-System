
import pandas as pd
import joblib

# Load the trained Random Forest model
model = joblib.load("models/crop_model.pkl")

# Load the dataset to calculate median values
dataset = pd.read_csv("dataset/Crop_recommendation.csv")

FEATURES = [
    "N", "P", "K",
    "temperature", "humidity", "ph", "rainfall"
]

# Calculate the median value of each input feature
median_values = dataset[FEATURES].median()


def explain_prediction(n, p, k, temperature, humidity, ph, rainfall):

    input_data = pd.DataFrame([{
        "N": n,
        "P": p,
        "K": k,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }])

    # Predict the crop
    prediction = model.predict(input_data)[0]

    # Get the predicted crop's probability
    class_index = list(model.classes_).index(prediction)
    original_probability = model.predict_proba(input_data)[0][class_index]

    results = []

    # Change one feature at a time to its dataset median
    for feature in FEATURES:

        modified_data = input_data.copy()
        modified_data.loc[0, feature] = median_values[feature]

        modified_probability = model.predict_proba(
            modified_data
        )[0][class_index]

        # Positive or negative change in probability
        impact = original_probability - modified_probability

        results.append({
            "Feature": feature,
            "Input Value": input_data.loc[0, feature],
            "Impact": impact,
            "Importance": abs(impact)
        })

    explanation = pd.DataFrame(results)

    # Show the most influential feature first
    explanation = explanation.sort_values(
        by="Importance",
        ascending=False
    )

    return prediction, explanation
