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
from utils.dotenv_manager import dotenv_loader, dotenv_reload
from utils.path_manager import PathManager
import os
import logging


dotenv_loader()
USERNAME = os.environ.get('USER_NAME')
PASSWORD = os.environ.get('PASSWORD')
AUTHORIZATION = os.environ.get('AUTHORIZATION')
status_code: int = int(os.environ.get('status_code'))
json_response: int = int(os.environ.get('json_response'))
dict_response: int = int(os.environ.get('dict_response'))

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def get_token():
    logger.debug('Attempt to get token')
    payload = {'username': USERNAME, 'password': PASSWORD}
    responses = CrudPage().get_token(payload)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.OK)
    assert_that(responses[dict_response]['jwt_token']).is_not_empty()
    parent_path = PathManager().get_parent_path()
    filename = os.path.join(parent_path, '.env')
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
    dotenv_reload()
    logger.debug('Token obtained')
