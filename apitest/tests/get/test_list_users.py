import logging as logger
import pytest
from apitest.src.helpers.users_helper import UsersHelper


@pytest.mark.get_all
@pytest.mark.get
def test_list_users():
    logger.info('TEST: Get list of users')

    # make the call
    users_obj = UsersHelper()
    users_api_info = users_obj.get_user()

    logger.info(f'Number of users returned: {users_api_info["total"]}')
