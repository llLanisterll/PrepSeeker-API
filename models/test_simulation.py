from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class TestSimulation(Base):
    __tablename__ = "test_simulations"

    id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.id"))
    score = Column(Float)
    status = Column(String)
    
    # Many to One relationship dengan Applicant
    applicant = relationship("Applicant", back_populates="test_simulations")
