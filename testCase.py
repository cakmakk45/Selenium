from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.kodlama.io/")

course = driver.find_elements(By.CLASS_NAME, ("course-listing-extra-info")) 
number_of_course = len(course)

if number_of_course == 6:
    print("Kodlama.io da bulunan toplam kurs say覺s覺:" + str(course))
else:
    print("Hatal覺 sonu癟 ????")
driver.save_screenshot(str(date.today()) + '(1).png')
sleep(5)

search = driver.find_element(By.XPATH,'//*[@name="query"]')
search.send_keys("Senior")
sleep(3)
title = driver.find_element(By.XPATH,'//*[@title="Senior Yaz覺l覺m Geli??tirici Yeti??tirme Kamp覺 (.NET)"]')
titleTest = title.text
print(title)
sleep(3)
if titleTest == "Senior Yaz覺l覺m Geli??tirici Yeti??tirme Kamp覺 (.NET)":
    print("Arama sonucu ba??ar覺l覺 ????")
else:
    print("Arama sonucu ba??ar覺s覺z????")
driver.save_screenshot(str(date.today()) + '(2).png')

driver.close()