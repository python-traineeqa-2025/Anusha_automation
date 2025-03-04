import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\anushagi\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Class_automation\Anusha_automation\bin\chromedriver.exe"
ser=Service(driver_path)
driver=webdriver.Chrome(service=ser)
driver.get("https://www.saucedemo.com/")

username=driver.find_element(By.XPATH,"//input[@id='user-name']")
username.click()
username.send_keys("standard_user")
password=driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys("secret_sauce")
login=driver.find_element(By.XPATH,"//input[@id='login-button']")
login.click()
product=driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Onesie']")
product.click()
description=driver.find_element(By.XPATH,"//div[@class='inventory_details_desc large_size']")
print(f"Description:{description.text}")
price=driver.find_element(By.XPATH,"//div[@class='inventory_details_price']")
print(f"Price:{price.text}")
# print("Page Title:",driver.title)

time.sleep(6)





driver.quit()

