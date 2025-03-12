# Selenium Web Scraping Project

## Overview
This project uses Selenium to scrape product listings from Websites like Flipkart, Amazon..etc based on a search query. The scraped HTML data is saved in local files for further processing.

## Requirements
- Python (>=3.x)
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium library

## Installation
1. Install Selenium using pip:
   ```bash
   pip install selenium
   ```
2. Download the appropriate ChromeDriver from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/) and place it in a known directory.

## Usage
1. Update the `query` variable in the script to search for different products.
2. Run the script:
   ```bash
   python script.py
   ```
3. The scraped HTML data will be saved in the `WebScrapingSearchProjectData/` folder.

## Features
- Scrapes from Websites like Flipkart product listings based on the provided query.
- Saves individual product data as HTML files.
- Iterates through multiple pages to collect more data.

## Notes
- Ensure Flipkart's structure remains the same, as changes might break the scraper.
- Respect Flipkart's robots.txt policy to avoid violations.
- Use delays if required to prevent getting blocked.

## Disclaimer
This project is for educational purposes only. Scraping e-commerce websites may violate their terms of service.

