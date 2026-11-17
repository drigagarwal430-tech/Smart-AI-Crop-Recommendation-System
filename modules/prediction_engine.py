
import joblib
import pandas as pd

# Load the saved Random Forest model
model = joblib.load("models/crop_model.pkl")


def recommend_crop(n, p, k, temperature,
                   humidity, ph, rainfall):

    # Prepare farmer input
    input_data = pd.DataFrame([{
        "N": n,
        "P": p,
        "K": k,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }])

    # Predict the most suitable crop
    prediction = model.predict(input_data)[0]

    # Get prediction scores for all crops
    probabilities = model.predict_proba(input_data)[0]

    # Rank the top five crops
    results = sorted(
        zip(model.classes_, probabilities),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    return prediction, results
