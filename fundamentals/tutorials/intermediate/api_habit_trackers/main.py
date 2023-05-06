import requests

base_url = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = "aaninwezi"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}


def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=base_url, json=user_params)
    response.raise_for_status()
    print(response.text)


def create_graph():
    graph_endpoint = f"{base_url}/{USERNAME}/graphs"
    graph_config = {
        "id": "graph1",
        "name": "Cycling graph",
        "unit": "km",
        "type": "float",
        "color": "sora"
    }
    response = requests.post(
        graph_endpoint, json=graph_config, headers=HEADERS)
    response.raise_for_status()
    print(response.text)


def add_a_pixel():
    pixel_endpoint = f"{base_url}/{USERNAME}/graphs/graph1"
    pixel_config = {
        "date": "20230223",
        "quantity": "5.74"
    }
    response = requests.post(
        pixel_endpoint, json=pixel_config, headers=HEADERS)
    response.raise_for_status()
    print(response.text)


def update_a_pixel():
    pixel_endpoint = f"{base_url}/{USERNAME}/graphs/graph1/20230224"
    pixel_config = {
        "quantity": "50.74"
    }
    response = requests.put(
        pixel_endpoint, json=pixel_config, headers=HEADERS)
    response.raise_for_status()
    print(response.text)


def delete_a_pixel():
    pixel_endpoint = f"{base_url}/{USERNAME}/graphs/graph1/20230224"

    response = requests.delete(
        pixel_endpoint, headers=HEADERS)
    response.raise_for_status()
    print(response.text)

delete_a_pixel()