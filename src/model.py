from enum import Enum as PythonEnum
from datetime import datetime
from pydantic import BaseModel, validator, Field
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, create_engine

Base = declarative_base()


VALID_PARAMETER = ["pm25", "pm10", "no", "no2", "o3", "so2", "bc", "co"]
    
    
class MeasurementOrm(Base):
    """
    sqlalchemy model of measurement document
    """
    
    __tablename__ = "measurements"
    
    id = Column(Integer, primary_key=True, nullable=False)
    location_id = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    parameter = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    date_utc = Column(DateTime, nullable=False)
    date_local= Column(DateTime, nullable=False)
    unit = Column(String, nullable=False)
    latitude  = Column(Float, nullable=False)
    longitude  = Column(Float, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=True)
    is_mobile = Column(Boolean, nullable=False)
    is_analysis = Column(String, nullable=True)
    entity = Column(String, nullable=False)
    sensor_type = Column(String, nullable=False)
    
    
class MeasurementModel(BaseModel):
    """
    pydantic model of measurements
    """
    id: int = Field(description="index of the air quality measurements")
    location_id: int 
    location: str
    parameter: str
    value: float
    date_utc: datetime
    date_local: datetime
    unit: str
    latitude: float
    longitude: float
    country: str
    city: str | None = None
    is_mobile: bool
    is_analysis: str | None = None
    entity: str
    sensor_type: str


    @validator('parameter')
    def check_valid_parameters(cls, v):
        if v is not None and v not in VALID_PARAMETER:
            raise ValueError(f"Invalid parameter. Parameter must be one of: {', '.join(item.value for item in VALID_PARAMETER)}")


    @validator('country')
    def check_valid_country(cls, v):
        if v is None:
            raise ValueError(f"Country cannot be null")

    
def create_tables(connection_url: str):
    """
    Creates the DB tables corresponding to the ORM model.

    Args:
        connection_url: the URL to an SQL database.
    """
    engine = create_engine(connection_url, echo=True)
    Base.metadata.create_all(engine)