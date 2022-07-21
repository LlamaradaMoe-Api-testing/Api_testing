from assertpy.assertpy import assert_that
from config import BASE_URI_PUT, AUTHORIZATION
import json
from utils.requests import Requests

def test_put_update():
    status_code = 1
    dict_response = 0
    id = '22'
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
    response = Requests(BASE_URI_PUT+id, headers, payload)
    responses = response.get_responses(response.get_request('put'))
    assert_that(responses[status_code]).is_equal_to(200)


test_put_update()
