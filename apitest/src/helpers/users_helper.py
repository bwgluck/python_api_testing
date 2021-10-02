import pytest
from apitest.src.utilities.requests_utility import RequestUtility


class UsersHelper(object):
    def __init__(self):
        self.requests_utility = RequestUtility()

    def create_user(self, name=None, job=None):
        payload = dict()
        payload['name'] = name
        payload['job'] = job

        create_user_json = self.requests_utility.post('/users', payload=payload, headers=None, expected_status_code=201)

        return create_user_json

    def delete_user(self, user_id=None):
        if not user_id:
            pytest.fail(f'No user ID provided. Cannot make delete request without user ID intended for deletion.')

        endpoint = f'/users/{user_id}'

        actual_status_code = self.requests_utility.delete(endpoint, headers=None, expected_status_code=204)

        return actual_status_code

    def login_user(self, email=None, password=None):
        payload = dict()
        payload['email'] = email
        payload['password'] = password

        login_user_json = self.requests_utility.post('/login', payload=payload, headers=None, expected_status_code=200)

        return login_user_json

    def get_user(self, user_id=None):
        if not user_id:
            endpoint = '/users'
        else:
            endpoint = f'/users/{user_id}'

        get_user_json = self.requests_utility.get(endpoint, headers=None, expected_status_code=200)

        return get_user_json

    def update_user(self, name=None, job=None, user_id=None):
        if not user_id:
            pytest.fail(f'No user ID provided. Cannot make put request without user ID intended for update.')

        endpoint = f'/users/{user_id}'

        payload = dict()
        payload['name'] = name
        payload['job'] = job

        put_user_json = self.requests_utility.put(endpoint, payload=payload, headers=None, expected_status_code=200)

        return put_user_json
