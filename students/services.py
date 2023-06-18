from .models import Student, Group
from .schemas import UpdateStudentModel, DisplayGroup
from typing import List
from core.utils import add_entity
from fastapi import HTTPException


async def add_new_student(request, database):
    if request.group_id is not None:
        group = database.query(Group).filter(Group.id == request.group_id).first()
        new_student = Student(
            first_name=request.first_name,
            second_name=request.second_name,
            third_name=request.third_name,
            birthday=request.birthday,
            group=group
        )
        add_entity(database, new_student)
        group.students_amount += 1
        database.commit()
        database.refresh(group)
    else:
        new_student = Student(
            first_name=request.first_name,
            second_name=request.second_name,
            third_name=request.third_name,
            birthday=request.birthday
        )
        add_entity(database, new_student)

    return new_student


async def get_students(database, second_name: str | None = None, group_num: int | None = None):
    if second_name:
        students = database.query(Student).join(Group, Student.group_id == Group.id).filter(
            Student.second_name.contains(second_name)).all()
    elif group_num:
        students = database.query(Student).join(Group, Student.group_id == Group.id).filter(
            Group.group_number == group_num).all()
    else:
        students = database.query(Student).join(Group, Student.group_id == Group.id).all()
    return students


async def get_free_students(database):
    students = database.query(Student).where(Student.group_id == None).all()
    return students


#
# async def get_students_by_group_id(group_id, database):
#     students = database.query(Student).where(Student.group_id == group_id).all()
#     return students


async def get_student(student_id, database) -> Student:
    return database.query(Student).get(student_id)


async def update(student_id, database, upd_student: UpdateStudentModel):
    student = database.query(Student).get(student_id)
    student_data = upd_student.dict(exclude_unset=True)
    for key, value in student_data.items():
        if value is not None:
            setattr(student, key, value)
    database.commit()
    database.refresh(student)
    return student


async def delete_student_by_id(student_id, database):
    student = database.query(Student).filter(Student.id == student_id).first()
    group = database.query(Group).get(student.group_id)
    group.students_amount -= 1
    database.query(Student).filter(Student.id == student_id).delete()
    database.commit()
    database.refresh(group)


async def add_new_group(request, database):
    new_group = Group(
        group_number=request.group_number,
        faculty_name=request.faculty_name
    )
    add_entity(database, new_group)
    return new_group


async def get_groups(database) -> List[Group]:
    groups = database.query(Group).all()
    return groups


async def get_group(group_id, database):
    group = database.query(Group).get(group_id)
    students = database.query(Student).join(Group, Student.group_id == group_id).all()
    return DisplayGroup(id=group.id, group_number=group.group_number, faculty_name=group.faculty_name,
                        students_amount=group.students_amount, students=students)


async def delete_group_by_id(group_id, database):
    group = database.query(Group).filter(Group.id == group_id).first()
    students = database.query(Student).where(Student.group_id == group_id).all()
    if group.students_amount > 0 or len(students) > 0:
        raise HTTPException(
            status_code=400,
            detail="В группе есть студенты.",
        )
    database.query(Group).filter(Group.id == group_id).delete()
    database.commit()


async def delete_student_from_group(student_id, group_id, database):
    group = database.query(Group).get(group_id)
    student = database.query(Student).get(student_id)
    student.group_id = None
    student.group = None
    group.students_amount -= 1
    database.commit()
    database.refresh(group)
    database.refresh(student)


async def update_group(group_id, database, upd_group: Group):
    group = database.query(Group).get(group_id)
    group_data = upd_group.dict(exclude_unset=True)
    for key, value in group_data.items():
        setattr(group, key, value)
    database.commit()
    database.refresh(group)
    return group


async def add_student_to_group(student_id, group_id, database):
    student = database.query(Student).get(student_id)
    group = database.query(Group).get(group_id)
    student.group_id = group.id
    group.students_amount += 1
    database.commit()
    database.refresh(group)
    database.refresh(student)
    return group
