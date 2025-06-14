FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY djangoBase djangoBase
WORKDIR /app/djangoBase
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
