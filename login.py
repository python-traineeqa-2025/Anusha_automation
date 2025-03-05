import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\anushagi\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Class_automation\Anusha_automation\bin\chromedriver.exe"
ser=Service(driver_path)
driver=webdriver.Chrome(service=ser)
url="https://www.saucedemo.com/"
driver.get(url)
def login(username,password):

    uname = driver.find_element(By.XPATH, "//input[@id='user-name']")
    uname.send_keys(username)
    pwd = driver.find_element(By.XPATH, "//input[@id='password']")
    pwd.send_keys(password)
    login = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login.click()

#valid_username and valid_password
login("standard_user","secret_sauce")
time.sleep(5)
driver.back()
time.sleep(5)
#invalid_username and valid_password
login("standard_user123","secret_sauce")
time.sleep(5)
driver.refresh()

#valid_username and invalid_password
login("locked_out_user","secret_saucee1233")
time.sleep(5)
driver.refresh()

#invalid_username and invalid_password
login("standard_user234","secret_saucee1233")
time.sleep(5)
driver.close()







