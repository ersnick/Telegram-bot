from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from ..models.statement_dto import Statement
from ..services.statement_service import StatementService, StatementServiceImpl

router = APIRouter(prefix='/api/statements')
statement_service: StatementService = StatementServiceImpl()


@router.get('')
def get_all_statements(filter: str = ''):
    if filter == '':
        statements = statement_service.get_all_statements()
    elif filter == 'unchecked':
        statements = statement_service.get_unchecked_statements()
    else:
        raise Exception('Wrong filter')

    return jsonable_encoder(statements)


@router.post('/{statement_id}/accept')
def accept_statement(statement_id: int, statement: Statement):
    statement.id = statement_id
    statement_service.accept_statement(statement=statement)
