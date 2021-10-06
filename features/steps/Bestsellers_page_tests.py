from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.by import By


TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')


@given('Open Amazon Bestsellers')
def open_amazon_Bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/')
    context.driver.refresh()


@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)

    assert len(actual_links) == int(expected_links), f'expected {expected_links} links'