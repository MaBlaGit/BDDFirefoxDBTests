from behave import given, when, then
from common.common_configs.website_urls import website_url
import time


@given('I go to the "{url}"')
def go_to_url(context, url):
    current_url = website_url.get(url)
    context.driver.get(current_url)
    time.sleep(5)


@given('I check if "{url}" is visible')
def check_if_page_visible(context, url):
    pass