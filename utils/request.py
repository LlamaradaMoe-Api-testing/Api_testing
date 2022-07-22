import requests
import json


class Requests:
    def __init__(self, url, headers, payload):
        self.url: str = url
        self.headers: dict = headers
        self.payload: dict = payload
        self.request_dic: dict = {
            'put': requests.get(self.url, headers=self.headers, data=self.payload),
            'get': requests.get(self.url, headers=self.headers, data=self.payload),
            'post': requests.get(self.url, headers=self.headers, data=self.payload),
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
