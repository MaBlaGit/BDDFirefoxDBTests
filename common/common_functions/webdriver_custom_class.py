
"""Selenium WebDriver functions."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def get_by(locator_type):
    locator_type = locator_type.lower()
    if locator_type == 'id':
        return By.ID
    elif locator_type == 'name':
        return By.NAME
    elif locator_type == 'tag_name':
        return By.TAG_NAME
    elif locator_type == 'xpath':
        return By.XPATH
    elif locator_type == 'class_name':
        return By.CLASS_NAME
    elif locator_type == 'css_selector':
        return By.CSS_SELECTOR
    elif locator_type == 'link_text':
        return By.LINK_TEXT
    elif locator_type == 'partial_link_text':
        return By.PARTIAL_LINK_TEXT
    else:
        raise Exception('No such type of locator!')


def get_element(context, locator, locator_type='id'):
    try:
        by_type = get_by(locator_type)
        element = context.driver.find_element(by_type, locator)
        return element
    except:
        raise Exception('Element not found!')


def delete_all_cookies(context):
    context.driver.delete_all_cookies()


def click_at(context, locator, locator_type='id'):
    element = get_element(context, locator, locator_type)
    element.click()


def refresh_page(context):
    context.driver.refresh()


def is_element_visible(context, locator, locator_type='id'):
    try:
        by_type = get_by(locator_type)
        wait = WebDriverWait(context.driver, 10)
        element = context.element = wait.until(ec.visibility_of_element_located((by_type, locator)))
        return element
    except:
        raise Exception('Element is not visible!')
