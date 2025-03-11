import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://us.puma.com/us/en/men/clothing/pants")

time.sleep(10)
# driver.find_element(By.CSS_SELECTOR,"")