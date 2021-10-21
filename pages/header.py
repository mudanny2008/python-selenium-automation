from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDER_LINK = (By.CSS_SELECTOR, "a#nav-orders")
    CART_LINK = (By.CSS_SELECTOR, "a#nav-cart")

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD )

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders_link(self):
        self.click(*self.ORDER_LINK)

    def click_cart_icon(self):
        self.click(*self.CART_LINK)



