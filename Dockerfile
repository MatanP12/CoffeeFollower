FROM python:3.12.8-alpine3.21

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

ENTRYPOINT [ "fastapi","run","src"]
