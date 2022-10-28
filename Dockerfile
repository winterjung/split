FROM python:3.8.2-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY main.py main.py

ENTRYPOINT ["python", "/app/main.py"]
