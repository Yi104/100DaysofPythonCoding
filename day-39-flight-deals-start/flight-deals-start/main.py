#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests

sheet_endpoint="https://api.sheety.co/3185a2e6763470c783dfef81ef875fb3/flightDeals/flightInfo"
# bearer_headers ={
    #"Authorization":"skdiweufbvkl23rf",
#}

response = requests.post(url=sheet_endpoint)
result=response.json
print(response.text)
print(result)