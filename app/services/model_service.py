import joblib
import pandas as pd

import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "models", "pipeline.pkl")

model = joblib.load(model_path)

def predict(data):

    X = pd.DataFrame([data])

    prediction = model.predict(X)

    return int(prediction[0])