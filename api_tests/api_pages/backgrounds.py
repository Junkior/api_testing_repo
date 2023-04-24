from api_tests.request_lib import Client
from jsonschema import validate



class Backgrounds:
    def __init__(self, url):
        self.url = url
        self.client = Client

    BACKGROUNDS = '/api/backgrounds'


    def get_backgrounds(self, json_schema):
        """
        GET backgrounds information
        :param json_schema: valid json schema
        :return: response of request
        """
        response = self.client.custom_request("GET", f"{self.url}{self.BACKGROUNDS}")
        validate(instance=response.json(), schema=json_schema)
        return response



    def get_backgrounds_negative(self, json_schema, additional_url):
        """
        GET ability-scores with negative scenarios as incorrect url
        :param json_schema: valid error json schema
        :param additional_url: additional url for negative scenarios
        :return: response of request
        """
        response = self.client.custom_request("GET", f"{self.url}{additional_url}")
        validate(instance=response.json(), schema=json_schema)
        return response