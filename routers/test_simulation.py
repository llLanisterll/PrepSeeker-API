from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from models.test_simulation import TestSimulation as TestSimulationModel
from models.applicant import Applicant as ApplicantModel
from schemas.test_simulation import TestSimulation, TestSimulationCreate, TestSimulationUpdate

router = APIRouter(
    prefix="/simulations",
    tags=["simulations"],
)

# Dependency to get db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TestSimulation, status_code=status.HTTP_201_CREATED)
def create_test_simulation(simulation: TestSimulationCreate, db: Session = Depends(get_db)):
    # Check if applicant exists before creating simulation
    db_applicant = db.query(ApplicantModel).filter(ApplicantModel.id == simulation.applicant_id).first()
    if not db_applicant:
        raise HTTPException(status_code=404, detail="Applicant not found")
        
    new_simulation = TestSimulationModel(
        applicant_id=simulation.applicant_id,
        score=simulation.score,
        status=simulation.status
    )
    db.add(new_simulation)
    db.commit()
    db.refresh(new_simulation)
    return new_simulation

@router.get("/", response_model=List[TestSimulation])
def read_test_simulations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(TestSimulationModel).offset(skip).limit(limit).all()

@router.get("/{simulation_id}", response_model=TestSimulation)
def read_test_simulation(simulation_id: int, db: Session = Depends(get_db)):
    simulation = db.query(TestSimulationModel).filter(TestSimulationModel.id == simulation_id).first()
    if simulation is None:
        raise HTTPException(status_code=404, detail="Test Simulation not found")
    return simulation

@router.put("/{simulation_id}", response_model=TestSimulation)
def update_test_simulation(simulation_id: int, simulation_update: TestSimulationUpdate, db: Session = Depends(get_db)):
    db_simulation = db.query(TestSimulationModel).filter(TestSimulationModel.id == simulation_id).first()
    if db_simulation is None:
        raise HTTPException(status_code=404, detail="Test Simulation not found")
    
    update_data = simulation_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_simulation, key, value)
        
    db.commit()
    db.refresh(db_simulation)
    return db_simulation

@router.delete("/{simulation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_test_simulation(simulation_id: int, db: Session = Depends(get_db)):
    db_simulation = db.query(TestSimulationModel).filter(TestSimulationModel.id == simulation_id).first()
    if db_simulation is None:
        raise HTTPException(status_code=404, detail="Test Simulation not found")
    
    db.delete(db_simulation)
    db.commit()
    return None
