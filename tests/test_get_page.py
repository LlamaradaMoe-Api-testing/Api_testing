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


# Happy path
@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.regresion
@allure.suite("acceptance")
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("test for validate if all the created pages are displayed correctly")
@allure.step("Method: test_get_all")
def test_get_all():
    logger.info('Executed test for validate get all pages correctly')
    try:
        get_token()
    except:
        logger.info('The Token is not valid')
        raise ConnectionError
    else:
        responses = CrudPage().get_all()
        try:
            assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
            logger.info('Test for validate get all pages correctly executed successfully')
        except:
            logger.info('The status of request not is valid please review if have page created and xammp turn on')
            raise ConnectionError
        finally:
            pretty_print(responses[json_response])


@allure.step('Setup: "{0}", keyword: "{key}"')
def step_with_title_placeholders(arg1, key=None):
    pass

@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.regresion
@allure.suite("acceptance")
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("test for validate if a created page with status publish is displayed correctly")
@allure.step("Method: test_get_page_id_publish")
def test_get_page_id_publish():
    logger.info('Execute test for get a page by id')

    get_token()
    requests = CrudPage().post(body())
    step_with_title_placeholders(1, requests)
    title = requests[dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('publish')
    pretty_print(json)
    logger.info('Test for get a page by id executed successfully')


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.regresion
@allure.suite("acceptance")
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("test for validate if a created page with status trash is displayed correctly")
@allure.step("Method: test_get_page_id_trash")
def test_get_page_id_trash():
    logger.info('Execute test for get a page created with status "trash"')
    get_token()
    requests = CrudPage().post(body())
    title = requests[dict_response]['title']['rendered']
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
    logger.info('Test for get a page created with status "trash" executed successfully')


@pytest.mark.acceptance
@pytest.mark.sanity
@pytest.mark.regresion
@allure.suite("acceptance")
@allure.suite("regression")
@allure.suite("sanity")
@allure.title("test for validate if a created page with status draft is displayed correctly")
@allure.step("Method: test_get_page_id_draft")
def test_get_page_id_draft():
    logger.info('Execute test for get a page created with status "draft"')
    get_token()
    requests = CrudPage().post(schema_draft())
    title = requests[dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('draft')
    pretty_print(json)
    logger.info('Test for get a page created with status "draft" executed successfully')


# Negative Test
@pytest.mark.regresion
@pytest.mark.negative
@allure.suite("negative")
@allure.suite("regression")
@allure.title("test for validate if a created page that dont have id valid is not displayed")
@allure.step("Method: test_get_id_notexist")
def test_get_id_notexist():
    logger.info('Execute test for validate status not found (404) at get a page with no existing id')
    get_token()
    id = 'cuare'
    responses = CrudPage().get_by_id(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])
    logger.info('Test for validate status not found (404) at get a page with no existing id executed successfully')


@pytest.mark.regresion
@pytest.mark.negative
@allure.suite("negative")
@allure.suite("regression")
@allure.title("test for validate if a created page that dont have id valid is not displayed")
@allure.step("Method: test_get_page_id_is_not_publish")
def test_get_page_id_is_not_publish():
    logger.info('Execute test for validate if page created with an invalid id is not displayed')
    get_token()
    requests = CrudPage().post(schema_draft())
    title = requests[dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_not_equal_to('publish')
    pretty_print(json)
    logger.info('Test for validate if page created with an invalid id is not displayed executed successfully')


@pytest.mark.regresion
@pytest.mark.negative
@allure.suite("negative")
@allure.suite("regression")
@allure.title("test for validate the status of page is not trash")
@allure.step("Method: test_get_page_id_is_not_publish")
def test_get_page_id_is_not_publish():
    logger.info('Executed test for get pages with validate the status not trash')
    get_token()
    requests = CrudPage().post(body())
    title = requests[dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_not_equal_to('trash')
    pretty_print(json)
    logger.info('Test for get pages with validate the status not trash executed successfully')
