import logging as logger
import pytest
from apitest.src.helpers.users_helper import UsersHelper
from apitest.src.utilities.generic_utilities import generate_random_email_and_pass


@pytest.mark.login
@pytest.mark.post
def test_login():
    logger.info('TEST: Login and receive token')

    # rand_info = generate_random_email_and_pass()
    # email = rand_info['email']
    # password = rand_info['password']

    email = 'eve.holt@reqres.in'
    password = 'cityslicka'

    # make the call
    user_obj = UsersHelper()
    user_api_info = user_obj.login_user(email=email, password=password)

    assert user_api_info['token'] != '', 'Login user api did not respond with a token as expected.'

    # status code is verified in users_helper/requests_utility


@pytest.mark.login
@pytest.mark.post
def test_login_no_email():
    logger.info('TEST: Login without email')

    password = 'cityslicka'

    user_obj = UsersHelper()
    with pytest.raises(Exception):
        user_obj.login_user(email=None, password=password)


@pytest.mark.login
@pytest.mark.post
def test_login_no_password():
    logger.info('TEST: Login without password. This test should fail.')

    email = 'peter@klave'

    user_obj = UsersHelper()
    user_api_info = user_obj.login_user(email=email, password=None)

    assert user_api_info['token'] != ''
