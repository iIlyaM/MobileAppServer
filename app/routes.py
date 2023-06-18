from fastapi import APIRouter

from app.students import students_router

routes = APIRouter()

routes.include_router(students_router.router, prefix="/students")
