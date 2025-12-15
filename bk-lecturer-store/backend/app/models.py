from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Major(Base):
    __tablename__ = "majors"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(Text)

class Lecturer(Base):
    __tablename__ = "lecturers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    title = Column(String)
    role = Column(String)
    unit = Column(String)
    image = Column(String)
    major_id = Column(Integer, ForeignKey("majors.id"))

    major = relationship("Major")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    lecturer_id = Column(Integer, ForeignKey("lecturers.id"))
    content = Column(Text)
    rating = Column(Integer)

