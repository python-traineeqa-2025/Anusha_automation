from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path=r"C:\Users\anushagi\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Class_automation\Anusha_automation\bin\chromedriver.exe"
service=Service(driver_path)
driver=webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com/")
credentials=driver.find_elements(By.XPATH,"//div[@id='login_credentials']")
print(credentials)

for i in credentials:
    cred=i.text
    print(cred)
    cred_list=cred.split('\n')
    print(cred_list)










