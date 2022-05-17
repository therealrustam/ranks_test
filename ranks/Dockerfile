FROM python:3.10-slim

COPY ./ /app

WORKDIR /app

COPY requirements.txt pwd

RUN pip3 install --upgrade pip && pip3 install -r /app/requirements.txt --no-cache-dir

CMD ["python", "manage.py", "runserver", "0:8000"]