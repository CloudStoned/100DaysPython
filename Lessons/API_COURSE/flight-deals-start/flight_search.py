from dotenv import load_dotenv
import os
import requests

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["FLIGHT_API_KEY"]
        self._api_secret = os.environ["FLIGHT_API_SECRET"]
        self._token = self.get_new_token()

    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
    
        response = requests.post(TOKEN_ENDPOINT, headers=header, data=body)
        # print(response.text)
        # print(f"Your token is {response.json()['access_token']}")
        # print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    
    def get_destination_code(self, city_name):
        # print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )
        
        print(f"Status code {response.status_code}... Getting IATACODE for {city_name}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code


    # def get_iata_code(self, city_name):
    #     return "TEST101"