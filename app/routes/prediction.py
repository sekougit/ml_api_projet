from fastapi import APIRouter

from app.schemas.prediction import PredictionInput
from app.services.model_service import predict

router = APIRouter()

@router.post("/predict")
def prediction(data: PredictionInput):

    result = predict(data.dict())

    return {
        "prediction": result
    }