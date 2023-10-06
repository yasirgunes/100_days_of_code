STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API = "b4234244672d4912a7fab6fecdb84e29"
STOCK_API = "MDFBHKP3E1MN0ZZY"
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.
import requests

stock_response = requests.get(f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={STOCK_API}")
stock_response.raise_for_status()
stock_data = stock_response.json()
days = [key for (key, value) in stock_data["Time Series (Daily)"].items()][:2]
yesterday = float(stock_data["Time Series (Daily)"][days[0]]["4. close"])
before_yesterday = float(stock_data["Time Series (Daily)"][days[1]]["4. close"])
diff_percentage = (yesterday - before_yesterday) / before_yesterday * 100
if diff_percentage >= 5:
    print("Get News")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator

news_response = requests.get(f"{NEWS_ENDPOINT}?q=tesla&qInTitle=tesla&from=2023-08-27&to=2023-08-28&sortBy=popularity&apiKey={NEWS_API}")
news_response.raise_for_status()
news = news_response.json()["articles"][:3]
for item in news:
    print(item["title"])

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
