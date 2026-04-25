# PrepSeeker API

API backend untuk sistem simulasi tes psikologi dan analisis resume, dibangun menggunakan FastAPI dan SQLAlchemy.

## 🚀 Instalasi & Setup

1. **Clone Repository**

   ```bash
   git clone <url-repository-anda>
   cd PrepSeeker-API
   ```

2. **Buat Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Pastikan Anda sudah mengaktifkan virtual environment.

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Server**
   ```bash
   python -m uvicorn main:app --reload
   ```
   Server akan berjalan pada `http://127.0.0.1:8000`.

## 📋 Dokumentasi API (Swagger UI)

Setelah server berjalan, Anda dapat mengakses dokumentasi interaktif di:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 📂 Struktur Proyek

- `main.py`: Entry point aplikasi, berisi konfigurasi FastAPI dan router.
- `database.py`: Konfigurasi koneksi database SQLAlchemy dan model `Base`.
- `models/`: Definisi model database (Applicant, TestSimulation).
- `schemas/`: Skema data Pydantic untuk validasi input/output.
- `routes/`: Definisi endpoint API (auth, applicants, simulations).
- `services/`: Logika bisnis dan interaksi database.
- `utils/`: Helper functions (misalnya untuk JWT).

## 🛠️ Teknologi yang Digunakan

- **Framework**: FastAPI
- **Database**: SQLAlchemy (SQLite untuk development)
- **Validasi Data**: Pydantic
- **Autentikasi**: JWT (JSON Web Tokens)
- **Server**: Uvicorn
