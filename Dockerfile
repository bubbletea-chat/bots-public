# Root Dockerfile for all bots
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

ARG BOT_DIR
WORKDIR /app

# Copy that bot’s code into the image
COPY ${BOT_DIR}/ /app/

# Install dependencies
RUN python -m pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

EXPOSE 8080
CMD ["python", "bot.py"]
