from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder

from ..models.group_dto import Group
from ..services.group_service import GroupService, GroupServiceImpl

router = APIRouter(prefix='/api/groups')
group_service: GroupService = GroupServiceImpl()


@router.get('', status_code=200, response_model=list[Group])
def get_all_groups(title: str = ''):
    if title != '':
        groups = group_service.get_groups_by_filter(title=title)
    else:
        groups = group_service.get_all_groups()
    return jsonable_encoder(groups)


@router.get('/{group_id}', status_code=200, response_model=Group)
def get_group_by_id(group_id: int):
    group = group_service.get_group_by_id(group_id=group_id)
    return jsonable_encoder(group)


@router.put('/{group_id}', status_code=200)
def update_group_by_id(group_id: int, group: Group) -> Response:
    group.id = group_id
    group_service.update_group(update_group=group)
    return Response()


@router.post('', status_code=201)
def create_group(group: Group) -> Response:
    group_service.create_group(group=group)
    return Response()


@router.delete('/{group_id}', status_code=200)
def delete_group_by_id(group_id: int) -> Response:
    group_service.delete_group_by_id(group_id=group_id)
    return Response()
