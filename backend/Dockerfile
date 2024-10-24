FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y make && apt-get clean

# Cambiado de backend/requirements.txt a solo requirements.txt
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Cambiado de COPY backend /app a COPY . /app
COPY . /app