from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
username.send_keys("standard_user")
sleep(2)
password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
password.send_keys("secret_sauce")
sleep(2)
login = driver.find_element(By.XPATH, "//*[@id='login-button']")
login.click()
product = driver.find_elements(By.CLASS_NAME, ("inventory_item"))
print(str(len(product)))

