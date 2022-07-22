#
# requests.py Copyright (c) 2022 Jalasoft.
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

import requests
import json


class Requests:
    def __init__(self, url, headers, payload):
        self.url: str = url
        self.headers: dict = headers
        self.payload: dict = payload
        self.request_dic: dict = {
            'put': requests.put(self.url, headers=self.headers, data=self.payload),
            'get': requests.get(self.url, headers=self.headers, data=self.payload),
            'post': requests.post(self.url, headers=self.headers, data=self.payload),
            'delete': requests.delete(self.url, headers=self.headers, data=self.payload)
        }

    def get_request(self, method):
        return self.request_dic.get(method)

    def get_responses(self, response):
        status_code = response.status_code
        text = response.text
        try:
            dict_response = response.json()
        except Exception as e:
            dict_response = {}
        return dict_response, status_code
