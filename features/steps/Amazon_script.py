from selenium.webdriver.common.by import By
from behave import given, when, then

HAM_MENU_ICON = By.ID, 'nav-hamburger-menu'


@when('Click on Amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID,'nav-search-submit-button').click()


@then('verify hamburger menu icon is present')
def verify_hamb_menu(context):
    expected_count = 1
    actual_count = len(context.driver.find_elements(*HAM_MENU_ICON))
    assert expected_count == actual_count, f'Actual elements{actual_count}, but expected {expected_count}'
