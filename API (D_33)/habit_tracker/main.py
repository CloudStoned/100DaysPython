import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "+Qaz123_WSX456"
USERNAME = "cloud-100-104"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers ={
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
# today = datetime(year=2024, month=7, day=28)
# print(today.strftime("%Y%m%d"))

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_habit = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many commits did you do today?: "),
}


# response = requests.post(url=pixel_post_endpoint, 
#                          json=post_habit, 
#                          headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_habit = {
    "quantity": "5"
}

# response = requests.put(url=update_endpoint,
#                         json=update_habit,
#                         headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)





