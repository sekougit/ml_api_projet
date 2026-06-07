import joblib
import pandas as pd

from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "pipeline.pkl"

print("MODEL_PATH =", MODEL_PATH)
print("Existe ?", MODEL_PATH.exists())

# mapping des classes Iris
LABELS = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

model = joblib.load(MODEL_PATH)

def predict(data):

    X = pd.DataFrame([data])

    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0]

    return {
        "prediction": LABELS[int(pred)],
        "confidence": float(max(proba)),
        "probabilities": {
            LABELS[i]: float(proba[i])
            for i in range(len(proba))
        }
    }