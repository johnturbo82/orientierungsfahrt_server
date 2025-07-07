FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 7900

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7900"]