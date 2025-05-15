from fastapi import FastAPI
from app.sentiment import analyze_sentiment
from app.models import SentimentRequest, SentimentResponse

app = FastAPI()
# making changes to the

@app.post("/analyze", response_model=SentimentResponse)
def analyze(request: SentimentRequest):
    sentiment = analyze_sentiment(request.text)
    return SentimentResponse(sentiment=sentiment)
