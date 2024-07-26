import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.getenv('OWM_API_KEY')
account_sid = os.getenv('TWILIO_ACCNT_SSID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

weather_params = {
    "lat": 12.879721,
    "lon": 121.774017,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

# print(data["list"][0]["weather"][0]["id"])

# for i in data["list"]:
#     for j in i["weather"]:
#         weather_code = j["id"]
#         if weather_code < 700:
#             print(f"Bring an Umbrella. Code: {weather_code}")
#         else:
#             print(weather_code)

will_rain = False

for i in data["list"]:
    weather_code = i["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+19383003497',
    body=f"Bring an Umbrella. Code: {weather_code}",
    to='+639928378868'
    )

    print(message.status)

    




