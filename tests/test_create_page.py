#
# test_create_page.py Copyright (c) 2022 Jalasoft.
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
import allure
from assertpy.assertpy import assert_that
import json
from http import HTTPStatus
from helpers.crud import CrudPage
from helpers.get_token import get_token
from jsonschema import validate
from utils.print_helpers import pretty_print
from utils.dotenv_manager import dotenv_loader
import os
import pytest


dotenv_loader()
status_code: int = int(os.environ.get('status_code'))
json_response: int = int(os.environ.get('json_response'))
dict_response: int = int(os.environ.get('dict_response'))


# Happy path
@pytest.mark.acceptance
@allure.suite("acceptance")
@allure.title("Test for create a page")
def test_create_post():
    get_token()
    payload = json.dumps({
      "title": "Validate status response!",
      "status": "publish",
      "content": "test for validate the status response"
    })
    responses = CrudPage().post(payload)
    pretty_print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    return responses[dict_response]['id']


@pytest.mark.acceptance
@allure.suite("acceptance")
@allure.title("Test for create a page with a valid token")
def test_validate_valid_token():
    get_token()
    payload = json.dumps({
        "title": "Valid token!",
        "status": "publish",
        "content": "test with a valid token"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)


@pytest.mark.acceptance
@allure.suite("acceptance")
@allure.title("Test for create a page with a valid title")
def test_valid_title():
    get_token()
    title = "Valid title"
    payload = json.dumps({
        "title": title,
        "status": "publish",
        "content": "Test for validate title"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    response_title = response_content['title']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['title']).is_not_empty()
    assert_that(response_title['raw']).is_equal_to(title)


@pytest.mark.acceptance
@allure.suite("acceptance")
@allure.title("Test for create a page with a valid content")
def test_valid_content():
    get_token()
    content = "test for validate the content"
    payload = json.dumps({
        "title": "Validate the content",
        "status": "publish",
        "content": content
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    resp_content = response_content['content']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['content']).is_not_empty()
    assert_that(resp_content['raw']).is_equal_to(content)


@pytest.mark.acceptance
@allure.suite("acceptance")
@allure.title("Test for create a page with status publish")
def test_valid_status_publish():
    get_token()
    status = "publish"
    payload = json.dumps({
        "title": "Status publish!",
        "status": status,
        "content": "test for validate the publish status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['status']).is_equal_to(status)


@pytest.mark.acceptance
@allure.suite("acceptance")
@allure.title("Test for create a page with status draft")
def test_valid_status_draft():
    get_token()
    status = "draft"
    payload = json.dumps({
        "title": "Status draft",
        "status": status,
        "content": "test for validate the draft status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['status']).is_equal_to(status)


@pytest.mark.acceptance
@allure.suite("acceptance")
@allure.title("Test for create a page with status private")
def test_valid_status_private():
    get_token()
    status = "private"
    payload = json.dumps({
        "title": "status private",
        "status": status,
        "content": "Test for validate the private status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['status']).is_equal_to(status)


@pytest.mark.endToend
@allure.suite("endToend")
@allure.title("Test for validate the schema response at create a page")
def test_validate_schema():
    file = open('./helpers/schema-create.json', "r")
    schema = json.loads(file.read())
    payload = json.dumps({
        "title": "Schema test",
        "status": "publish",
        "content": "test for validate the schema response"
    })
    responses = CrudPage().post(payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    schema_test = json.loads(responses[json_response])
    validate(instance=schema_test, schema=schema)


# Negative tests
@pytest.mark.regression
@allure.suite("regression")
@allure.title("Test for create a page without a title")
def test_valid_no_title():
    get_token()
    payload = json.dumps({
        "title": "",
        "status": "publish",
        "content": "Test for validate no title"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_title = response_content['title']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_title['raw']).is_equal_to('')


@pytest.mark.regression
@allure.suite("regression")
@allure.title("Test for create a page with blank title")
def test_valid_void_title():
    get_token()
    payload = json.dumps({
        "title": "  ",
        "status": "publish",
        "content": "Test for validate void title"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_title = response_content['title']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_title['raw']).is_equal_to('')


@pytest.mark.regression
@allure.suite("regression")
@allure.title("Test for create a page with null title")
def test_valid_null_title():
    get_token()
    payload = json.dumps({
        "status": "publish",
        "content": "Test for validate null title"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_title = response_content['title']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_title['raw']).is_equal_to('')


@pytest.mark.regression
@pytest.mark.sanity
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with null content")
def test_valid_null_content():
    get_token()
    payload = json.dumps({
        "title": "null content",
        "status": "publish",
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_content = response_content['content']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_content['raw']).is_equal_to('')


@pytest.mark.regression
@pytest.mark.sanity
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page without content")
def test_valid_void_content():
    get_token()
    payload = json.dumps({
        "title": "void content",
        "status": "publish",
        "content": ""
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_content = response_content['content']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_content['raw']).is_equal_to('')


@pytest.mark.regression
@pytest.mark.sanity
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with blank content")
def test_valid_no_content():
    get_token()
    payload = json.dumps({
        "title": "void content",
        "status": "publish",
        "content": "  "
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_content = response_content['content']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_content['raw']).is_not_empty()


@pytest.mark.regression
@pytest.mark.sanity
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with invalid status")
def test_invalid_status():
    status = 'not a status'
    payload = json.dumps({
        "title": "void content",
        "status": status,
        "content": "  "
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.BAD_REQUEST)
    assert_that(response_content['data']['status']).is_equal_to(400)


@pytest.mark.regression
@pytest.mark.sanity
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with void status")
def test_void_status():
    payload = json.dumps({
        "title": "void content",
        "status": "",
        "content": "test for validate the void status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.BAD_REQUEST)
    assert_that(response_content['data']['status']).is_equal_to(400)


@pytest.mark.regression
@pytest.mark.sanity
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with default status")
def test_null_status():
    payload = json.dumps({
        "title": "void content",
        "content": "test for validate the void status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['status']).is_equal_to('draft')


@pytest.mark.regression
@pytest.mark.security
@allure.suite("regression")
@allure.suite("security")
@allure.title("Test for create a page with invalid token")
def test_invalid_token():
    invalid_token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey'
    payload = json.dumps({
        "title": "invalid token",
        "status": "publish",
        "content": "test an invalid token"
    })
    responses = CrudPage().post_with_token(payload, invalid_token)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.UNAUTHORIZED)
    assert_that(responses[dict_response]['error_description']).is_equal_to("Incorrect JWT Format.")
