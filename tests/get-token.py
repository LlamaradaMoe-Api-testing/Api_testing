from assertpy.assertpy import assert_that
import json
from utils.requests import Requests
from config import USERNAME, PASSWORD, BASE_URI, AUTHORIZATION


def test_get_token():
    status_code = 1
    dict_response = 0
    payload = {'username': USERNAME, 'password': PASSWORD}
    headers = {}
    response = Requests(BASE_URI, headers, payload)
    responses = response.get_responses(response.get_request('post'))
    assert_that(responses[status_code]).is_equal_to(200)
    assert_that(responses[dict_response]['jwt_token']).is_not_empty()
    json_response = json.dumps(responses[dict_response], indent=2)
    print(json_response)
    filename = "../config.py"
    text = open(filename).read()
    open(filename, "w+").write(text.replace(AUTHORIZATION, 'Bearer '+responses[dict_response]['jwt_token']))


test_get_token()
