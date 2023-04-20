import requests
from jsonschema import validate

class StartPage:
    def __init__(self, url):
        self.url = url

    GET_START_PAGE = '/api'

    def get_start_page(self, json_schema):
        response = requests.get(f"{self.url}{self.GET_START_PAGE}")
        validate(instance=response.json(), schema=json_schema)
        return response



