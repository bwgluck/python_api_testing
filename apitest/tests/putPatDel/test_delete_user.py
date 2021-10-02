import logging as logger
import pytest
from apitest.src.helpers.users_helper import UsersHelper


@pytest.mark.delete
def test_delete_user():
    logger.info('TEST: Delete user')

    user_id = '2'

    del_obj = UsersHelper()
    response_code = del_obj.delete_user(user_id)

    logger.info(f'Delete response code: {response_code}')


@pytest.mark.delete
def test_delete_fail_no_id():
    logger.info('TEST: Fail to delete user since there is no id')

    del_obj = UsersHelper()
    response_code = del_obj.delete_user()

    logger.info(f'Delete response code: {response_code}')
