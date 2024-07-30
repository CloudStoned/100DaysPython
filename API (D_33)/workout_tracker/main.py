import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["sheet_endpoint"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

params = {
    "query": exercise_text,
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
response.raise_for_status()
data = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_input= {
    "workout": 
            {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_input)
    
    if sheet_response.status_code == 200:
        print("Data successfully posted to the sheet:")
        print(sheet_response.json())
    else:
        error_response = sheet_response.json()
        if 'errors' in error_response:
            print("Error:", error_response['errors'][0]['detail'])
        else:
            print(f"Request failed with status code {sheet_response.status_code}")
            print(sheet_response.text)
