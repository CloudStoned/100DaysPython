from dotenv import load_dotenv
import os
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
import time

load_dotenv()

SHEET_GET = os.environ["SHEET_GET"]
SHEET_UNAME = os.environ["SHEET_UNAME"]
SHEET_PASS = os.environ["SHEET_PASS"]



data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()


# for item in sheet_data:
#     if not item.get('iataCode'):
#         row_id = item['id']
#         city_name = item['city']
#         iata_code = flight_search.get_iata_code(city_name)
#         updated_data = data_manager.update_row(row_id, iata_code)
#         item['iataCode'] = iata_code

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])

        # slowing down requests to avoid rate limit
        time.sleep(2)

pprint(f"sheet_data:\n {sheet_data}")
    
data_manager.destination_data = sheet_data
data_manager.update_row()


