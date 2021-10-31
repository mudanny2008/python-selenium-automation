from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDER_LINK = (By.CSS_SELECTOR, "a#nav-orders")
    CART_LINK = (By.CSS_SELECTOR, "a#nav-cart")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    ARRIVALS = (By.XPATH, "//span[contains(text(), 'New Arrivals')]")
    SELECTION_ARRIVALS = (By.ID, "nav-flyout-amazonfresh")




    def select_department_by_alias(self, alias):
        select = Select(self.find_element(*self.DEPARTMENT_SELECT))
        select.select_by_value(f'search-alias={alias}')


    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD )

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders_link(self):
        self.click(*self.ORDER_LINK)

    def click_cart_icon(self):
        self.click(*self.CART_LINK)


    def hover_over_new_arrivals_options(self):
        new = self.find_element(*self.ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new)
        actions.perform()
        sleep(5)


    def Verify_correct_options_present(self):
        self.wait_for_element_appear(*self.SELECTION_ARRIVALS)








