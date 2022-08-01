#
# get_token.py Copyright (c) 2022 Jalasoft.
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


from helpers.config import USERNAME, PASSWORD, AUTHORIZATION, status_code, json_response, dict_response
from assertpy.assertpy import assert_that
from http import HTTPStatus
from helpers.crud import CrudPage


def test_get_token():
    payload = {'username': USERNAME, 'password': PASSWORD}
    responses = CrudPage().get_token(payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(responses[dict_response]['jwt_token']).is_not_empty()
    filename = "../helpers/config.py"
    text = open(filename).read()
    open(filename, "w+").write(text.replace(AUTHORIZATION, 'Bearer ' + responses[dict_response]['jwt_token']))

