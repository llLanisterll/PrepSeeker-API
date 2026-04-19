from fastapi import FastAPI
from database import engine, Base

from routers import applicant, test_simulation, auth

from models.applicant import Applicant
from models.test_simulation import TestSimulation

# Auto-generate tables in the database right when the app starts
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PrepSeeker API",
    description="API untuk Job Seeker Prep Application",
    version="1.0.0"
)

# Memasukkan router untuk entitas-entitas kita
app.include_router(applicant.router)
app.include_router(test_simulation.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Selamat datang di PrepSeeker API"}

# ==========================================
# INSTRUKSI MENJALANKAN SERVER
# ==========================================
# 1. Buka terminal barumu.
# 2. Pastikan virtual environment kamu sudah aktif.
# 3. Jalankan perintah berikut:
#      uvicorn main:app --reload
#
# 4. Buka browser dan pergi ke URL berikut untuk melihat Swagger UI:
#      http://127.0.0.1:8000/docs
# ==========================================
