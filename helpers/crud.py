#
# crud.py Copyright (c) 2022 Jalasoft.
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

from utils.api_requests import Api_Requests
import os


class CrudPage:
    def __init__(self):
        self.base_uri = os.environ.get('BASE_URI')
        self.authorization = os.environ.get('AUTHORIZATION')
        self.headers: dict = {
                'Authorization': self.authorization,
                'Content-Type': 'application/json'
        }

    def put(self, id, payload):
        response = Api_Requests(f'{self.base_uri}/wp/v2/pages/{id}', self.headers, payload)
        responses = response.get_responses(response.get_request('put'))
        return responses

    def post(self, payload):
        response = Api_Requests(f'{self.base_uri}/wp/v2/pages/', self.headers, payload)
        responses = response.get_responses(response.get_request('post'))
        return responses

    def delete(self, id, payload):
        response = Api_Requests(f'{self.base_uri}/wp/v2/pages/{id}', self.headers, payload)
        responses = response.get_responses(response.get_request('delete'))
        return responses

    def get_all(self):
        payload = {}
        response = Api_Requests(f'{self.base_uri}/wp/v2/pages/', self.headers, payload)
        responses = response.get_responses(response.get_request('get'))
        return responses

    def get_by_id(self, id):
        payload = {}
        response = Api_Requests(f'{self.base_uri}/wp/v2/pages/{id}', self.headers, payload)
        responses = response.get_responses(response.get_request('get'))
        return responses

    def get_token(self, payload):
        headers = {}
        response = Api_Requests(f'{self.base_uri}/api/v1/token', headers, payload)
        responses = response.get_responses(response.get_request('post'))
        return responses

    def delete_not_token(self, id, payload,token='sasdadasdasd'):
        headers: dict = {
            'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzd",
            'Content-Type': 'application/json'
        }
        response = Api_Requests(f'{self.base_uri}/wp/v2/pages/{id}', headers, payload)
        responses = response.get_responses(response.get_request('delete'))
        return responses

    def post_with_token(self, payload, token):
        self.headers: dict = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        return self.post(payload)
