from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Person(Base):
    __tablename__ = "personnel"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    position = Column(String)

    shifts = relationship("Shift", back_populates="person", cascade="all, delete-orphan")

class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    shift_type = Column(String) # e.g., "Day", "Night"
    person_id = Column(Integer, ForeignKey("personnel.id"))

    person = relationship("Person", back_populates="shifts")
