
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class WebDriverCustomClass(object):

    def __init__(self, driver):
        self.driver = driver

    def get_by(self, locator):
        if locator.lower() == 'id':
            return By.ID
        elif locator.lower() == 'name':
            return By.NAME
        elif locator.lower() == 'tag_name':
            return By.TAG_NAME
        elif locator.lower == 'xpath':
            return By.XPATH
        elif locator.lower == 'class_name':
            return By.CLASS_NAME
        elif locator.lower() == 'css_selector':
            return By.CSS_SELECTOR
        elif locator.lower() == 'link_text':
            return By.LINK_TEXT
        elif locator.lower() == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT
        else:
            raise Exception('No such type of locator!')

    def get_element(self, locator, locator_type='id'):
        try:
            by_type = self.get_by(locator_type)
            self.driver.find_element(by_type, locator)
        except:
            raise Exception('Element not found!')

    def is_element_visible(self, locator, locator_type='id'):
        try:
            by_type = self.get_element(locator_type)
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(ec.visibility_of_element_located((by_type, locator)))
            return element
        except:
            raise Exception('Element is not visible!')
