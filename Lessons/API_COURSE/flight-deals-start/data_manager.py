from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import os
import requests
import json

load_dotenv()

SHEET_PUT = os.environ["SHEET_PUT"]
SHEET_GET = os.environ["SHEET_GET"]
SHEET_UNAME = os.environ["SHEET_UNAME"]
SHEET_PASS = os.environ["SHEET_PASS"]

class DataManager:
    def __init__(self) -> None:
        self._authorization = HTTPBasicAuth(SHEET_UNAME, SHEET_PASS)
        self.destination_data = {}

    # def get_data(self):
    #     _authorization = HTTPBasicAuth(SHEET_UNAME, SHEET_PASS)
    #     url = SHEET_GET
    #     response = requests.get(url, auth=_authorization)
    #     if response.status_code == 200:
    #         json_data = response.json()
    #         prices = json_data.get('prices', [])
    #         sheet_data = prices
            
    #         return sheet_data
            
    #     else:
    #         return f"Faled to fetch data: {response.status_code}"

    
    def get_destination_data(self):
        response = requests.get(url=SHEET_GET, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_row(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{SHEET_PUT}/{city["id"]}", 
                                    json=new_data, 
                                    auth=self._authorization)
            print(response.text)

    # def update_destination_codes(self):
    #     for city in self.destination_data:
    #         new_data = {
    #             "price": {
    #                 "iataCode": city["iataCode"]
    #             }
    #         }
    #         response = requests.put(
    #             url=f"{SHEET_PUT}/{city['id']}",
    #             json=new_data,
    #             auth=self._authorization
    #         )
    #         print(response.text)
        