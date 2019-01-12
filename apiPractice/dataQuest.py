import requests
import json
class dataQuest:
    def getIssLocation(self):
        # Set up the parameters we want to pass to the API.
        # This is the latitude and longitude of New York City.
        parameters = {"lat": 40.71, "lon": -74}
        # Make a get request to get the latest position of the international space station from the opennotify api.
        response = requests.get("http://api.open-notify.org/iss-now.json", parameters)
        location = json.loads(response.content)
        # Print the status code of the response.
        return location
    def whosInSpace(self):
        # Get the response from the API endpoint.
        response = requests.get("http://api.open-notify.org/astros.json")
        data = response.json()
        # 9 people are currently in space.
        return (data)