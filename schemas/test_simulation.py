from pydantic import BaseModel
from typing import Optional

class TestSimulationBase(BaseModel):
    score: float
    status: str

class TestSimulationCreate(TestSimulationBase):
    applicant_id: int

class TestSimulationUpdate(BaseModel):
    score: Optional[float] = None
    status: Optional[str] = None

class TestSimulation(TestSimulationBase):
    id: int
    applicant_id: int
    
    class Config:
        from_attributes = True
