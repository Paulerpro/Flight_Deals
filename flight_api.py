import requests
from decouple import config

url = "https://test.api.amadeus.com/v1/security/oauth2/token"

client_id =config("client_id")
client_secret =config("client_secret")

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}


response = requests.post(url, headers=headers, data=data)

print(response.json())

