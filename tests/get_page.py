# 
# get_page.py Copyright (c)
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


dotenv_loader()
status_code: int = int(os.environ.get('status_code'))
json_response: int = int(os.environ.get('json_response'))
dict_response: int = int(os.environ.get('dict_response'))


# Happy path
def test_get_all():
    responses = CrudPage().get_all()
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    pretty_print(responses[json_response])


def test_get_page_id_publish():
    requests = CrudPage().post(body())
    title = requests [dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('publish')
    pretty_print(json)


def test_get_page_id_trash():
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


def test_get_page_id_draft():
    requests = CrudPage().post(schema_draft())
    title = requests[dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('draft')
    pretty_print(json)


# Negative Test
def test_get_id_notexist():
    id = 'cuare'
    responses = CrudPage().get_by_id(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])


def test_get_page_id_is_not_publish():
    requests = CrudPage().post(schema_draft())
    title = requests[dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_not_equal_to('publish')
    pretty_print(json)


def test_get_page_id_is_not_publish():
    requests = CrudPage().post(body())
    title = requests[dict_response]['title']['rendered']
    responses = CrudPage().get_by_id(requests[dict_response]['id'])
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_not_equal_to('trash')
    pretty_print(json)
