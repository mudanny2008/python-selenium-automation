from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('open Amazon help page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('input cancel order into search help library and press enter')
def search_amazon(context):
    search = context.driver.find_element(By.ID, 'helpsearch')
    search.clear()
    search.send_keys('Cancel order')
    search.send_keys(Keys.ENTER)

@then('verify cancel order is executable')
def verify_cancel_order_is_executable(context):
    element = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1")
    assert 'Cancel Items or Orders' in element.text, f"Expected query not in {context.driver.current_url.lower()}"
