# 
# @object_result.py Copyright (c)
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

def test_get_page_id():
    id = 10
    responses = CrudPage().get_by_id(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    pretty_print(responses[json_response])

def test_get_all():
    responses = CrudPage().get_all()
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    pretty_print(responses[json_response])

def test_get_id_notexist():
    id = 100
    responses = CrudPage().get_by_id(id)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.NOT_FOUND)
    pretty_print(responses[json_response])
