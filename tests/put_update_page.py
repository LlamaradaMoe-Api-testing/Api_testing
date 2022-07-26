#
# put_update_page.py Copyright (c) 2022 Jalasoft.
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
import json
from http import HTTPStatus
from helpers.crud import CrudPage


def test_put_update():
    status_code = 1
    dict_response = 0
    json_response = 2
    id = '22'
    payload = json.dumps({
        "id": id,
        "title": "Hello world17!!",
        "status": "private",
        "content": ""
    })
    responses = CrudPage().put(id, payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    print(responses[json_response])



