FROM python:3.11-slim

WORKDIR /app

COPY persistent_auditor.py .

cmd ["python", "persistent_auditor.py"]