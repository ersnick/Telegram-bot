from fastapi import APIRouter, status, Response
from fastapi.encoders import jsonable_encoder

from ..services import event_service as service
from ..models.event import *

router = APIRouter(prefix='/api/events')


@router.get('', response_model=list[EventDTO], status_code=status.HTTP_200_OK)
def get_all_routes():
    events = service.get_all_events()
    return jsonable_encoder(events)


@router.get('/{event_id}', response_model=EventDTO, status_code=status.HTTP_200_OK)
def get_event_by_id(event_id: int):
    event = service.get_event_by_id(event_id=event_id)
    return jsonable_encoder(event)


@router.post('', status_code=status.HTTP_201_CREATED)
def create_event(event: EventDTO) -> Response:
    service.create_event(event=event)
    return Response()


@router.put('/{event_id}', status_code=status.HTTP_200_OK)
def update_event_by_id(event_id: int, event: EventDTO) -> Response:
    event.id = event_id
    service.update_event(event=event)
    return Response()


@router.delete('/{event_id}', status_code=status.HTTP_200_OK)
def delete_event_by_id(event_id: int) -> Response:
    service.delete_event_by_id(event_id=event_id)
    return Response()
