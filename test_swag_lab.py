
from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pathlib import Path
from constants2 import *


class Test_Swag_Lab:
    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()
#ister 1
    def test_login(self):
        self.driver.get(BASE_DOMAIN_URL)
        username = self.driver.find_element(By.XPATH, USER_NAME_XPATH)
        username.send_keys("standard_user")
        password = self.driver.find_element(By.XPATH, PASSWORD_XPATH)
        password.send_keys("secret_sauce")
        login = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, USER_NAME_XPATH)))
        login.click()
        # login olduktan sonra yönlendirilen adrese göre kontrol sağlanmıştır.
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        sleep(5)
#ister 2
    def test_fail_control_login(self):
        self.driver.get(BASE_DOMAIN_URL)
        username = self.driver.find_element(By.XPATH, USER_NAME_XPATH)
        username.send_keys("sssstandard_user")
        password = self.driver.find_element(By.XPATH, PASSWORD_XPATH)
        password.send_keys("secret_sauc")
        login = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, USER_NAME_XPATH)))
        login.click()
        sleep(5)
#ister 3
    def test_control_login(self):
        self.driver.get(BASE_DOMAIN_URL)
        username = self.driver.find_element(By.XPATH, USER_NAME_XPATH)
        username.send_keys("ssstandard_user")
        password = self.driver.find_element(By.XPATH, PASSWORD_XPATH)
        password.send_keys("secret_sauce")
        login = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, USER_NAME_XPATH)))
        login.click()
        sleep(5)

        assert "SSSSpic sadface: Username and password do not match any user in this service" == FAIL_PASSWORD
#ister 4.

    def test_control_product_count(self):
        self.driver.get(BASE_DOMAIN_URL)
        username = self.driver.find_element(By.XPATH, USER_NAME_XPATH)
        username.send_keys("standard_user")
        sleep(2)
        password = self.driver.find_element(By.XPATH, PASSWORD_XPATH)
        password.send_keys("secret_sauce")
        sleep(2)
        login = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        login.click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))

        product = self.driver.find_elements(By.CLASS_NAME, ("inventory_item"))
        count = len(product)
        assert count == 6
#ister 5
    def test_change_button_text(self):
        self.driver.get(BASE_DOMAIN_URL)
        username = self.driver.find_element(By.XPATH, USER_NAME_XPATH)
        username.send_keys("standard_user")
        sleep(2)
        password = self.driver.find_element(By.XPATH, PASSWORD_XPATH)
        password.send_keys("secret_sauce")
        sleep(2)
        login = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        login.click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.NAME, ADD_TO_CARD_BTN_NAME)))
        addToCardBtn = self.driver.find_element(By.NAME, ADD_TO_CARD_BTN_NAME)
        addToCardBtn.click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, REMOVE_BUTTON_XPATH)))
        removeBtn = self.driver.find_element(By.XPATH, REMOVE_BUTTON_XPATH)
        remove_button_text = removeBtn.text
        assert remove_button_text == "REMOVE"
        sleep(2)
#ister 6
    def test_change_basket_number(self):
        self.driver.get(BASE_DOMAIN_URL)
        username = self.driver.find_element(By.XPATH, USER_NAME_XPATH)
        username.send_keys("standard_user")
        sleep(2)
        password = self.driver.find_element(By.XPATH, PASSWORD_XPATH)
        password.send_keys("secret_sauce")
        sleep(2)
        login = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        login.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, ADD_TO_CARD_BTN_NAME)))
        addToCardBtn = self.driver.find_element(By.NAME, ADD_TO_CARD_BTN_NAME)
        addToCardBtn.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, SHOPPING_CARD_CLASS_NAME)))
        basket_number = self.driver.find_element(By.CLASS_NAME, SHOPPING_CARD_CLASS_NAME)
        basket_item_number = basket_number.text

        assert basket_item_number == "1"
 