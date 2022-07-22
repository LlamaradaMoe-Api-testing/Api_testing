#
# create-page.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

#import requests
from utils.requests import Requests
import json
from assertpy.assertpy import assert_that
from config import URI
from config import AUTHORIZATION
from config import NONCE
from config import COOKIE


def test_create_post():

    url = f'{URI}/wp-json/wp/v2/pages/'
    status_code = 1
    payload = json.dumps({
      "title": "Hello!!!",
      "status": "publish",
      "content": "Hello this is a test for api testing"
    })
    headers = {
      'Cookie': COOKIE,
      'X-WP-Nonce': NONCE,
      'Authorization': 'Bearer ' + AUTHORIZATION,
      'Content-Type': 'application/json'
    }

    #response = requests.request("POST", url, headers=headers, data=payload)
    response = Requests(url, headers, payload)
    responses = response.get_responses(response.get_request('post'))
    #posts = responses.json()
    print(responses)
    assert_that(responses[status_code]).is_equal_to(201)


#test_create_post()

