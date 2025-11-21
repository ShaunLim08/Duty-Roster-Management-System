from sqlalchemy.orm import Session
import models, schemas
from datetime import date, timedelta
import random

def auto_schedule(db: Session, start_date: date, days: int):
    # Clear existing shifts in that range? Or just append?
    # For simplicity, let's clear all shifts first or just assume empty.
    # The user requirement says "distribute shifts based on number of employees and working days".
    
    people = db.query(models.Person).all()
    if not people:
        return {"error": "No personnel available"}

    shifts_to_create = []
    current_date = start_date
    
    # Simple Round Robin
    person_idx = 0
    
    for _ in range(days):
        # Create a Day shift
        person = people[person_idx % len(people)]
        shifts_to_create.append(models.Shift(date=current_date, shift_type="Day", person_id=person.id))
        person_idx += 1
        
        # Create a Night shift? Or just one shift per day?
        # Let's assume 1 shift per day for simplicity unless specified.
        # Requirement says "Shift Scheduling".
        
        current_date += timedelta(days=1)

    db.add_all(shifts_to_create)
    db.commit()
    return {"message": f"Scheduled {len(shifts_to_create)} shifts"}
