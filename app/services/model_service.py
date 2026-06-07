import joblib
import pandas as pd

from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "pipeline.pkl"

print("MODEL_PATH =", MODEL_PATH)
print("Existe ?", MODEL_PATH.exists())

model = joblib.load(MODEL_PATH)
def predict(data):

    X = pd.DataFrame([data])

    prediction = model.predict(X)

    return int(prediction[0])