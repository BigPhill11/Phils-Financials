import os
import requests
import openai
import json

MARKETSTACK_KEY = os.environ.get("MARKETSTACK_KEY")
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

def fetch_market_data():
    url = f"http://api.marketstack.com/v1/eod?access_key={MARKETSTACK_KEY}&symbols=^GSPC,^IXIC,BTCUSD,ETHUSD"
    response = requests.get(url)
    data = response.json()
    if 'data' not in data:
        return "Market data unavailable"
    try:
        tickers = data['data']
        return f"S&P 500: {tickers[0]['close']}, Nasdaq: {tickers[1]['close']}, BTC: ${tickers[2]['close']}, ETH: ${tickers[3]['close']}"
    except:
        return "Market data could not be parsed."

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?category=business&apiKey={NEWSAPI_KEY}&language=en"
    response = requests.get(url)
    headlines = []
    if 'articles' in response.json():
        for article in response.json()['articles'][:3]:
            headlines.append({"title": article['title'], "summary": article['description']})
    return headlines

def generate_gpt_summary(text):
    openai.api_key = OPENAI_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a financial analyst writing concise interpretations of market and economic events."},
                {"role": "user", "content": f"Summarize and analyze this: {text}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return "GPT summary failed"

def write_data_file(market_summary, headlines, analysis):
    output = {
        "marketRecap": {
            "summary": market_summary,
            "gptTake": analysis
        },
        "headlines": headlines,
        "events": {
            "today": ["Placeholder Event 1", "Placeholder Event 2"],
            "gptTake": "Events are placeholders for now."
        },
        "deals": {
            "today": ["Placeholder Deal 1", "Placeholder Deal 2"],
            "gptTake": "Deals are placeholders for now."
        }
    }

    with open("data.js", "w") as f:
        f.write("const data = ")
        json.dump(output, f, indent=2)

# Run the update
market_summary = fetch_market_data()
news = fetch_news()
headline_text = " ".join([item['title'] for item in news])
analysis = generate_gpt_summary(headline_text)
write_data_file(market_summary, news, analysis)
