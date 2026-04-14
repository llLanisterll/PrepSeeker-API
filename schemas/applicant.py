from pydantic import BaseModel, EmailStr
from typing import Optional

class ApplicantBase(BaseModel):
    name: str
    email: EmailStr

class ApplicantCreate(ApplicantBase):
    pass

class ApplicantUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class Applicant(ApplicantBase):
    id: int
    
    class Config:
        from_attributes = True
