from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

@given("Open Amazon T&C page")
def open_amazon_term_and_condition_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def store_current_window(context):
    context.driver.original_window = context.driver.current_window_handle
    print(f'cCurrent window handle: {context.driver.original_window}')

@when('Click on Amazon Privacy Notice link')
def click_on_amazon_privacy_notice_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']").click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    all_window_handles = context.driver.window_handles
    print(all_window_handles)
    context.driver.switch_to.window(all_window_handles[1])
    print(f'Current window handle (after switch): {context.driver.current_window_handle}')

@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_Privacy_page_is_open(context):
    verify_amazon_Privacy = context.driver.find_element(By.CSS_SELECTOR, "div.help-service-content h1").text

    assert verify_amazon_Privacy == 'Amazon.com Privacy Notice'

@then('User can close new window and switch back to original')
def User_can_close_new_window_and_switch_back_original(context):
    context.driver.close()
    context.driver.switch_to_window(context.driver.original_window)





