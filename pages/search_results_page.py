from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResults(Page):
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a price']]")
    SEARCH_RESULT_TEXT = (By.CSS_SELECTOR, "a.a-size-base.a-link-normal.a-text-normal")
    def click_first_product(self):
        self.click(*self.SEARCH_RESULT_TEXT)