from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ShiftBase(BaseModel):
    date: date
    shift_type: str
    person_id: int

class ShiftCreate(ShiftBase):
    pass

class Shift(ShiftBase):
    id: int
    person_name: Optional[str] = None # For convenience in frontend

    class Config:
        orm_mode = True

class PersonBase(BaseModel):
    name: str
    age: int
    position: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    shifts: List[Shift] = []

    class Config:
        orm_mode = True
