from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from models.applicant import Applicant as ApplicantModel
from schemas.applicant import Applicant, ApplicantCreate, ApplicantUpdate

router = APIRouter(
    prefix="/applicants",
    tags=["applicants"],
)

# Dependency to get db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Applicant, status_code=status.HTTP_201_CREATED)
def create_applicant(applicant: ApplicantCreate, db: Session = Depends(get_db)):
    db_applicant = db.query(ApplicantModel).filter(ApplicantModel.email == applicant.email).first()
    if db_applicant:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_applicant = ApplicantModel(name=applicant.name, email=applicant.email)
    db.add(new_applicant)
    db.commit()
    db.refresh(new_applicant)
    return new_applicant

@router.get("/", response_model=List[Applicant])
def read_applicants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(ApplicantModel).offset(skip).limit(limit).all()

@router.get("/{applicant_id}", response_model=Applicant)
def read_applicant(applicant_id: int, db: Session = Depends(get_db)):
    applicant = db.query(ApplicantModel).filter(ApplicantModel.id == applicant_id).first()
    if applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")
    return applicant

@router.put("/{applicant_id}", response_model=Applicant)
def update_applicant(applicant_id: int, applicant_update: ApplicantUpdate, db: Session = Depends(get_db)):
    db_applicant = db.query(ApplicantModel).filter(ApplicantModel.id == applicant_id).first()
    if db_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")
    
    update_data = applicant_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_applicant, key, value)
        
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

@router.delete("/{applicant_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_applicant(applicant_id: int, db: Session = Depends(get_db)):
    db_applicant = db.query(ApplicantModel).filter(ApplicantModel.id == applicant_id).first()
    if db_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")
    
    db.delete(db_applicant)
    db.commit()
    return None
