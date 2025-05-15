# FastAPI Sentiment Analyzer

## What It Does
A simple FastAPI microservice that analyzes the sentiment of input text using TextBlob.

## How to Run

### Locally
uvicorn app.main:app --reload

## Using docker
docker build -t sentiment-app .
docker run -p 8000:8000 --env-file .env sentiment-app
