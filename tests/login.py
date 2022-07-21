import requests

from assertpy.assertpy import assert_that, soft_assertions
from config import URI, USER, PASS
from utils.print_helpers import pretty_print


def test_login():
    url = f'{URI}/wp-json/api/v1/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = f"username={USER}&password={PASS}"
    response = requests.post(url, headers=headers, data=payload)
    pretty_print(response.json())
    assert_that(response.status_code).is_equal_to(200)


test_login()
