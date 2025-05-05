# Upload Service

Этот проект позволяет сохранять фотографии в MinIO. Для запуска сервиса используется Docker и Docker Compose.

## Шаги для начала работы

### 1. Создание `.env` файла
Сначала создайте файл `.env`, скопировав его из `example.env`:

```bash
cp example.env .env
```

### 2. Создание docker network  файла

```bash
docker network create upload_service_network
```
### 3. Запуск Docker контейнеров

```bash
docker-compose up --build
```
Это соберет и запустит все сервисы, определенные в docker-compose.yml.

### 4. Доступ к API

После того как контейнеры запустятся, откройте документацию API по следующему адресу:

http://0.0.0.0:8088/docs
