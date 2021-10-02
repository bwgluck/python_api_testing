import logging as logger
import random
import string


def generate_random_email_and_pass(domain=None, email_prefix=None):
    logger.debug('Generating random email and password...')

    if not domain:
        domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_len = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_len))

    email = email_prefix + '_' + random_string + '@' + domain

    password_len = 20
    password_string = ''.join(random.choices(string.ascii_letters, k=password_len))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f'Randomly generated email and password: {random_info}')

    return random_info
