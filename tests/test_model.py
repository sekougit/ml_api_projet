from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "pipeline.pkl"

print(MODEL_PATH)
print(MODEL_PATH.exists())

model = joblib.load(MODEL_PATH)

print("OK")