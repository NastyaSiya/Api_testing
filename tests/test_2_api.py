from http import HTTPStatus
from api.questions_api import api
from utils.assertions import Assert


def test_2_api():
    resp = api.list_users()

    assert resp.status_code == HTTPStatus.OK
    Assert.validate_schema(resp.json())


def test_3_api():
    resp = api.single_user_not_found()

    assert resp.status_code == HTTPStatus.NOT_FOUND
    Assert.validate_schema(resp.json())


def test_4_api():
    resp = api.single_user()
    resp_body = resp.json()

    assert resp.status_code == HTTPStatus.OK
    Assert.validate_schema(resp_body)

    assert resp_body["data"]["first_name"] == 'Janet'
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert example == resp_body


def test_create():
    name = 'Alex'
    job = 'Worker'
    resp = api.create(name, job)

    assert resp.status_code == HTTPStatus.CREATED
    assert resp.json()['name'] == name
    assert resp.json()['job'] == job
    assert api.delete_user(resp.json()['id']).status_code == HTTPStatus.NO_CONTENT
