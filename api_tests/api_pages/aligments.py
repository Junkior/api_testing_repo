from api_tests.request_lib import Client
from jsonschema import validate


class Aligments:
    def __int__(self, url):
        self.url = url
        self.client = Client

    ALIGMENTS = '/api/aligments'

    def get_aligments(self, json_schema):
        response = self.client.custom_request("GET", f"{self.url}{self.ALIGMENTS}")
        validate(instance=response.json(), schema=json_schema)
        return response