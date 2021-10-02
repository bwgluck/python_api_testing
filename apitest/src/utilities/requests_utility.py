from apitest.src.configs.hosts_config import API_HOSTS
import json
import logging as logger
import os
import requests


class RequestUtility(object):

    def __init__(self):
        # Get environment. If no ENV variable, use test env.
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.expected_status_code = 400
        self.status_code = 400
        self.url = ''
        self.res_json = {}
        # With APIs that require authentication, we could use env variables to store creds.

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f'Bad status code. Expected {self.expected_status_code}, ' \
                                                                  f'Actual status code {self.status_code}, ' \
                                                                  f'URL: {self.url}, ' \
                                                                  f'Response JSON: {self.res_json}'

    def post(self, endpoint, payload=None, headers=None, expected_status_code=None):
        if not expected_status_code:
            expected_status_code = 200
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        post_rs = requests.post(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = post_rs.status_code
        self.expected_status_code = expected_status_code
        self.res_json = post_rs.json()
        self.assert_status_code()

        logger.debug(f'API response: {post_rs.json()}')
        return post_rs.json()

    def get(self, endpoint, headers=None, expected_status_code=None):
        if not expected_status_code:
            expected_status_code = 200
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        get_rs = requests.get(url=self.url, headers=headers)
        self.status_code = get_rs.status_code
        self.expected_status_code = expected_status_code
        self.res_json = get_rs.json()
        self.assert_status_code()

        logger.debug(f'API response: {get_rs.json()}')
        return get_rs.json()

    def delete(self, endpoint, headers=None, expected_status_code=None):
        if not expected_status_code:
            expected_status_code = 204
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        del_rs = requests.delete(url=self.url, headers=headers)
        self.status_code = del_rs.status_code
        self.expected_status_code = expected_status_code
        self.assert_status_code()

        return self.status_code

    def put(self, endpoint, payload=None, headers=None, expected_status_code=None):
        if not expected_status_code:
            expected_status_code = 200
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        put_rs = requests.put(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = put_rs.status_code
        self.expected_status_code = expected_status_code
        self.res_json = put_rs.json()
        self.assert_status_code()

        logger.debug(f'API response: {put_rs.json()}')
        return put_rs.json()
