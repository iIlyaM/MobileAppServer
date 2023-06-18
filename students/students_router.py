from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from core.utils import get_db
from . import schemas
from . import services

router = APIRouter(
    tags=['Students']
)


@router.post('/new_student', status_code=status.HTTP_201_CREATED)
async def create_user(request: schemas.CreateStudentModel, database: Session = Depends(get_db)):
    new_student = await services.add_new_student(request, database)
    return new_student


@router.get('/students', response_model=List[schemas.DisplayStudentModel])
async def get_all_students(
        second_name: str | None = None,
        group_number: int | None = None,
        database: Session = Depends(get_db),
):
    return await services.get_students(database, second_name, group_number)


@router.get('/students/no_group_students', response_model=List[schemas.DisplayStudentModel])
async def get_all_no_group_students(
        database: Session = Depends(get_db),
):
    return await services.get_free_students(database)


@router.get('/{student_id}', response_model=schemas.DisplayStudentModel)
async def get_student_by_id(
        student_id: int,
        database: Session = Depends(get_db),
):
    return await services.get_student(student_id, database)


@router.put('/{student_id}', response_model=schemas.DisplayStudentModel)
async def update_student(
        student_id: int,
        stud_data: schemas.UpdateStudentModel,
        database: Session = Depends(get_db)
):
    return await services.update(student_id, database, stud_data)


@router.delete('/{student_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def remove_student_by_id(
        student_id: int,
        database: Session = Depends(get_db),
):
    return await services.delete_student_by_id(student_id, database)


@router.put('/{student_id}/{group_id}', status_code=status.HTTP_200_OK, response_class=Response)
async def remove_student_from_group(
        student_id: int,
        group_id: int,
        database: Session = Depends(get_db),
):
    return await services.delete_student_from_group(student_id, group_id, database)


@router.post('/group/new_group', status_code=status.HTTP_201_CREATED)
async def create_group(request: schemas.Group, database: Session = Depends(get_db)):
    new_group = await services.add_new_group(request, database)
    return new_group


@router.get('/group/groups', response_model=List[schemas.DisplayGroup])
async def get_all_students(
        database: Session = Depends(get_db),
):
    return await services.get_groups(database)


@router.get('/group/{group_id}', response_model=schemas.DisplayGroup)
async def get_group_by_id(
        group_id: int,
        database: Session = Depends(get_db),
):
    return await services.get_group(group_id, database)


@router.put('/group/{group_id}/', response_model=schemas.Group)
async def update_group(
        group_id: int,
        group_data: schemas.Group,
        database: Session = Depends(get_db)
):
    return await services.update_group(group_id, database, group_data)


@router.put('/group/new_student/{group_id}/{student_id}/', status_code=status.HTTP_200_OK)
async def add_student_group(
        group_id: int,
        student_id: int,
        database: Session = Depends(get_db)
):
    return await services.add_student_to_group(student_id, group_id, database)


@router.delete('/group/{group_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def remove_group_by_id(
        group_id: int,
        database: Session = Depends(get_db),
):
    return await services.delete_group_by_id(group_id, database)
