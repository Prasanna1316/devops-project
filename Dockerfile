FROM python:3.12-slim

WORKDIR /app

COPY app.py .

ENV APP_VERSION=1.0.0

EXPOSE 5000

CMD ["python", "app.py"]