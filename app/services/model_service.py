import joblib
import pandas as pd

model = joblib.load("models/pipeline.pkl")

def predict(data):

    X = pd.DataFrame([data])

    prediction = model.predict(X)

    return int(prediction[0])