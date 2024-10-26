#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
flight_search = FlightSearch()

# destination_data = data_manager.get_destination_data()

# updated_data = FlightSearch.get_IATA_codes(sheet_data=destination_data)


# Test data to manage API Call limit
updated_data = [{'city': 'Paris', 'iataCode': 'TESTING', 'lowestPrice': 54, 'id': 2}, {'city': 'Frankfurt', 'iataCode': 'TESTING', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TESTING', 'lowestPrice': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': 'TESTING', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'TESTING', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'TESTING', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'TESTING', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'TESTING', 'lowestPrice': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': 'TESTING', 'lowestPrice': 378, 'id': 10}]

flight_search.get_locations_cities(updated_data)

# data_manager.update_city_iatacode(updated_data)