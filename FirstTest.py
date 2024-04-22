import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
element = driver.find_element(By.CLASS_NAME('login_logo')).text
assert element == "Sauce Demo"
driver.find_element(By.ID('user-name')).send_keys('standard_user')
driver.find_element(By.ID('password')).send_keys('secret_sauce')
driver.find_element(By.ID('login-button')).click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH("//div[@class='inventory_item'][1]//button")).click()
driver.implicitly_wait(10)
cartItems = driver.find_element(By.XPATH("//span[@class='shopping_cart_badge")).get_attribute("text")
assert cartItems == "1"
driver.implicitly_wait(10)
driver.find_element(By.XPATH("//div[@class='react-burger-menu-btn']")).click()
driver.find_element(By.XPATH("//a[@id='logout_sidebar_link']")).click()




