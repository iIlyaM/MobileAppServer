from fastapi import APIRouter

from students import students_router

routes = APIRouter()

routes.include_router(students_router.router, prefix="/students")
