from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for i in range(1, 10):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")

    # time.sleep(2) 
    elem = driver.find_elements(By.CLASS_NAME, "KzDlHZ")
    for item in elem:
        print(item.text)


# time.sleep(2)
driver.close()  
