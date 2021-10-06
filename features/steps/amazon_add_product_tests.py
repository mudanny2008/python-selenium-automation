from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#@given('Open Amazon Page')
#def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')



@when('Input {search_word} into amazon search')
def search_amazon(context, search_word):
    #print(search_word)
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


#@when('Click on amazon search icon')
#def click_search(context):
    #context.driver.find_element(By.ID, 'nav-search-submit-button')

#@when ('Click on the first product')
#def click_first_product(context):
    #context.driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a price']]").click()

@when ('Store product name')
def get_product_name(context):
    #context.current_product_name =
    results = context.driver.find_elements(By.XPATH, "//div[@class='a-section a-spacing-none a-spacing-top-small']/h2/a/span")
    print(len(results))
    context.current_product_name = results[2].text
    print(f'current product: {context.current_product_name}')

@when ('Click on product')
def click_on_product(context):
    context.driver.find_element(By.XPATH, "//span[@class='a-price']").click()


@when('Click on add to the cart')
def click_add_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()
    context.driver.find_element(By.ID, 'attachSiNoCoverage').click()


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/aw/c?ref_=navm_hdr_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(By.ID, 'nav-cart-count').text


    assert actual_count == expected_count, f'Expexted {expected_count} item(s), but got {actual_count}'


