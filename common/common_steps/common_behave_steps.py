from behave import given, when, then
from common.common_configs.website_urls import website_url
from common.common_functions.webdriver_custom_class import *
from common.common_configs.website_locators import locators


@given('I go to the "{url}"')
def go_to_url(context, url):
    current_url = website_url.get(url)
    context.driver.get(current_url)


@given('I check if page is "{visible}"')
def check_if_page_visible(context, visible):
    is_element_visible(context, locators.get(visible), locator_type='xpath')
