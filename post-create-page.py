import requests
import json
from assertpy.assertpy import assert_that
from config import BASE_URL
from config import AUTHORIZATION


def test_create_post():

    payload = json.dumps({
      "title": "Hello api testing!!",
      "status": "publish",
      "content": "Hello this is a test for api testing"
    })
    headers = {
      'Cookie': 'wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_6895bee2a097ffb11fc81c8ff67ee16d=freddy%7C1658411234%7Cs2vYRuBtZbsEZF2BS49YCAV58REZGkvM5DpUhvc4SpA%7Ca3c3055e7598dd9f74c56f3c713928533c13b73ca29784e62b0af419ad9ee160; wp-settings-time-1=1658245061; jenkins-timestamper-offset=14400000; _ga=GA1.1.268673621.1657157213; remember-me=ZnJlZGR5OjE2NTg3NzE4NDQyNzg6MDA3N2Y0NTdmMjVkZDQ0NjkxOTc4MGRiNmQ4MWU5MjAzOGFkMjM5ZjQ2MmNhODE0MGNkOGIzZGY4NjU1OTNjZg; wordpress_test_cookie=WP%20Cookie%20check',
      'X-WP-Nonce': '9da5ddda8c',
      'Authorization': 'Bearer '+ AUTHORIZATION,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", BASE_URL, headers=headers, data=payload)
    posts = response.json()
    print(posts)
    assert_that(response.status_code).is_equal_to(201)


test_create_post()
