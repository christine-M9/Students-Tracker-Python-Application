from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id=Column(Integer, primary_key=True)
    name=Column(String)
    student_id=Column(Integer)

engine=create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)