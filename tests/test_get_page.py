# 
# test_get_page.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
# 
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from assertpy.assertpy import assert_that
from http import HTTPStatus
from helpers.crud import CrudPage
from helpers.get_token import get_token
from utils.print_helpers import pretty_print
from helpers.payload_schema import body, schema_draft
from utils.dotenv_manager import dotenv_loader
import os
import pytest
import allure
import logging

dotenv_loader()
status_code: int = int(os.environ.get('status_code'))
json_response: int = int(os.environ.get('json_response'))
dict_response: int = int(os.environ.get('dict_response'))

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@allure.title('Setting the environment')
@allure.step('Preparing request')
@pytest.fixture(autouse=True)
def setup_requisites():
    get_token()
    global requests
    requests = CrudPage().post(body())
    global title
    title = requests[dict_response]['title']['rendered']
    id_page = requests[dict_response]['id']
    yield
    payload = {}
    CrudPage().delete(id_page, payload)


# Happy path
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.acceptance
@pytest.mark.regression
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("test for validate if all the created pages are displayed correctly")
@allure.step("Method: test_get_all")
def test_get_all():
    logger.info('Executed test for validate get all pages correctly')
    responses = CrudPage().get_all()
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    pretty_print(responses[json_response])
    logger.debug(f'Request executed successfully')
    logger.info('Test for validate get all pages correctly executed successfully')


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.acceptance
@pytest.mark.regression
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("test for validate if a created page with status publish is displayed correctly")
@allure.step("Method: test_get_page_id_publish")
def test_get_page_id_publish():
    logger.info('Execute test for get a page by id')
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('publish')
    pretty_print(json)
    logger.debug(f'Request executed successfully')
    logger.info('Test for get a page by id executed successfully')


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.acceptance
@pytest.mark.regression
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("test for validate if a created page with status trash is displayed correctly")
@allure.step("Method: test_get_page_id_trash")
def test_get_page_id_trash():
    logger.info('Execute test for get a page created with status "trash"')
    payload = {}
    responses = CrudPage().delete(requests[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('trash')
    pretty_print(json)
    logger.debug(f'Request executed successfully')
    logger.info('Test for get a page created with status "trash" executed successfully')


@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.acceptance
@pytest.mark.regression
@allure.suite("regression")
@allure.suite("acceptance")
@allure.title("test for validate if a created page with status draft is displayed correctly")
@allure.step("Method: test_get_page_id_draft")
def test_get_page_id_draft():
    logger.info('Execute test for get a page created with status "draft"')
    requests = CrudPage().post(schema_draft())
    title = requests[dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('draft')
    pretty_print(json)
    logger.debug(f'Request executed successfully')
    logger.info('Test for get a page created with status "draft" executed successfully')
    id = requests[dict_response]['id']
    payload = {}
    CrudPage().delete(id, payload)


# Negative Test
@pytest.mark.negative
@pytest.mark.regression
@allure.suite("regression")
@allure.suite("negative")
@allure.title("test for validate if a created page that dont have id valid is not displayed")
@allure.step("Method: test_get_id_notexist")
def test_get_id_notexist():
    logger.info('Execute test for validate status not found (404) at get a page with no existing id')
    id = 'cuare'
    responses = CrudPage().get_by_id(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])
    logger.debug(f'Request executed successfully')
    logger.info('Test for validate status not found (404) at get a page with no existing id executed successfully')


@pytest.mark.negative
@pytest.mark.regression
@allure.suite("regression")
@allure.suite("negative")
@allure.title("test for validate if a created page that dont have id valid is not displayed")
@allure.step("Method: test_get_page_id_is_not_publish")
def test_get_page_id_is_not_publish():
    logger.info('Execute test for validate if page created with an invalid id is not displayed')
    requests = CrudPage().post(schema_draft())
    title = requests[dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dicto = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dicto['title']['rendered']).is_equal_to(title)
    assert_that(dicto['status']).is_not_equal_to('publish')
    pretty_print(json)
    logger.debug(f'Request executed successfully')
    logger.info('Test for validate if page created with an invalid id is not displayed executed successfully')
    id = requests[dict_response]['id']
    payload = {}
    CrudPage().delete(id, payload)


@pytest.mark.negative
@pytest.mark.regression
@allure.suite("regression")
@allure.suite("negative")
@allure.title("test for validate the status of page is not trash")
@allure.step("Method: test_get_page_id_is_not_trash")
def test_get_page_id_is_not_trash():
    logger.info('Executed test for get pages with validate the status not trash')
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_not_equal_to('trash')
    pretty_print(json)
    logger.debug(f'Request executed successfully')
    logger.info('Test for get pages with validate the status not trash executed successfully')
