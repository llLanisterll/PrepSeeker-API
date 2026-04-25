from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import timedelta
from auth.security import verify_password, get_password_hash, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=["Authentication"])

# Simulasi database user sederhana untuk keperluan UTS.
# Pada aplikasi nyata, data ini harus disimpan di tabel Users melalui session database.
dummy_db = {
    "admin": {
        "username": "admin",
        # Default password adalah "password123"
        "hashed_password": get_password_hash("password123")
    }
}

# Schema untuk pendaftaran user baru
class UserCreate(BaseModel):
    username: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate):
    if user.username in dummy_db:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar")
    
    # Simpan ke dummy_db (Pada aplikasi nyata harusnya ke database session sesungguhnya)
    dummy_db[user.username] = {
        "username": user.username,
        "hashed_password": get_password_hash(user.password)
    }
    return {"message": "User berhasil didaftarkan"}

@router.post("/login", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Cek user dari database dummy
    user = dummy_db.get(form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username tidak ditemukan",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verifikasi password
    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password salah",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Buat JWT token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
