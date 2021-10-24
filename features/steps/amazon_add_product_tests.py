from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon add Page')
def open_amazon(context):
    context.app.main_page.open_main_page()



@when('Input {search_word} into amazon search')
def search_amazon(context, search_word):
    #print(search_word)
    context.app.header.input_search(search_word)



@when('Click amazon search icon')
def click_search(context):
    context.app.header.click_search()

@when ('Click on the first product')
def click_first_product(context):
    context.app.search_results_page.click_first_product()


#@when ('Store product name')
#def get_product_name(context):
    #context.current_product_name =
    #results = context.driver.find_elements(By.XPATH, "//div[@class='a-section a-spacing-none a-spacing-top-small']/h2/a/span")
    #print(len(results))
    #context.current_product_name = results[2].text
    #print(f'current product: {context.current_product_name}')

@when('Store product name')
def get_product_name(context):
    context.current_product_name = context.app.product_page.get_product_name()

#@when ('Click on product')
#def click_on_product(context):
    #context.driver.find_element(By.XPATH, "//span[@class='a-price']").click()


@when('Click on add to the cart button')
def click_add_to_cart(context):
    context.app.product_page.click_add_to_cart()
    sleep(1)
    #context.driver.find_element(By.ID, 'add-to-cart-button').click()
    #context.driver.find_element(By.ID, 'attachSiNoCoverage').click()


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/aw/c?ref_=navm_hdr_cart')
    sleep(5)

@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(By.ID, 'nav-cart-count').text


    assert actual_count == expected_count, f'Expexted {expected_count} item(s), but got {actual_count}'


@when('Click Amazon Orders link')
def click_orders_link(context):
    context.app.header.click_orders_link()

@then('Verify Sign In page is opened')
def verify_sign_in_page(context):
    context.app.main_page.verify_sign_in_page()


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()

@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_shopping_cart_is_empty(context):
    context.app.main_page.Verify_Your_Shopping_Cart_is_empty_text_present()
