import requests
import datetime
USERNAME = "maheshvardhan"
TOKEN = "rtyh789hbnm890"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph"
user_params = {
    "token": "rtyh789hbnm890",
    "username": "maheshvardhan",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": "graph",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai"
}
today = datetime.date.today()
formatted_date = today.strftime('%Y%m%d')
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
post_endpoint = f"{pixela_endpoint}/maheshvardhan/graphs/{GRAPH_ID}"
pixel_data = {
    "date": formatted_date,
    "quantity": "90",
}
# post_data = requests.post(url=post_endpoint, json=pixel_data, headers=headers)
# print(post_data.text)
put_endpoint = f"{pixela_endpoint}/maheshvardhan/graphs/{GRAPH_ID}/{formatted_date}"
put_data = {
    "quantity": "90",
}
# put_data = requests.put(url=put_endpoint, json=put_data, headers =headers)
# print(put_data.text)
delete_endpoint = f"{pixela_endpoint}/maheshvardhan/graphs/{GRAPH_ID}/{formatted_date}"
# delete_response = requests.delete(url=delete_endpoint, headers = headers)
# print(delete_response.text)
