import logging as logger
import pytest
from apitest.src.helpers.users_helper import UsersHelper


@pytest.mark.put
def test_update_put_user():
    logger.info('TEST: Update user with PUT request')

    name = 'morpheus'
    job = 'leader'
    user_id = '2'

    # make the call
    put_obj = UsersHelper()
    put_api_info = put_obj.update_user(name=name, job=job, user_id=user_id)

    # verify user data
    assert put_api_info['name'] == name, f'Put user api returned the wrong name. Name: {name}'
    assert put_api_info['job'] == job, f'Put user api returned the wrong job. Job: {job}'
