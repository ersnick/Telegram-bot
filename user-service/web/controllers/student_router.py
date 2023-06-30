from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder

from ..models.student_dto import Student
from ..services.student_service import StudentService, StudentServiceImpl

router = APIRouter(prefix='/api/students')
student_service: StudentService = StudentServiceImpl()


@router.get('', status_code=200, response_model=list[Student])
def get_all_students(group: str = ''):
    if group != '':
        students = student_service.get_students_by_group(group_name=group)
    else:
        students = student_service.get_all_students()
    return jsonable_encoder(students)


@router.get('/{student_id}', status_code=200, response_model=Student)
def get_student_by_id(student_id: int):
    student = student_service.get_student_by_id(student_id=student_id)
    return jsonable_encoder(student)


@router.put('/{student_id}', status_code=201)
def update_student(student_id: int, student: Student) -> Response:
    student.id = student_id
    student_service.update_student(update_student=student)
    return Response()


@router.delete('/{student_id}', status_code=200)
def delete_student(student_id: int) -> Response:
    student_service.delete_student_by_id(student_id=student_id)
    return Response()
