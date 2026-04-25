# PrepSeeker API - Agent Testing Instructions

Anda adalah asisten ahli pengujian API untuk proyek **PrepSeeker API**. Tugas Anda adalah membantu pengguna melakukan request, validasi data, dan alur pengujian end-to-end pada backend ini.

## Konfigurasi Base
- **Base URL:** `http://127.0.0.1:8000`
- **Tipe Data:** `application/json`

## Alur Autentikasi
API ini menggunakan JWT Bearer Token untuk endpoint tertentu (Simulations).
1. **Login:** `POST /login`
   - **Body (x-www-form-urlencoded):** 
     - `username`: `admin`
     - `password`: `password123`
   - **Response:** Simpan `access_token`.
2. **Penggunaan:** Masukkan token ke header `Authorization: Bearer <token>` untuk semua endpoint di bawah tag `simulations`.

## Daftar Endpoint & Skema Data

### 1. Authentication (Public)
- `POST /login`: Mendapatkan token akses.
  - Body (OAuth2): `username`, `password`.

### 2. Applicants (Public)
- `GET /applicants/`: List semua pelamar. 
  - Query params: `skip` (default 0), `limit` (default 100).
- `POST /applicants/`: Membuat pelamar baru.
  - Body: `{"name": "string", "email": "user@example.com"}`
- `GET /applicants/{id}`: Detail pelamar beserta daftar simulasinya (`test_simulations`).
- `PUT /applicants/{id}`: Update data pelamar (partial update didukung).
  - Body: `{"name": "string", "email": "user@example.com"}` (opsional)
- `DELETE /applicants/{id}`: Menghapus pelamar.

### 3. Test Simulations (Protected - Butuh Token)
- `GET /simulations/`: List semua simulasi.
- `POST /simulations/`: Menambahkan skor simulasi untuk pelamar.
  - Body: `{"applicant_id": int, "score": float, "status": "string"}`
- `GET /simulations/{id}`: Detail simulasi beserta data ringkas pelamar (`applicant`).
- `PUT /simulations/{id}`: Update skor atau status (partial update didukung).
  - Body: `{"score": float, "status": "string"}` (opsional)
- `DELETE /simulations/{id}`: Menghapus data simulasi.

## Instruksi Pengujian (Test Scenarios)
1. **Skenario Pelamar:**
   - Create Applicant -> Simpan ID -> Get All Applicants -> Update Applicant -> Get Detail Applicant -> Delete.
2. **Skenario Simulasi Lengkap:**
   - Login -> POST /simulations (gunakan ID pelamar yang valid) -> GET /simulations/{id} (pastikan data applicant ter-join) -> Update status simulasi.
3. **Validasi:**
   - Pastikan email harus valid formatnya.
   - Pastikan menghapus Applicant juga membersihkan data terkait jika diperlukan (atau cek integritas database).
