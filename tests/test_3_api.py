from api.questions_api import api
from utils.assertions import Assert
from http import HTTPStatus


def test_3_api():
    email = "eve.holt@reqres.in"
    password = "12345"
    response = api.createpassword(email, password)

    assert response.status_code == HTTPStatus.OK
    Assert.validate_schema(response.json())


def test_3_api1():
    email = "eve.holt@reqres.in"
    response = api.createuncorrect(email)
    response_body = response.json()
    example = {
                "error": "Missing password"
                }

    assert response.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(response.json())
    assert response_body == example
