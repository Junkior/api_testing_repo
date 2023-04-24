from api_tests.api_pages.ability_scores import AbilityScores
from api_tests.Schemas.ability_scores_schemas import ability_scores_schema_positive


URL = 'https://www.dnd5eapi.co'


class TestEndpoints:

    def test_ability_scores_page_positive(self):
        response = AbilityScores(url=URL).get_ability_scores(json_schema=ability_scores_schema_positive)
        response.raise_for_status()
        body = response.json()
        list_of_indexes = [item["index"] for item in body["results"]]
        assert list_of_indexes == ['cha', 'con', 'dex', 'int', 'str', 'wis']
        assert response.status_code == 200

