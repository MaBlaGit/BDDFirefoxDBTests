

from common.common_functions import webdriver_custom_class
from common.common_configs.website_locators import *
from common.common_configs.db_queries import *
from common.common_steps.common_behave_steps import *


@given('I "{ok}" policy')
def accept(context, ok):
    webdriver_custom_class.click_at(context, locators.get(ok), locator_type='xpath')


@when('I delete cookies from current session')
def delete_cookies(context):
    delete_all_cookies(context)


@when('I refresh the web page')
def refresh_the_page(context):
    refresh_page(context)
