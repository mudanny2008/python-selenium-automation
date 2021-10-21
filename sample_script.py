from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')
driver.implicitly_wait(4)
print('here:', driver.current_url)

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# click search
button = driver.find_element(By.NAME, 'btnK')
button.click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
