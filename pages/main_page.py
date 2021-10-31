
from time import sleep
from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, "h1.a-spacing-small")
    SHOPPING_CART = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty")




    def open_main_page(self):
        self.open_page()

    def verify_sign_in_page(self):
        self.verify_text('Sign-In', *self.SIGN_IN)

    def Verify_Your_Shopping_Cart_is_empty_text_present(self):
        sleep(2)

        self.verify_text('Your Amazon Cart is empty', *self.SHOPPING_CART)



