FROM python:3.11-slim

WORKDIR /app

COPY auditor.py .

cmd ["python", "auditor.py"]