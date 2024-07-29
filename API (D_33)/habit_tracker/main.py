import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "+Qaz123_WSX456"
USERNAME = "cloud-100-104"
GRAPH_ID = "graph1"
HEADERS = { "X-USER-TOKEN": TOKEN}

def create_account(TOKEN,USERNAME):
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=pixela_endpoint, json=user_params)

    return response

# print(create_account(TOKEN,USERNAME))

def create_graph(HEADERS):
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Coding Graph",
        "unit": "commit",
        "type": "int",
        "color": "shibafu"
    }
    response = requests.post(url=graph_endpoint,json=graph_config, headers=HEADERS)

    return response

# print(create_graph(HEADERS))

def post_pixel(HEADERS):
    today = datetime.now()
    # today = datetime(year=2024, month=7, day=28)
    # print(today.strftime("%Y%m%d"))

    pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    post_habit = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("How many commits did you do today?: "),
    }

    response = requests.post(url=pixel_post_endpoint, 
                            json=post_habit, 
                            headers=HEADERS)

    return response

print(post_pixel(HEADERS))

def update_pixel(HEADERS):
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    update_habit = {
        "quantity": "5"
    }

    response = requests.put(url=update_endpoint,
                            json=update_habit,
                            headers=HEADERS)
    
print(update_pixel(HEADERS))

def delete_pixel(HEADERS):
    today = datetime.now()
    # today = datetime(year=2024, month=7, day=28)
    # print(today.strftime("%Y%m%d"))

    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
    response = requests.delete(url=delete_endpoint,headers=HEADERS)

    return response

print(delete_pixel(HEADERS))




