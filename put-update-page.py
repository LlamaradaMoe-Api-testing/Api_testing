import requests
from assertpy.assertpy import assert_that
from config import BASE_URI_PUT, AUTHORIZATION
import json


def test_put_update():
    id = '18'
    payload = json.dumps({
        "id": id,
        "title": "Hello world17!!",
        "status": "private",
        "content": ""
    })
    headers = {
        'Authorization': AUTHORIZATION,
        'Content-Type': 'application/json'
    }
    response = requests.post(BASE_URI_PUT+id, headers=headers, data=payload)
    posts = response.json()
    assert_that(response.status_code).is_equal_to(201)


test_put_update()
