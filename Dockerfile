FROM python:3.8.2-slim-buster

ENV PYTHONUNBUFFERED=1

COPY main.py /main.py

ENTRYPOINT ["python", "/main.py"]
