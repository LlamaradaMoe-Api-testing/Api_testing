import requests
from assertpy.assertpy import assert_that
from config import URI, TOKEN, ID
from utils.request import Requests
from utils.print_helpers import pretty_print
import json


def test_delete():
    status_code = 1
    dict_response = 0
    payload = {}
    headers = {
        'Authorization': TOKEN,
        'Content-Type': 'application/json'
    }

    response = Requests(URI+ID, headers, payload)
    responses = response.get_responses(response.get_request('delete'))
    assert_that(responses[status_code]).is_equal_to(200)
    pretty_print(responses[dict_response])





