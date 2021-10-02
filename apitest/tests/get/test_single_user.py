import logging as logger
import pytest
from apitest.src.helpers.users_helper import UsersHelper


@pytest.mark.get_one
@pytest.mark.get
def test_single_user():
    logger.info('TEST: Get a single user')

    user_id = '2'
    users_obj = UsersHelper()
    users_api_info = users_obj.get_user(user_id)

    # verify response
    assert users_api_info['data']['id'] == int(user_id), f'Get user api returned id that differs from provided id. ' \
                                                         f'Expected: {user_id}. Actual: {users_api_info["data"]["id"]}'


@pytest.mark.get_one
@pytest.mark.get
def test_wrong_user_id():
    logger.info('TEST: Get a single user')

    user_id = '23'
    users_obj = UsersHelper()

    with pytest.raises(Exception):
        users_obj.get_user(user_id)
