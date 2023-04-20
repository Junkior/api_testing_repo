import requests.exceptions

from api_tests.api_pages.main_api_page import StartPage
from api_tests.Schemas.start_page import valid_schema

URL = 'https://www.dnd5eapi.co'

def test_start_api_page():
    try:
        response = StartPage(url=URL).get_start_page(json_schema=valid_schema)
        response.raise_for_status()
        body = response.json()
    except requests.exceptions.HTTPError as err:
        print("HTTP error:", err)
    except ValueError as err:
        print("Json parse error:", err)

    else:
        assert response.status_code == 200
        assert body["rules"] == "/api/rules"
