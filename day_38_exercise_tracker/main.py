import requests
import datetime
import os

NUTRITION_API_ID = os.environ.get("API_ID")
NUTRITION_API_KEY = os.environ.get("API_KEY")
SHEETY_API_ENDPOINT = "https://api.sheety.co/4e0507483fbf4c25343bbb948e0af280/myWorkouts/workouts"


nut_headers_params = {
    "x-app-id": NUTRITION_API_ID,
    "x-app-key": NUTRITION_API_KEY,
    "x-remote-user-id": "0",
}
params = {
    "query": input("What exercises did you do today?: "),
    "gender": "male",
    "weight_kg": 87,
    "height_cm": 188,
    "age": 21,
}
# TODO: Get Exercise Stats with Natural Language Queries
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=params,
                         headers=nut_headers_params)
response.raise_for_status()
exercise_data = response.json()["exercises"]

# TODO: Saving Data into Google Sheets
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
headers = {
    "Authorization": AUTH_TOKEN
}

today_datetime = datetime.datetime.now()
today = today_datetime.strftime("%d/%m/%Y")
time = today_datetime.strftime("%X")
for exercise in exercise_data:
    exercise_name = exercise["name"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    exercise_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories,
        }
    }
    exercise_response = requests.post(url=SHEETY_API_ENDPOINT, json=exercise_params, headers=headers)
    exercise_response.raise_for_status()
