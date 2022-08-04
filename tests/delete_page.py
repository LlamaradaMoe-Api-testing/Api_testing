# delete_page.py Copyright (c) 2022 Jalasoft.
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
from utils.dotenv_manager import dotenv_loader
import os


dotenv_loader()
status_code: int = int(os.environ.get('status_code'))
json_response: int = int(os.environ.get('json_response'))
dict_response: int = int(os.environ.get('dict_response'))


# Happy path
@pytest.mark.smoke
def test_delete():
    id = CrudPage().post(body())
    payload = {}
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(responses[dict_response]['status']).is_equal_to('trash')
    pretty_print(responses[json_response])
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.GONE)

@pytest.mark.acceptance
def test_deleted_with_send_payload():
    id = CrudPage().post(body())
    responses = CrudPage().delete(id[dict_response]['id'], body())
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    payload = {}
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.GONE)
    pretty_print(responses[json_response])

@pytest.mark.black_box
def test_validate_schema():
    file = open('../helpers/schema-delete.json', "r")
    schema = json.loads(file.read())
    id = CrudPage().post(body())
    payload = {}
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    schema_test = json.loads(responses[json_response])
    validate(instance=schema_test, schema=schema)
# Negative test
@pytest.mark.negative
def test_delete_notfound_id():
    id = 1
    payload = {}
    responses = CrudPage().delete(id, payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])

@pytest.mark.negative
def test_delete_string_id_enter():
    id = "cuatro"
    payload = {}
    responses = CrudPage().delete(id, payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])

@pytest.mark.blackbox
def test_delete_incorrect_token():
    id = CrudPage().post(body())
    payload = {}
    responses = CrudPage().delete_not_token(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.UNAUTHORIZED)
    pretty_print(responses[json_response])
    responses = CrudPage().delete(id[dict_response]['id'], payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
