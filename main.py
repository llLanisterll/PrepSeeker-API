from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PrepSeeker API</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            body {
                background-color: #0f172a; /* Slate 900 */
                color: #f8fafc;
                font-family: 'Inter', sans-serif;
            }
            .glow-bg {
                position: fixed;
                width: 800px;
                height: 800px;
                background: radial-gradient(circle, rgba(139,92,246,0.15) 0%, rgba(15,23,42,0) 70%);
                top: 0;
                left: 50%;
                transform: translateX(-50%);
                z-index: -1;
                pointer-events: none;
            }
            .gradient-text {
                background: linear-gradient(to right, #a855f7, #ec4899);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .glass-card {
                background: rgba(30, 41, 59, 0.5); /* Slate 800 with opacity */
                backdrop-filter: blur(12px);
                border: 1px solid rgba(51, 65, 85, 0.8); /* Slate 700 */
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            }
            .btn-glow {
                background: linear-gradient(to right, #9333ea, #db2777); /* Purple 600 to Pink 600 */
                transition: all 0.3s ease;
            }
            .btn-glow:hover {
                box-shadow: 0 0 20px rgba(168, 85, 247, 0.6);
                transform: translateY(-2px);
                background: linear-gradient(to right, #a855f7, #ec4899);
            }
            .code-block {
                background-color: #0f172a; /* Slate 900 */
                border: 1px solid #334155; /* Slate 700 */
            }
        </style>
    </head>
    <body class="relative min-h-screen pb-20">
        <div class="glow-bg"></div>
        
        <!-- MAIN CONTAINER -->
        <main class="max-w-4xl mx-auto px-6 pt-20 z-10 relative">
            
            <!-- HERO SECTION -->
            <div class="text-center mb-16">
                <h1 class="text-5xl md:text-6xl font-extrabold mb-6 gradient-text drop-shadow-lg tracking-tight">PrepSeeker API</h1>
                <p class="text-slate-400 text-lg md:text-xl max-w-2xl mx-auto mb-10 leading-relaxed">
                    API backend berkinerja tinggi untuk Manajemen Pelamar Kerja & Simulasi Tes. Dilengkapi dengan dokumentasi interaktif yang kuat.
                </p>
                <a href="/docs" class="inline-flex items-center justify-center px-8 py-4 text-lg font-bold text-white rounded-full btn-glow">
                    Buka Interactive API (Swagger UI) 
                    <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </a>
            </div>

            <!-- INFORMASI PROYEK -->
            <div class="glass-card p-8 rounded-2xl mb-12 transition-all hover:border-slate-500">
                <h2 class="text-2xl font-bold text-slate-200 mb-4 border-b border-slate-700 pb-3">Informasi Proyek UTS</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                    <div>
                        <p class="text-slate-400"><span class="text-slate-300 font-semibold">Mata Kuliah:</span> Pemrograman Web Lanjutan</p>
                        <p class="text-slate-400 mt-2"><span class="text-slate-300 font-semibold">Teknologi Dasar:</span> FastAPI & Python 3.9+</p>
                    </div>
                    <div>
                        <p class="text-slate-400"><span class="text-slate-300 font-semibold">Database & ORM:</span> SQLite + SQLAlchemy</p>
                        <p class="text-slate-400 mt-2"><span class="text-slate-300 font-semibold">Keamanan:</span> JWT Auth & Bcrypt</p>
                    </div>
                </div>
            </div>

            <!-- DESKRIPSI PROYEK -->
            <div class="mb-12">
                <h2 class="text-2xl font-bold text-slate-200 mb-4 flex items-center">
                    <svg class="w-6 h-6 mr-2 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    Deskripsi Proyek
                </h2>
                <p class="text-slate-400 leading-relaxed text-justify">
                    PrepSeeker API adalah sebuah sistem backend RESTful berbasis arsitektur modular yang dirancang untuk mengelola data pelamar kerja secara efisien. Proyek ini mendemonstrasikan implementasi CRUD (Create, Read, Update, Delete) dua entitas utama, yakni <span class="text-slate-300 font-semibold">Applicant</span> dan <span class="text-slate-300 font-semibold">TestSimulation</span>, yang saling terhubung melalui relasi One-to-Many menggunakan SQLAlchemy. Sistem ini diproteksi secara ketat menggunakan metode otentikasi JWT (JSON Web Token), di mana keamanan data dijamin melalui hashing kata sandi, serta validasi skema input yang presisi menggunakan Pydantic.
                </p>
            </div>

            <!-- FITUR UTAMA -->
            <div class="mb-12">
                <h2 class="text-2xl font-bold text-slate-200 mb-6 flex items-center">
                    <svg class="w-6 h-6 mr-2 text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                    Fitur Utama
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="glass-card p-5 rounded-xl border-l-4 border-l-purple-500">
                        <h3 class="text-lg font-semibold text-slate-200 mb-1">Manajemen Pelamar</h3>
                        <p class="text-sm text-slate-400">Endpoint publik untuk registrasi, pembaruan biodata, hingga pencarian pelamar.</p>
                    </div>
                    <div class="glass-card p-5 rounded-xl border-l-4 border-l-pink-500">
                        <h3 class="text-lg font-semibold text-slate-200 mb-1">Otentikasi JWT</h3>
                        <p class="text-sm text-slate-400">Login aman menggunakan token berbatas waktu untuk mengakses resource privat.</p>
                    </div>
                    <div class="glass-card p-5 rounded-xl border-l-4 border-l-purple-500">
                        <h3 class="text-lg font-semibold text-slate-200 mb-1">Skor Simulasi Tes</h3>
                        <p class="text-sm text-slate-400">Pencatatan riwayat skor tes (0-100) yang terikat langsung ke ID pelamar (Protected).</p>
                    </div>
                    <div class="glass-card p-5 rounded-xl border-l-4 border-l-pink-500">
                        <h3 class="text-lg font-semibold text-slate-200 mb-1">Integritas Data</h3>
                        <p class="text-sm text-slate-400">Penggunaan Cascade Delete untuk membersihkan orphan data secara otomatis.</p>
                    </div>
                </div>
            </div>

            <!-- STRUKTUR DIREKTORI -->
            <div class="mb-12">
                <h2 class="text-2xl font-bold text-slate-200 mb-4 flex items-center">
                    <svg class="w-6 h-6 mr-2 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg>
                    Struktur Direktori
                </h2>
                <div class="code-block p-6 rounded-xl overflow-x-auto text-sm text-slate-300 font-mono leading-loose shadow-inner">
                    <span class="text-purple-400">PrepSeeker-API/</span><br>
                    ├── <span class="text-slate-400">main.py</span> <span class="text-slate-500 italic ml-4"># File utama aplikasi (Entry point)</span><br>
                    ├── <span class="text-slate-400">database.py</span> <span class="text-slate-500 italic ml-4"># Konfigurasi koneksi SQLite</span><br>
                    ├── <span class="text-purple-400">auth/</span><br>
                    │   └── <span class="text-slate-400">security.py</span> <span class="text-slate-500 italic ml-4"># Logika JWT Token & Hashing Bcrypt</span><br>
                    ├── <span class="text-purple-400">models/</span> <span class="text-slate-500 italic ml-4"># Definisi Skema Tabel Database (SQLAlchemy)</span><br>
                    │   ├── <span class="text-slate-400">applicant.py</span><br>
                    │   └── <span class="text-slate-400">test_simulation.py</span><br>
                    ├── <span class="text-purple-400">routers/</span> <span class="text-slate-500 italic ml-4"># Definisi Endpoint API (Path Operations)</span><br>
                    │   ├── <span class="text-slate-400">applicant.py</span><br>
                    │   ├── <span class="text-slate-400">test_simulation.py</span><br>
                    │   └── <span class="text-slate-400">auth.py</span><br>
                    └── <span class="text-purple-400">schemas/</span> <span class="text-slate-500 italic ml-4"># Definisi Validasi Request/Response (Pydantic)</span><br>
                        ├── <span class="text-slate-400">applicant.py</span><br>
                        └── <span class="text-slate-400">test_simulation.py</span>
                </div>
            </div>

            <!-- INSTALASI & SETUP -->
            <div class="mb-12">
                <h2 class="text-2xl font-bold text-slate-200 mb-4 flex items-center">
                    <svg class="w-6 h-6 mr-2 text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
                    Cara Menjalankan
                </h2>
                <div class="space-y-6">
                    <!-- Step 1 -->
                    <div>
                        <h3 class="text-slate-300 font-semibold mb-2">1. Aktifkan Virtual Environment</h3>
                        <div class="code-block p-4 rounded-lg flex items-center text-sm font-mono text-pink-300">
                            <span class="text-slate-500 mr-3">$</span> source venv/bin/activate
                        </div>
                    </div>
                    <!-- Step 2 -->
                    <div>
                        <h3 class="text-slate-300 font-semibold mb-2">2. Install Dependensi</h3>
                        <div class="code-block p-4 rounded-lg flex items-center text-sm font-mono text-pink-300">
                            <span class="text-slate-500 mr-3">$</span> pip install -r requirements.txt
                        </div>
                    </div>
                    <!-- Step 3 -->
                    <div>
                        <h3 class="text-slate-300 font-semibold mb-2">3. Jalankan Server Uvicorn</h3>
                        <div class="code-block p-4 rounded-lg flex items-center text-sm font-mono text-purple-300">
                            <span class="text-slate-500 mr-3">$</span> uvicorn main:app --reload
                        </div>
                    </div>
                </div>
            </div>
            
            <footer class="text-center text-slate-500 text-sm mt-16 pt-8 border-t border-slate-800">
                &copy; 2026 PrepSeeker API. Dibuat dengan FastAPI.
            </footer>

        </main>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

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
