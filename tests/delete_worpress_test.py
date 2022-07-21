import requests
from assertpy.assertpy import assert_that
from config import URI, TOKEN


def test_delete():
    payload = {}
    headers = {
        'Authorization': TOKEN,
        'Content-Type': 'application/json'
    }
    response = requests.delete(f"{URI}wp-json/wp/v2/pages/27", headers=headers, data=payload)
    print(response.json())
    assert_that(response.status_code).is_equal_to(200)

test_delete()
