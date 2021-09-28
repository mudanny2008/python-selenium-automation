from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')

@when ('click on the cart icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()

@then ('verify that amazon cart is empty')
def verify_that_amazon_cart_is_empty(context):
    sleep(4)
    text = context.driver.find_element(By.CSS_SELECTOR, 'div#sc-empty-cart-message h2').text
    assert text == 'Your Amazon Cart is empty', f"got {text}"
