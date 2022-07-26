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
from tests.get_token import test_get_token
from utils.print_helpers import pretty_print
from helpers.config import AUTHORIZATION, status_code, json_response, dict_response


def test_delete():
    id = 37
    responses = CrudPage().delete(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    pretty_print(responses[json_response])

    # Negative test


def test_delete_notfound_id():
    id = "1"
    responses = CrudPage().delete(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])


def test_delete_string_id_enter():
    id = "cuatro"
    responses = CrudPage().delete(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])


def test_delete_incorrect_token():
    id = "33"
    filename = "../helpers/config.py"
    text = open(filename).read()
    open(filename, "w+").write(text.replace(AUTHORIZATION, 'Bearer a5s4d65ad4s5'))
    responses = CrudPage().delete(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.UNAUTHORIZED)
    pretty_print(responses[json_response])
    test_get_token()
