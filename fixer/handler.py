import requests
import json

base_address = "http://data.fixer.io/api/latest?access_key="


def get_rates(api_key):
    """
    send a get request to fixer.io's Api and get rates and transform it to dict and return it
    :return: dict of get request's response
    """
    response = requests.get(base_address + api_key)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None
