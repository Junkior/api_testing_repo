from api_tests.request_lib import Client
from jsonschema import validate

class StartPage:
    def __init__(self, url):
        self.url = url
        self.client = Client

    START_PAGE = '/api/'

    def get_start_page(self, json_schema):
        """
        Making a request to the API's base URL returns an object containing available endpoints.
        :param json_schema: json schema for validate response body json
        :return: response of request
        """
        response = self.client.custom_request("GET", f"{self.url}{self.START_PAGE}")
        validate(instance=response.json(), schema=json_schema)
        return response



