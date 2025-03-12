from bs4 import BeautifulSoup
import os
import pandas as pd
import logging

# Initialize logging
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

# Data dictionary
d = {'title': [], 'price': [], 'link': []}

# Folder path
folder_path = "WebScrapingSearchProjectData"

if not os.path.exists(folder_path):
    print(f"Directory '{folder_path}' does not exist.")
    exit()

# Base URL for Flipkart
base_url = "https://www.flipkart.com"

# Iterate over files in the directory
for file in os.listdir(folder_path):
    try:
        with open(os.path.join(f"{folder_path}/{file}"), encoding='utf-8') as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Extract title
        title = soup.find('div', class_='KzDlHZ')
        title_text = title.get_text(strip=True) if title else "N/A"

        # Extract price
        price = soup.find('div', class_='Nx9bqj _4b5DiR')
        price_text = price.get_text(strip=True) if price else "N/A"
        # price_text = price_text.replace('â‚¹', 'Rs. ') 
        price_text = price_text.replace('₹', '') 
        
        # Extract link
        link_tag = soup.find('a', class_='CGtC98')
        link_url = link_tag['href'] if link_tag else ""
        full_url = base_url + link_url if link_url else "N/A"

        # Append data
        d['title'].append(title_text)
        d['price'].append(price_text)
        d['link'].append(full_url)

    except Exception as e:
        logging.error(f"Error processing file {file}: {e}")

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data=d)
df.to_csv("WebScrapingSearchProjectDataCollected.csv", index=False, encoding='utf-8')

print("Data collection completed. Check 'WebScrapingSearchProjectDataCollected.csv' for results.")


''' OLD Code
from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price': [], 'link':[]}
# Discounted Price = Nx9bqj _4b5DiR

for file in os.listdir("WebScrapingSearchProjectData"):
    try:
        with open(f"WebScrapingSearchProjectData/{file}") as f:
            html_doc =  f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

        title = soup.find('div', class_='KzDlHZ').get_text(strip=True)

        price = soup.find('div', class_='Nx9bqj _4b5DiR').get_text(strip=True)

        base_url = "https://www.flipkart.com"
        link_tag = soup.find('a', class_='CGtC98')
        if link_tag:
            link_url = link_tag['href']
        full_url = base_url + link_url

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(full_url)

        # print(soup.prettify())

    except Exception as e:
        print(e)

df = pd.DataFrame(data=d)
df.to_csv("WebScrapingSearchProjectDataCollected.csv")
---------------Improved by CHATGPT 
Potential Issues and Fixes:
Price Encoding Issue:

The price might appear as garbled text (e.g., Ã¢â€šÂ¹32,990). Use proper encoding:
python
Copy code
price = soup.find('div', class_='Nx9bqj _4b5DiR').get_text(strip=True).encode('latin1').decode('utf-8')
Handling Missing or Incorrect Data:

If any of the elements (title, price, or link) are missing in the HTML file, your code will throw an error. Add checks before extracting these fields:
python
Copy code
title = soup.find('div', class_='KzDlHZ')
title_text = title.get_text(strip=True) if title else "N/A"

price = soup.find('div', class_='Nx9bqj _4b5DiR')
price_text = price.get_text(strip=True).encode('latin1').decode('utf-8') if price else "N/A"

link_tag = soup.find('a', class_='CGtC98')
link_url = link_tag['href'] if link_tag else ""
full_url = base_url + link_url if link_url else "N/A"
Folder Path Check:

Ensure the directory WebScrapingSearchProjectData exists. If not, handle it gracefully:
python
Copy code
if not os.path.exists("WebScrapingSearchProjectData"):
    print("Directory 'WebScrapingSearchProjectData' does not exist.")
    exit()
Error Logging:

Instead of printing the error directly, log it for better debugging:
python
Copy code
import logging
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)
logging.error(f"Error processing file {file}: {e}")
CSV Encoding:

Save the CSV with UTF-8 encoding to avoid any character issues:
python
Copy code
df.to_csv("WebScrapingSearchProjectDataCollected.csv", index=False, encoding='utf-8')
'''
