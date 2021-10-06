from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon product {product_id} Page')
def open_amazon(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@then ("Verify user can click through colors")
def verify_user_can_click_through_colors(context):
    colors = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")
    for color in colors:
        color.click()