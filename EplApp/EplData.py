import requests
import json
from EplApp import keys

class EplData:
    def getData(self):
        keyClass = keys.keyHolder()
        head = {'X-Auth-Token': keyClass.getKeys()}
        request = requests.get("https://api.football-data.org/v2/teams/86/matches?", headers=head)
        return request.content




def main():
    data = EplData()
    print(data.getData())

if __name__=="__main__":
    main()