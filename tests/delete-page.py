#
# delete-page.py Copyright (c) 2022 Jalasoft.
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

from assertpy.assertpy import assert_that
from config import BASE_URI, AUTHORIZATION
from utils.requests import Requests
from http import HTTPStatus


def test_delete():
    status_code = 1
    dict_response = 0
    json_response = 2
    id = "40"
    payload = {}
    headers = {
        'Authorization': AUTHORIZATION,
        'Content-Type': 'application/json'
    }

    response = Requests(f'{BASE_URI}/wp/v2/pages/{id}', headers, payload)
    responses = response.get_responses(response.get_request('delete'))
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    print(responses[json_response])

    
test_delete()
