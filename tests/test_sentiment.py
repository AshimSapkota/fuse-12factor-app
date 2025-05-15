from app.sentiment import analyze_sentiment

def test_positive():
    assert analyze_sentiment("I love this!") == "positive"

def test_negative():
    assert analyze_sentiment("I hate this!") == "negative"

def test_neutral():
    assert analyze_sentiment("It is a pen.") == "neutral"
