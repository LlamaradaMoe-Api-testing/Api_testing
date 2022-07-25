from assertpy.assertpy import assert_that
from utils.config import BASE_URI, AUTHORIZATION
from utils.requests import Requests
from helpers.print_helpers import pretty_print


def test_delete():
    status_code = 1
    dict_response = 0
    id = "10"
    payload = {}
    headers = {
        'Authorization': AUTHORIZATION,
        'Content-Type': 'application/json'
    }

    response = Requests(f'{BASE_URI}/wp/v2/pages/{id}', headers, payload)
    responses = response.get_responses(response.get_request('delete'))
    assert_that(responses[status_code]).is_equal_to(200)
    pretty_print(responses[dict_response])
test_delete()