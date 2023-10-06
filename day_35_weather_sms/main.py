import requests

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC39c771be2b4d63490849abb30a82554f'
auth_token = 'ad5673a75a51b38bfb488a1714b5fac7'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test",
                     from_='+447883290969',
                     to='+905063281393'
                 )

print(message.sid)


parameters = {
    "lat": 21.30,
    "lon": 118.39,
    "appid": "2208eefd3f59fbb87e9ce808e53252a5",
    "units": "metric"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
weather_list = data["list"]
bring_umbrella = False
counter = 0
for w_data in weather_list[:5]:
    weather_id = w_data["weather"][0]["id"]
    if weather_id < 700:
        bring_umbrella = True

if bring_umbrella:
    print("Bring Umbrella!")
else:
    print("No need for Umbrella!")

