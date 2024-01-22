import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_APIkey="89GXQGYAOLE9293I"
NEWS_APIkey = "485ce03083e145579dd09784ff596943"

account_sid="AC50ddaaa4f514f0635758d4abd77296db"
auth_token="f769a7f5ce7a4216447a7c7a427bf1ec"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#1 list comprehensions on Python dictionaries.[new_value for (key, value) in dictionary.items()]
#2 Get the day before yesterday's closing stock price
# 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# 5. - If TODO4 percentage is greater than 5 then print("Get News").

STOCK_PARAMS={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_APIkey
}

response=requests.get(STOCK_ENDPOINT,params=STOCK_PARAMS)
response.raise_for_status()
stock_data=response.json()["Time Series (Daily)"]
data_list =[value for (key,value) in stock_data.items()]
yesterday_close= float(data_list[0]["4. close"])
Pretwo_day_close= float(data_list[1]["4. close"])
day_difference =yesterday_close - Pretwo_day_close
percent_difference= round(abs(day_difference)/ Pretwo_day_close *100)

if day_difference >0:
    up_down ="📈📈"
else:
    up_down="📉📉"

## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation



NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_APIkey,
}

if percent_difference >0:
    response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    response.raise_for_status()
    news_data = response.json()["articles"]
    three_articles = news_data[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percent_difference}\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in
                          three_articles]

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="formatted_articles",
        from_="__ your twilio number__",
        to="__your verified number at twilio__ "
    )
    print(message.status)

else:
    print("no big deal")




    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

print(formatted_articles)

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

