from api_tests.request_lib import Client
from jsonschema import validate


class Aligments:
    def __int__(self, url):
        self.url = url
        self.client = Client

    ALIGMENTS = '/api/aligments'

    def get_aligments(self, json_schema):
        """
        GET aligments information
        :param json_schema: valid json schema
        :return: response of request
        """
        response = self.client.custom_request("GET", f"{self.url}{self.ALIGMENTS}")
        validate(instance=response.json(), schema=json_schema)
        return response

    def get_aligments_negative(self, json_schema, additional_url):
        """
        GET ability-scores with negative scenarios as incorrect url
        :param json_schema: valid error json schema
        :param additional_url: additional url for negative scenarios
        :return: response of request
        """
        response = self.client.custom_request("GET", f"{self.url}{additional_url}")
        validate(instance=response.json(), schema=json_schema)
        return response
