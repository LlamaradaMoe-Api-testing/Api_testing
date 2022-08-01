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
from tests.get_token import test_get_token
from utils.print_helpers import pretty_print
from helpers.config import AUTHORIZATION, status_code, json_response, dict_response
#happy path
def test_get_all():
    responses = CrudPage().get_all()
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    pretty_print(responses[json_response])

def test_get_page_id_publish():
    id = 10
    title = 'Validate status response!'
    responses = CrudPage().get_by_id(id)
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('publish')
    pretty_print(json)


def test_get_page_id_trash():
    id = 5
    title = 'Hello world!!!'
    responses = CrudPage().get_by_id(id)
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('trash')
    pretty_print(json)

def test_get_page_id_draft():
    id = 5
    title = 'Hello world!!!'
    responses = CrudPage().get_by_id(id)
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_equal_to('trash')
    pretty_print(json)

def test_get_media_id():
    id = 16
    responses = CrudPage().get_media_by_id(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    pretty_print(responses[json_response])

#Negative Test
def test_get_id_notexist():
    id = 'cuare'
    responses = CrudPage().get_by_id(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])

def test_get_page_id_is_not_publish():
    id = 5
    title = 'Hello world!!!'
    responses = CrudPage().get_by_id(id)
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_not_equal_to('publish')
    pretty_print(json)

def test_get_page_id_is_not_publish():
    id = 10
    title = 'Validate status response!'
    responses = CrudPage().get_by_id(id)
    json = responses[json_response]
    dict = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(dict['title']['rendered']).is_equal_to(title)
    assert_that(dict['status']).is_not_equal_to('trash')
    pretty_print(json)