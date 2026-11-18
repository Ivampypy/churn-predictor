FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir requirements.txt .

COPY . .

CMD ["uvicorn","api.mapi:app","--host","--port","8000"]


