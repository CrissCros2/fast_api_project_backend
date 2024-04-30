from sqlalchemy import Column, String, DateTime, UUID, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


# To model many-to-many relationships use link table
class EventPersonAssociation(Base):
    __tablename__ = "eventpersonassociation"
    person_id = Column(UUID(as_uuid=True), ForeignKey("persons.id"), primary_key=True)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"), primary_key=True)

    event = relationship("EventTable", back_populates="persons")
    person = relationship("PersonTable", back_populates="events")


# Events table
class EventTable(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    time = Column(DateTime)
    persons = relationship("EventPersonAssociation", back_populates="event")


# Persons table
class PersonTable(Base):
    __tablename__ = "persons"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, index=True)
    events = relationship("EventPersonAssociation", back_populates="person")
