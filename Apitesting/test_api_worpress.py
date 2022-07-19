import requests
from assertpy.assertpy import assert_that
from config import URI


def test_delete():
    payload = {}
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsIm5hbWUiOiJhYmFycmllbnRvIiwiaWF0IjoxNjU4MjY3MDIyLCJleHAiOjE4MTU5NDcwMjJ9.U_snuHNpjj5eBf1OrulOxwNLhgiZHjNFkfaOV72wI4Y',
        'Content-Type': 'application/json'
    }
    response = requests.delete(URI, headers=headers, data=payload)
    print(response.json())
    assert_that(response.status_code).is_equal_to(200)

test_delete()