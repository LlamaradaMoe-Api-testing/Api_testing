#
# create_page.py Copyright (c) 2022 Jalasoft.
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
from utils.print_helpers import pretty_print
from tests.get_token import test_get_token


def test_create_post():
    status_code = 1
    dict_response = 0
    json_response = 2
    payload = json.dumps({
      "title": "Hello world!!!",
      "status": "publish",
      "content": ""
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)


def test_validate_valid_token():
    test_get_token()
    status_code = 1
    dict_response = 0
    json_response = 2
    payload = json.dumps({
        "title": "Valid token!!!",
        "status": "publish",
        "content": ""
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)


def test_valid_content():
    status_code = 1
    dict_response = 0
    json_response = 2
    payload = json.dumps({
        "title": "Valid token!!!",
        "status": "publish",
        "content": "Correct content"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)


def test_valid_status_publish():
    status_code = 1
    dict_response = 0
    json_response = 2
    payload = json.dumps({
        "title": "Status publish!",
        "status": "publish",
        "content": "Correct content"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)


def test_valid_status_draft():
    status_code = 1
    dict_response = 0
    json_response = 2
    payload = json.dumps({
        "title": "Status draft",
        "status": "draft",
        "content": "Correct content"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)


def test_valid_status_private():
    status_code = 1
    dict_response = 0
    json_response = 2
    payload = json.dumps({
        "title": "status private",
        "status": "private",
        "content": "Correct content"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
