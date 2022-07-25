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

from utils.requests import Requests
import json
from assertpy.assertpy import assert_that
from config import BASE_URI
from config import AUTHORIZATION
from http import HTTPStatus


def test_create_post():

    url = f'{BASE_URI}/wp/v2/pages/'
    status_code = 1
    json_response = 2
    payload = json.dumps({
      "title": "Hello world!!!",
      "status": "publish",
      "content": ""
    })
    headers = {
      'Authorization': AUTHORIZATION,
      'Content-Type': 'application/json'
    }

    response = Requests(url, headers, payload)
    responses = response.get_responses(response.get_request('post'))
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)


test_create_post()
