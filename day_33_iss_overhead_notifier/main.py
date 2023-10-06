import requests
from datetime import datetime

MY_LAT = 41.205379
MY_LONG = 36.689064

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # With this we can raise exception if there is a problem instead of raising it manually

data = response.json()
latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])
coordinates = (latitude, longitude)


parameters = {
    "lat": 41.205379,
    "lng": 36.689064,
    "formatted": 0,
}
sunset_api = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sunset_api.raise_for_status()
data = sunset_api.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split("+")[0].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split("+")[0].split(":")[0])
current_time = int(datetime.now().hour)

is_close_enough = abs(latitude - MY_LAT) <= 5 and abs(longitude - MY_LONG) <= 5  # if the iss is close to my coordinates
is_dark = not (sunrise <= current_time <= sunset)


