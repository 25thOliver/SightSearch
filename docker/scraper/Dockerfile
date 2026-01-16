# docker/scraper/Dockerfile

FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV IMAGE_DIR=/app/images

COPY docker/scraper/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/

WORKDIR /app/src

CMD ["python", "scraper.py"]
