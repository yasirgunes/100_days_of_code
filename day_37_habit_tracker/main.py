import requests
api_endpoint = "https://pixe.la/v1/users"
TOKEN = "sadecedeniyorum55"
USERNAME = "yasirgunes"
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_params = {
    "id": "graph1",
    "name": "coding",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}
from datetime import *
datetime = datetime.now().strftime("%Y%m%d")
add_pixel_params = {
    "date": datetime,
    "quantity": str(round(float(input("How much hours did you code today?: ")), 2)),
}
header_params = {
    "X-USER-TOKEN": TOKEN,
}
response = requests.post(url=f"{api_endpoint}/{USERNAME}/graphs/graph1", json=add_pixel_params, headers=header_params)
response.raise_for_status()
print(response.text)

