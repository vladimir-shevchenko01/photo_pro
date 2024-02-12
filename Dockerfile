FROM python:3.10-slim

WORKDIR /app-photo-pro

ENV PYTHONUNBUFFERED=1 \
		PYTHONDOWNTWRITEBYTECODE=1

COPY requirements.txt /app-photo-pro/

RUN apt-get update && \
    apt-get clean && \
		pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
		apt-get remove -y gcc && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY . /app-photo-pro/
