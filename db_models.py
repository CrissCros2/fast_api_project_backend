from sqlalchemy import Column, String, DateTime, UUID, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


# To model many-to-many relationships use link table
class EventPersonAssociation(Base):
    __tablename__ = "eventpersonassociation"
    event_id = Column(UUID, ForeignKey("events.id"), primary_key=True)
    attendee_id = Column(UUID, ForeignKey("persons.id"), primary_key=True)

    event = relationship("EventTable", back_populates="persons")
    person = relationship("PersonTable", back_populates="event")


# Events table
class EventTable(Base):
    __tablename__ = "events"

    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    time = Column(DateTime)
    persons = relationship("EventPersonAssociation", back_populates="event")


# Persons table
class PersonTable(Base):
    __tablename__ = "persons"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)
    event = relationship("EventPersonAssociation", back_populates="person")
