from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PredictionHistory(Base):

    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True)

    prediction = Column(Integer)

    sepal_length = Column(Float)

    sepal_width = Column(Float)

    petal_length = Column(Float)

    petal_width = Column(Float)