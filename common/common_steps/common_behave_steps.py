from behave import given, when, then
from common.common_configs.website_urls import website_url
from common.common_functions.webdriver_custom_class import *
from common.common_configs.website_locators import locators


@given('I go to the {url} web page')
def go_to_url(context, url):
    context.driver.get(website_url.get(url))


@given('I check if {website} web page is visible')
def check_if_page_visible(context, website):
    is_element_visible(context, locators.get(website), locator_type='xpath')
