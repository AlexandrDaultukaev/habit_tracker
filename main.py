import requests
import os
from dotenv import load_dotenv

load_dotenv()


user_params = {
    "token": os.getenv("TOKEN"),
    "username": os.getenv("USERNAME"),
    "agree": os.getenv("AGREE"),
    "nminor": os.getenv("NMINOR"),
}

print(user_params)

response = requests.post(url="https://pixe.la/v1/users", json=user_params)
print(response.text)