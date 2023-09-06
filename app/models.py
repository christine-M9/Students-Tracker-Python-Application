from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


class Student(Base):
    __tablename__ = 'students'

    id=Column(Integer, primary_key=True)
    name=Column(String)
    student_id=Column(Integer)

    courses = relationship('Course', secondary=student_courses, back_populates='students')

    def get_enrolled_courses(self):
        return [course.name for course in self.courses]


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    students = relationship('Student', secondary=student_courses, back_populates='courses')

engine=create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)