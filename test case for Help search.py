from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
print('here:', driver.current_url)

search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('Cancel order')
search.send_keys(Keys.ENTER)
element=driver.find_element(By.XPATH, "//div[@class='help-content']/h1")


# verify
assert 'Cancel Items or Orders' in element.text, f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
