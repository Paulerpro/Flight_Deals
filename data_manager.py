import requests
from decouple import config
# from requests.auth import HTTPBasicAuth

SHEETY_ENDPOINT = "https://api.sheety.co/a33c7ae87238dcbf63019b3e7ba9509b/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self._user = config("USERNAME")
        # self._password = config("PASSWORD")
        # self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        
        response = requests.get(SHEETY_ENDPOINT)

        # # pprint(response.json())

        self.destination_data = response.json()["prices"]

        return self.destination_data
 

    def update_city_iatacode(self, updated_data):
    
        for data in updated_data:
            url = f'{SHEETY_ENDPOINT}/{data["id"]}'

            body = {
                "price": {
                "iataCode": data["iataCode"]
                }
            }
            response = requests.put(url, json=body)
        return response.json()