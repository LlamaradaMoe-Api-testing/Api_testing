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


from assertpy.assertpy import assert_that
from http import HTTPStatus
from helpers.crud import CrudPage
from utils.dotenv_manager import dotenv_loader
import os


dotenv_loader()
USERNAME = os.environ.get('USER_NAME')
PASSWORD = os.environ.get('PASSWORD')
AUTHORIZATION = os.environ.get('AUTHORIZATION')
status_code: int = int(os.environ.get('status_code'))
json_response: int = int(os.environ.get('json_response'))
dict_response: int = int(os.environ.get('dict_response'))


def test_get_token():
    payload = {'username': USERNAME, 'password': PASSWORD}
    print(USERNAME)
    print(PASSWORD)
    responses = CrudPage().get_token(payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(responses[dict_response]['jwt_token']).is_not_empty()
    filename = "../.env"
    string = 'AUTHORIZATION'
    replacement = ""
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        if string in line:
            line = 'AUTHORIZATION=Bearer ' + responses[dict_response]['jwt_token']
        replacement = replacement + line + "\n"
    file.close()
    new_file = open(filename, "w")
    new_file.write(replacement)
    new_file.close()
