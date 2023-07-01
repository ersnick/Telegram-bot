FROM python:3.9

WORKDIR /user-service

RUN pip install pipenv

RUN pip install uvicorn

RUN pip install fastapi

RUN pip install python-dotenv

RUN pip install sqlalchemy

RUN pip install bcrypt

RUN pip install psycopg2-binary

COPY Pipfile.lock Pipfile.lock

RUN pipenv sync

RUN pipenv install uvicorn

COPY . /user-service

EXPOSE 8082

CMD ["python", "main.py"]