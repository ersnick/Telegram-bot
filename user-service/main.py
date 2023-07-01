import logging
from logging import INFO

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

from core.exceptions.illegal_argument_exception import IllegalArgumentException
from web.controllers.group_router import router as group_router
from web.controllers.statement_router import router as statement_router
from web.controllers.student_router import router as student_router
from web.controllers.user_routing import router as user_router

logger = logging.getLogger()

app = FastAPI()
app.include_router(router=user_router, tags=['User router'])
app.include_router(router=statement_router, tags=['Statement router'])
app.include_router(router=student_router, tags=['Student router'])
app.include_router(router=group_router, tags=['Group router'])


@app.exception_handler(IllegalArgumentException)
def runtime_exception_handler(request: Request, e: IllegalArgumentException) -> Response:
    return JSONResponse(status_code=400, content={'message': e.message})


@app.exception_handler(Exception)
def other_exception_handler(request: Request, e: Exception) -> Response:
    return JSONResponse(status_code=500, content={'message': 'server error'})


def main():
    logger.info('App was start')
    uvicorn.run(app=app,
                port=8082,
                reload=False,
                host='0.0.0.0')


def __config_logger():
    file_log = logging.FileHandler('user-service.log')
    console_log = logging.StreamHandler()
    FORMAT = '[%(levelname)s] %(asctime)s : %(message)s | %(filename)s'
    logging.basicConfig(level=INFO,
                        format=FORMAT,
                        handlers=(file_log, console_log),
                        datefmt='%d-%m-%y - %H:%M:%S')


if __name__ == '__main__':
    __config_logger()
    load_dotenv('.env')
    main()
