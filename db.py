from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, MetaData
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from uuid import UUID


engine = create_engine("sqlite:///mydb.db")
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

connection = engine.connect()


# Events table
class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    time = Column(DateTime)
    attendees = relationship("Person", back_populates="event")


class Person(Base):
    __tablename__ = "persons"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)


events_table_exists = engine.dialect.has_table(connection, "events")
persons_table_exists = engine.dialect.has_table(connection, "persons")
if not events_table_exists or not persons_table_exists:
    Base.metadata.create_all(bind=engine)
