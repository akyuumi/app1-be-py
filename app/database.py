import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.models import User
import yaml

Base = declarative_base()

class DBConfig:
    
    def __init__(self, config_path):
        db_host = os.environ.get("DB_HOST")
        db_port = os.environ.get("DB_PORT")
        db_name = os.environ.get("DB_NAME")
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")

def get_user_by_id(user_id: int) -> User:
    db_config = DBConfig("config/config.yaml")
    engine = create_engine(f"postgresql://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    
    user_db = session.query(UserDB).filter(UserDB.user_id == user_id).first()
    session.close()
    
    if user_db:
        return User(user_id=user_db.user_id, name=user_db.name)
    return None

class UserDB(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
