from pydantic import BaseModel, EmailStr
from typing import Optional, List


# ============================================
# Schema Dasar (Base)
# ============================================

class ApplicantBase(BaseModel):
    """Schema dasar untuk field-field Applicant."""
    name: str
    email: EmailStr


# ============================================
# Schema untuk Input (Create & Update)
# ============================================

class ApplicantCreate(ApplicantBase):
    """Schema untuk membuat Applicant baru. 
    Semua field wajib diisi (name, email).
    """
    pass


class ApplicantUpdate(BaseModel):
    """Schema untuk mengupdate Applicant.
    Semua field bersifat opsional (partial update).
    """
    name: Optional[str] = None
    email: Optional[EmailStr] = None


# ============================================
# Schema untuk Output / Response
# ============================================

class ApplicantResponse(ApplicantBase):
    """Schema response standar untuk Applicant (tanpa relasi)."""
    id: int

    class Config:
        from_attributes = True


# ============================================
# Schema Response dengan Relasi
# ============================================

# Forward reference — kita import di bawah untuk menghindari circular import
from schemas.test_simulation import TestSimulationResponse  # noqa: E402


class ApplicantWithSimulations(ApplicantResponse):
    """Schema response Applicant beserta daftar TestSimulation-nya.
    Digunakan saat ingin menampilkan detail lengkap Applicant di API.
    """
    test_simulations: List[TestSimulationResponse] = []

    class Config:
        from_attributes = True
