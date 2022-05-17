FROM python:3.8-slim

RUN mkdir /app


COPY ranks/requirements.txt /app


RUN pip install -r /app/requirements.txt --no-cache-dir


COPY ranks/ /app


WORKDIR /app


CMD ["python", "manage.py", "runserver", "0:8000"] 