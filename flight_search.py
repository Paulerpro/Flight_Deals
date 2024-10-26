import requests
from decouple import config
import pprint

AMADEUS_ENPOINT = "https://test.api.amadeus.com/v1"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = config("API_KEY")
        self._api_secret = config("SECRET_KEY")
        self._access_token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }

        response = requests.post(f'{AMADEUS_ENPOINT}/security/oauth2/token', headers=headers, data=data)

        print(response.json())

        self._access_token = response.json()["access_token"]

        return self._access_token
    
    def get_locations_cities(self, updated_data):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }

        for data in updated_data:
            city = data["city"]
            response = requests.get(url=f'{AMADEUS_ENPOINT}/reference-data/countryCode/cities?keyword={city}', data=data)

            pprint(response.json())
            
    
    def get_IATA_codes(sheet_data: list):
        for data in sheet_data:
            if not data["iataCode"]:
                data["iataCode"] = "TESTING"
        return sheet_data