from pydantic import BaseModel, Field
from typing import Optional


# ============================================
# Schema Dasar (Base)
# ============================================

class TestSimulationBase(BaseModel):
    """Schema dasar untuk field-field TestSimulation."""
    score: float = Field(..., ge=0.0, le=100.0, description="Skor simulasi dari 0 hingga 100")
    status: str


# ============================================
# Schema untuk Input (Create & Update)
# ============================================

class TestSimulationCreate(TestSimulationBase):
    """Schema untuk membuat TestSimulation baru.
    Field applicant_id wajib untuk menghubungkan ke Applicant.
    """
    applicant_id: int


class TestSimulationUpdate(BaseModel):
    """Schema untuk mengupdate TestSimulation.
    Semua field bersifat opsional (partial update).
    """
    score: Optional[float] = Field(None, ge=0.0, le=100.0)
    status: Optional[str] = None


# ============================================
# Schema untuk Output / Response
# ============================================

class TestSimulationResponse(TestSimulationBase):
    """Schema response standar untuk TestSimulation (tanpa relasi)."""
    id: int
    applicant_id: int

    class Config:
        from_attributes = True


# ============================================
# Schema Response dengan Relasi
# ============================================

class ApplicantBrief(BaseModel):
    """Schema ringkas Applicant, digunakan di dalam nested response.
    Mencegah circular import dengan tidak mengimport dari schemas.applicant.
    """
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class TestSimulationWithApplicant(TestSimulationResponse):
    """Schema response TestSimulation beserta data Applicant-nya.
    Digunakan saat ingin menampilkan detail lengkap simulasi di API.
    """
    applicant: ApplicantBrief

    class Config:
        from_attributes = True
