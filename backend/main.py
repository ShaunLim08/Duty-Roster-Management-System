from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import models, schemas, crud, logic
from database import SessionLocal, engine
from sqlalchemy import func

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/personnel/", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return crud.create_person(db=db, person=person)

@app.get("/personnel/", response_model=List[schemas.Person])
def read_people(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_people(db, skip=skip, limit=limit)

@app.delete("/personnel/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db)):
    crud.delete_person(db, person_id)
    return {"message": "Deleted"}

@app.post("/shifts/", response_model=schemas.Shift)
def create_shift(shift: schemas.ShiftCreate, db: Session = Depends(get_db)):
    return crud.create_shift(db=db, shift=shift)

@app.get("/shifts/", response_model=List[schemas.Shift])
def read_shifts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shifts = crud.get_shifts(db, skip=skip, limit=limit)
    # Enrich with person name for frontend convenience
    for shift in shifts:
        if shift.person:
            shift.person_name = shift.person.name
    return shifts

@app.delete("/shifts/{shift_id}")
def delete_shift(shift_id: int, db: Session = Depends(get_db)):
    crud.delete_shift(db, shift_id)
    return {"message": "Shift deleted"}

@app.get("/statistics/")
def get_statistics(db: Session = Depends(get_db)):
    # Count shifts per person
    stats = db.query(models.Person.name, func.count(models.Shift.id)).join(models.Shift).group_by(models.Person.id).all()
    return [{"name": name, "count": count} for name, count in stats]
