from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
fileNo = 1
for i in range(1, 10+1):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")

    # time.sleep(2) 
    elements = driver.find_elements(By.CLASS_NAME, "CGtC98")
    print(f"{len(elements)} items Found ! on page {i}")
    for elem in elements:
        # print(item.text)
        d = elem.get_attribute("outerHTML")
        with open(f"WebScrapingSearchProjectData/{query}_{fileNo}.html", "w", encoding="utf-8") as f:
            f.write(d)
            fileNo += 1


print(f"Total {fileNo - 1} items Found ! on {i} pages.")

# time.sleep(2)
driver.close()  
