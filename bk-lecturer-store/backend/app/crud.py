from sqlalchemy.orm import Session
from . import models

def get_all_lecturers(db: Session):
    return db.query(models.Lecturer).all()

def get_major_by_name(db: Session, name: str):
    return db.query(models.Major).filter(models.Major.name.ilike(f"%{name}%")).first()

