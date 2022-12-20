from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/login/")
driver.maximize_window()
sleep(10)


username = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "pass")

username.send_keys("kadriye_1407@hotmail.com")
password.send_keys("12345")
sleep(10)
login = driver.find_element(By.XPATH,"//*[@id='loginbutton']")


login.click()
sleep(10)

title = driver.title
print(driver.title)
if  title=="Log in":
    print("Giriş başarılı 😍")
else:
    print("Giriş başarısız!😲") 
sleep(10) 

