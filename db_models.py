from sqlalchemy import Column, String, DateTime, UUID

from db import Base


# Events table
class EventTable(Base):
    __tablename__ = "events"

    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    time = Column(DateTime)
    # attendees = relationship("PersonTable", back_populates="event")


class PersonTable(Base):
    __tablename__ = "persons"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)
