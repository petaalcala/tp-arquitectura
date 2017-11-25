FROM python:2
WORKDIR /app/py
RUN pip install flask gunicorn
