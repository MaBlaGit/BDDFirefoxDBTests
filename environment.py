
"""Fixtures which set up and tear down testing environment after each Scenario."""

from selenium import webdriver


def before_scenario(context, scenario):
    """Set up fixture."""
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    """Tear down fixture."""
    context.driver.quit()
