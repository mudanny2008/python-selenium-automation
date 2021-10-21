from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon product {product_id} Page')
def open_amazon(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@then ("Verify user can click through colors")
def verify_user_can_click_through_colors(context):
    colors = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

    for i in range(len(colors)):
        colors[i].click()
        current_color = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name li").text
        #assert current_color == expected_colors[i], f'Error expected {expected_colors[i]} did not match {current_color}'