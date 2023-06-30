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


@router.get('/{user_id}', response_model=User, status_code=200)
def get_user_by_id(user_id: int):
    user = user_service.get_user_by_id(user_id=user_id)
    return jsonable_encoder(user)
