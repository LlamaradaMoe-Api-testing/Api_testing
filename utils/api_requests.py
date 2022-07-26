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
import allure
import requests
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Api_Requests:
    def __init__(self, url, headers, payload):
        self.url: str = url
        self.headers: dict = headers
        self.payload: dict = payload

    def get_request(self, method):
        return self.request_dic.get(method)

    def get_responses(self, response):
        status_code = response.status_code
        text = response.text
        try:
            dict_response = response.json()
        except Exception as e:
            dict_response = {}
        json_response = json.dumps(dict_response, indent=2)
        return dict_response, status_code, json_response

    def make_request(self, method):
        logger.debug('Generating the request')
        if method == 'get':
            api_request = requests.get(self.url, headers=self.headers, data=self.payload)
            allure.attach('GET', 'Method: ', allure.attachment_type.TEXT)
        if method == 'post':
            api_request = requests.post(self.url, headers=self.headers, data=self.payload)
            allure.attach('POST', 'Method: ', allure.attachment_type.TEXT)
        if method == 'delete':
            api_request = requests.delete(self.url, headers=self.headers, data=self.payload)
            allure.attach('DELETE', 'Method: ', allure.attachment_type.TEXT)
        status_code = api_request.status_code
        try:
            dict_response = api_request.json()
        except Exception as e:
            dict_response = {}
        json_response = json.dumps(dict_response, indent=2)
        return dict_response, status_code, json_response
