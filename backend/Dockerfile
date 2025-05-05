# 1. Сборка зависимостей в отдельном контейнере
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update --fix-missing && \
    apt-get install -y gcc libpq-dev ffmpeg libsm6 libxext6 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt

# 2. Финальный минимальный образ
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY .. .


EXPOSE 8008
