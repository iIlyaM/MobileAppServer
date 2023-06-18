from sqlalchemy import Column, String, Integer, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from core.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    third_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)

    group_id = Column(Integer, ForeignKey("groups.id"))
    group = relationship("Group", back_populates="students")


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    group_number = Column(Integer, nullable=False)
    faculty_name = Column(String, nullable=False)
    students_amount = Column(Integer, default=0)
    students = relationship("Student", back_populates="group")

