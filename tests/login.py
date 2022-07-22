import requests

from assertpy.assertpy import assert_that, soft_assertions
from config import URI, USER, PASS
from utils.print_helpers import pretty_print



def test_login():
    url = f'{URI}/api/v1/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = f"username={USER}&password={PASS}"
    response = requests.post(url, headers=headers, data=payload)
    assert_that(response.status_code).is_equal_to(200)
    jwt_token = response.json()['jwt_token']
    token_type = response.json()['token_type']
    return token_type + " " + jwt_token

