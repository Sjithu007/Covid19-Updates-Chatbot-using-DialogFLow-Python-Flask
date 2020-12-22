import requests
import json
class Api:
    def __init__(self):
        pass

    def makeApiRequestForCounrty(self, country_name):
        url = "https://covid-193.p.rapidapi.com/statistics"
        querystring = {"country": country_name}
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "4964abb878msh3c88b019b427d21p15966ejsnb25364f1d1ea"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('response')[0]
        print(result.get('cases'))
        print("*" * 20)
        return result.get('cases') , result.get('deaths'),result.get('tests')

    def makeApiRequestForIndianStates(self, state_name):
        url = "https://covid19-data.p.rapidapi.com/india"
        querystring = {"state": state_name}
        headers = {
            'x-rapidapi-host': "covid19-data.p.rapidapi.com",
            'x-rapidapi-key': "4964abb878msh3c88b019b427d21p15966ejsnb25364f1d1ea"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        #result = js.get('list')
        return js

    def makeApiWorldwide(self):
        url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
        headers = {
            "x-rapidapi-host": "covid-19-statistics.p.rapidapi.com",
            "x-rapidapi-key": "4964abb878msh3c88b019b427d21p15966ejsnb25364f1d1ea"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('data')
        return result

