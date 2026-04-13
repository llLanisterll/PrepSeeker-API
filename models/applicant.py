from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Applicant(Base):
    __tablename__ = "applicants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    # One to Many relationship dengan TestSimulation
    test_simulations = relationship("TestSimulation", back_populates="applicant")
