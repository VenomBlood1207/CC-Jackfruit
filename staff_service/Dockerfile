FROM python:3.9-slim
ENV PYTHONPATH=/app
WORKDIR /app

# Copy shared module first
COPY shared /app/shared
COPY staff_service/requirements.txt .
COPY staff_service/app ./app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]