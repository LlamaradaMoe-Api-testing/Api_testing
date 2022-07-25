#
# create_page.py Copyright (c) 2022 Jalasoft.
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

from utils.requests import Requests
import json
from config import URI
from config import AUTHORIZATION
from helpers.build_create_page import CreatePage


class CreatePage(CreatePage):
    def __init__(self, title='example', status="publish", content=""):
        self.token = AUTHORIZATION
        self.title = title
        self.content = content
        self.status = status
        self.url = f'{URI}/wp-json/wp/v2/pages/'

    def create(self):
        payload = json.dumps({
            "title": self.title,
            "status": self.status,
            "content": self.content
        })
        headers = {
            'Authorization': 'Bearer ' + AUTHORIZATION,
            'Content-Type': 'application/json'
        }
        request = Requests(self.url, headers, payload)
        response = request.get_responses(request.get_request('post'))
        return response

    def set_token(self, token):
        self.token = token
