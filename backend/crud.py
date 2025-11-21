from sqlalchemy.orm import Session
import models, schemas
from datetime import date

def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()

def get_people(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(name=person.name, age=person.age, position=person.position)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def delete_person(db: Session, person_id: int):
    db_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person

def get_shifts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Shift).offset(skip).limit(limit).all()

def create_shift(db: Session, shift: schemas.ShiftCreate):
    db_shift = models.Shift(date=shift.date, shift_type=shift.shift_type, person_id=shift.person_id)
    db.add(db_shift)
    db.commit()
    db.refresh(db_shift)
    return db_shift

def delete_shift(db: Session, shift_id: int):
    db_shift = db.query(models.Shift).filter(models.Shift.id == shift_id).first()
    if db_shift:
        db.delete(db_shift)
        db.commit()
    return db_shift

def delete_all_shifts(db: Session):
    db.query(models.Shift).delete()
    db.commit()
