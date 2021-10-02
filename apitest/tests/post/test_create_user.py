import logging as logger
import pytest
from apitest.src.helpers.users_helper import UsersHelper


@pytest.mark.create
@pytest.mark.post
def test_create_user():
    logger.info('TEST: Create new user')

    name = 'morpheus'
    job = 'leader'

    # make the call
    login_obj = UsersHelper()
    login_api_info = login_obj.create_user(name=name, job=job)

    # verify user data
    assert login_api_info['name'] == name, f'Create user api returned the wrong name. Name: {name}'
    assert login_api_info['job'] == job, f'Create user api returned the wrong name. Job: {job}'

    # status code is verified in users_helper/requests_utility
