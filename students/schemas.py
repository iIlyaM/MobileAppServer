from datetime import date
from typing import List

from pydantic import BaseModel


class Group(BaseModel):
    group_number: int
    faculty_name: str

    class Config:
        orm_mode = True


class DisplayStudentModel(BaseModel):
    id: int = 0
    first_name: str | None = None
    second_name: str | None = None
    third_name: str | None = None
    birthday: date | None = None
    group: Group | None = None

    class Config:
        orm_mode = True


class CreateStudentModel(BaseModel):
    first_name: str
    second_name: str
    third_name: str
    birthday: str
    group_id: int | None = None

    class Config:
        orm_mode = True


class DisplayGroup(BaseModel):
    id: int
    group_number: int
    faculty_name: str
    students_amount: int = 0
    students: List[DisplayStudentModel]

    class Config:
        orm_mode = True


class UpdateStudentModel(BaseModel):
    first_name: str | None = None
    second_name: str | None = None
    third_name: str | None = None
    birthday: date | None = None

    class Config:
        orm_mode = True
