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
import logging
import allure
from assertpy.assertpy import assert_that
import json
from http import HTTPStatus
from helpers.crud import CrudPage
from helpers.get_token import get_token
from jsonschema import validate
from utils.print_helpers import pretty_print
from utils.dotenv_manager import dotenv_loader
from utils.path_manager import PathManager
import os
import pytest


dotenv_loader()
status_code: int = int(os.environ.get('status_code'))
json_response: int = int(os.environ.get('json_response'))
dict_response: int = int(os.environ.get('dict_response'))

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

page_id: int = 0


@allure.title('')
@allure.step('Preparing request')
@pytest.fixture(autouse=True)
def setup_requisites():
    get_token()
    yield
    payload = {}
    CrudPage().delete(page_id, payload)


# Happy path
@pytest.mark.regression
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("Test for create a page")
@allure.step("Method: test_create_post")
def test_create_post():
    logger.info('Execute test for create a page')
    payload = json.dumps({
      "title": "Validate status response!",
      "status": "publish",
      "content": "test for validate the status response"
    })
    responses = CrudPage().post(payload)
    pretty_print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page executed successfully')
    allure.attach(responses[json_response], 'JSON response: ', allure.attachment_type.JSON)
    global page_id
    page_id = responses[dict_response]['id']
    return responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("Test for create a page with a valid token")
@allure.step("Method: test_validate_valid_token")
def test_validate_valid_token():
    logger.info('Execute test for create a page using a valid token')
    payload = json.dumps({
        "title": "Valid token!",
        "status": "publish",
        "content": "test with a valid token"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    logger.debug(f'Request executed successfully')
    logger.info('Test for for create a page using a valid token executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("Test for create a page with a valid title")
@allure.step("Method: test_valid_title")
def test_valid_title():
    logger.info('Execute test for create a page using a valid title')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page using a valid title executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("Test for create a page with a valid content")
@allure.step("Method: test_valid_content")
def test_valid_content():
    logger.info('Execute test for create a page using a valid content')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page using a valid content executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("Test for create a page with status publish")
@allure.step("Method: test_valid_status_publish")
def test_valid_status_publish():
    logger.info('Execute test for create a page using the status "publish"')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page using the status "publish" executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("Test for create a page with status draft")
@allure.step("Method: test_valid_status_draft")
def test_valid_status_draft():
    logger.info('Execute test for create a page using the status "draft"')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page using the status "draft" executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.acceptance
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("Test for create a page with status private")
@allure.step("Method: test_valid_status_private")
def test_valid_status_private():
    logger.info('Execute test for create a page using the status "private"')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page using the status "private" executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.endToend
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@allure.suite("regression")
@allure.suite("endToend")
@allure.title("Test for validate the schema response at create a page")
@allure.step("Method: test_validate_schema")
def test_validate_schema():
    logger.info('Execute test for validate the response schema')
    parent_path = PathManager().get_parent_path()
    file = open(os.path.join(parent_path, './helpers/schema-create.json'), "r")
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for validate the response schema executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


# Negative tests
@pytest.mark.regression
@allure.suite("regression")
@allure.title("Test for create a page without a title")
@allure.step("Method: test_valid_no_title")
def test_valid_no_title():
    logger.info('Execute test for create a page without a title, by default (none)')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page without a title executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@allure.suite("regression")
@allure.title("Test for create a page with blank title")
@allure.step("Method: test_valid_void_title")
def test_valid_void_title():
    logger.info('Execute test for create a page without a title, by default (none)')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page without a title executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@allure.suite("regression")
@allure.title("Test for create a page with null title")
@allure.step("Method: test_valid_null_title")
def test_valid_null_title():
    logger.info('Executed test for create a page with null a title, by default (none)')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page with null a title executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.sanity
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with null content")
@allure.step("Method: test_valid_null_content")
def test_valid_null_content():
    logger.info('Execute test for create a page with null content')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page with null content executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.sanity
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page without content")
@allure.step("Method: test_valid_void_content")
def test_valid_void_content():
    logger.info('Execute test for create a page without content')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page without content executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.sanity
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with blank content")
@allure.step("Method: test_valid_no_content")
def test_valid_no_content():
    logger.info('Execute test for create a page with blank content')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page with blank content executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.negative
@allure.suite("negative")
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with invalid status")
@allure.step("Method: test_invalid_status")
def test_invalid_status():
    logger.info('Execute test for verify bad request (400) at create a page with invalid status')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page with invalid status executed successfully')


@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.negative
@allure.suite("negative")
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with void status")
@allure.step("Method: test_void_status")
def test_void_status():
    logger.info('Execute test for verify bad request (400) at create a page with void status')
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
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page with void status executed successfully')


@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.negative
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("Test for create a page with default status")
@allure.step("Method: test_null_status")
def test_null_status():
    logger.info('Execute test for create a page without a status, by default "draft"')
    payload = json.dumps({
        "title": "void content",
        "content": "test for validate the void status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['status']).is_equal_to('draft')
    logger.debug(f'Request executed successfully')
    logger.info('Test for create a page without a status executed successfully')
    global page_id
    page_id = responses[dict_response]['id']


@pytest.mark.regression
@pytest.mark.security
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("regression")
@allure.suite("security")
@allure.title("Test for create a page with invalid token")
@allure.step("Method: test_invalid_token")
def test_invalid_token():
    logger.info('Execute test for verify unauthorized (403) at create a page with invalid token')
    invalid_token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
    payload = json.dumps({
        "title": "invalid token",
        "status": "publish",
        "content": "test an invalid token"
    })
    logger.debug(f"Token used: {invalid_token}")
    logger.debug(f'Payload: {payload}')
    responses = CrudPage().post_with_token(payload, invalid_token)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.UNAUTHORIZED)
    assert_that(responses[dict_response]['error_description']).is_equal_to("Incorrect JWT Format.")
    logger.debug(f'Request executed successfully')
    logger.info('Test for verify unauthorized (403) at create a page with invalid token executed successfully')
