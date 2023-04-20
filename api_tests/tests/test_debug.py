from api_tests.api_pages.main_api_page import StartPage
from api_tests.Schemas.start_page import valid_schema

URL = 'https://www.dnd5eapi.co'

def test_demo():
    response = StartPage(url=URL).get_start_page(json_schema=valid_schema)
    print(response.text)
    assert response.status_code==200