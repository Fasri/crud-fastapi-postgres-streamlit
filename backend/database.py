from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  # Exemplo com SQLite

# Cria o motor do banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()
