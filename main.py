import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

user_params = {
    "token": TOKEN,
    "username": os.getenv("USERNAME"),
    "agreeTermsOfService": os.getenv("AGREE"),
    "notMinor": os.getenv("NMINOR"),
}

graph_params = {
    "id": os.getenv("IDG"),
    "name": os.getenv("NM"),
    "unit": os.getenv("UNT"),
    "type": os.getenv("TYP"),
    "color": os.getenv("CLR"),
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

now = str(datetime.datetime.now()).split()[0].replace("-", "")

pixel_params = {
    "date": now,
    "quantity": input("How much time did you study today?\n"),
}

#response = requests.post(url="https://pixe.la/v1/users", json=user_params)
#response = requests.post(url=f"https://pixe.la//v1/users/{user_params['username']}/graphs", json=graph_params, headers=headers)
response = requests.post(url=f"https://pixe.la//v1/users/{user_params['username']}/graphs/{graph_params['id']}",
                         json=pixel_params, headers=headers)
print(response.text)