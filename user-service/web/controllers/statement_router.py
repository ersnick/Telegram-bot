from core.exceptions.illegal_argument_exception import IllegalArgumentException
from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder

from ..models.statement_dto import Statement
from ..services.statement_service import StatementService, StatementServiceImpl

router = APIRouter(prefix='/api/statements')
statement_service: StatementService = StatementServiceImpl()


@router.get('', response_model=list[Statement], status_code=200)
def get_all_statements(filter: str = ''):
    if filter == '':
        statements = statement_service.get_all_statements()
    elif filter == 'unchecked':
        statements = statement_service.get_unchecked_statements()
    else:
        raise IllegalArgumentException(message='Wrong filter')

    return jsonable_encoder(statements)


@router.post('/{statement_id}/accept', status_code=200)
def accept_statement(statement_id: int, statement: Statement) -> Response:
    statement.id = statement_id
    statement_service.accept_statement(accept_statement=statement)
    return Response()


@router.post('/{statement_id}/dismiss', status_code=200)
def dismiss_statement(statement_id: int) -> Response:
    statement_service.dismiss_statement(statement_id=statement_id)
    return Response()
