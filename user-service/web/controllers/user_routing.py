from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from ..services.user_service import UserService, UserServiceImpl
from ..models.user_dto import User

router = APIRouter(prefix='/api/users')
user_service: UserService = UserServiceImpl()


@router.get('', response_model=list[User], status_code=200)
def get_all_users():
    users = user_service.get_all_users()
    return jsonable_encoder(users)
