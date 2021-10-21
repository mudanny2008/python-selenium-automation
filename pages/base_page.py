class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'

    def click(self, *locator):  #(By.ID, 'value..')
        self.driver.find_element(*locator).click()

    def open_page(self, page_address=''):
        self.driver.get(f'{self.base_url}{page_address}')

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, text, *locator):
        current_text = self.driver.find_element(*locator).text

        assert current_text == text, f'Expected {text}, but got {current_text}'
        #assert current_text == text

    #def input_text(self, text, *locator):
        #self.driver.find_element(*locator).send_keys(text)

    #def verify_text(self, text, *locator):
        ##assert current_text == text

