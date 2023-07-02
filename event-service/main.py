import logging
from logging import INFO

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from core.routers.event_router import router as event_router

app = FastAPI()
app.include_router(router=event_router, tags=['Event router'])


def main():
    uvicorn.run(app=app, port=8083, host='0.0.0.0', reload=False)


def __config_logger():
    file_log = logging.FileHandler('event-service.log')
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
