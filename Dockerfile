FROM python:3.11-slim
WORKDIR /app
COPY persistent_auditor.py functions.py inventory.txt .
CMD ["python", "persistent_auditor.py"]