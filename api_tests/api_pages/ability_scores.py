from api_tests.request_lib import Client
from jsonschema import validate


class AbilityScores:
    def __init__(self, url):
        self.url = url
        self.client = Client

    ABILITY_SCORES = '/api/ability-scores'

    def get_ability_scores(self, json_schema):
        """
        Get list of all available resources for an ability-scores.
        :param json_schema: schema for validate
        :return: response of request
        """
        response = self.client.custom_request("GET", f"{self.url}{self.ABILITY_SCORES}")
        validate(instance=response.json(), schema=json_schema)
        return response
