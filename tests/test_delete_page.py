# test_delete_page.py Copyright (c) 2022 Jalasoft.
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
from http import HTTPStatus
from helpers.crud import CrudPage
from utils.print_helpers import pretty_print
from helpers.payload_schema import body
from helpers.get_token import get_token
from utils.dotenv_manager import dotenv_loader
from jsonschema import validate
import os
import json
import pytest
import allure
import logging


dotenv_loader()
status_code: int = int(os.environ.get('status_code'))
json_response: int = int(os.environ.get('json_response'))
dict_response: int = int(os.environ.get('dict_response'))

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Happy path
@pytest.mark.smoke
@allure.suite("smoke")
@allure.title("Test to delete a page by id")
@allure.step("Method: test_delete")
def test_delete():
    logger.info('Execute test for delete a page by id')
    get_token()
    id = CrudPage().post(body())
    payload = {}
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(responses[dict_response]['status']).is_equal_to('trash')
    pretty_print(responses[json_response])
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.GONE)
    logger.info('Test for delete a page by id executed successfully')


@pytest.mark.acceptance
@allure.suite("acceptance")
@allure.title("Test to delete a page by id sending a payload")
@allure.step("Method: test_deleted_with_send_payload")
def test_deleted_with_send_payload():
    logger.info('Execute test for delete a page by id sending a payload')
    get_token()
    id = CrudPage().post(body())
    responses = CrudPage().delete(id[dict_response]['id'], body())
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    payload = {}
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.GONE)
    pretty_print(responses[json_response])
    logger.info('Test for delete a page by id sending a payload executed successfully')


@pytest.mark.black_box
@allure.suite("black_box")
@allure.title("Test the result schema of delete a page by id")
@allure.step("Method: test_validate_schema")
def test_validate_schema():
    logger.info('Execute test for validate the response schema of delete a page by id')
    file = open('./helpers/schema-delete.json', "r")
    schema = json.loads(file.read())
    id = CrudPage().post(body())
    payload = {}
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    schema_test = json.loads(responses[json_response])
    validate(instance=schema_test, schema=schema)
    logger.debug(f'Request executed successfully')
    logger.info('Test for validate the response schema of delete a page by id executed successfully')


# Negative test
@pytest.mark.negative
@allure.suite("negative")
@allure.title("Test to delete a page by not exist id")
@allure.step("Method: test_delete_notfound_id")
def test_delete_notfound_id():
    logger.info('Execute test for validate not found (404) response at delete page with invalid id')
    get_token()
    id = 1
    payload = {}
    responses = CrudPage().delete(id, payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])
    logger.debug(f'Request executed successfully')
    logger.info('Test for validate not found (404) response at delete page with invalid id executed successfully')


@pytest.mark.negative
@allure.suite("negative")
@allure.title("Test to delete a page by an incorrect id")
@allure.step("Method: test_delete_string_id_enter")
def test_delete_string_id_enter():
    logger.info('Execute test for validate not found (404) response at delete page with incorrect id')
    get_token()
    id = "cuatro"
    payload = {}
    responses = CrudPage().delete(id, payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])
    logger.debug(f'Request executed successfully')
    logger.info('Test for validate not found (404) response at delete page with incorrect id executed successfully')


@pytest.mark.black_box
@allure.suite("black_box")
@allure.title("Test to delete a page by id with Unauthorized")
@allure.step("Method: test_delete_incorrect_token")
def test_delete_incorrect_token():
    logger.info('Execute test for validate unauthorized (403) response at delete page with invalid token')
    get_token()
    id = CrudPage().post(body())
    payload = {}
    responses = CrudPage().delete_not_token(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.UNAUTHORIZED)
    pretty_print(responses[json_response])
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    logger.debug(f'Request executed successfully')
    logger.info('Test for validate unauthorized (403) response at delete with invalid token executed successfully')
