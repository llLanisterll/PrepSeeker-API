from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup database URL (menggunakan SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./prepseeker.db"

# Membuat database engine
# "check_same_thread": False hanya diperlukan untuk SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Membuat SessionLocal class, setiap instance dari kelas ini akan menjadi database session aktual
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Membuat base class untuk membuat model database (ORM models)
Base = declarative_base()
