from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def start_scraping(url):
    options = Options()
    options.headless = True  # Run in headless mode for no GUI
    service = Service('path/to/chromedriver')  # Update with your chromedriver path //
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        data = parse_data(driver)
        return data
    finally:
        driver.quit()

def parse_data(driver):
    # Example of extracting data; modify selectors as needed
    elements = driver.find_elements(By.CLASS_NAME, 'example-class')
    scraped_data = [element.text for element in elements]
    return scraped_data

if __name__ == "__main__":
    url = "https://cddistribution.com/pe/categoria-producto/juguetes-nuevos/pokemon-tcg/" 
    data = start_scraping(url)
    print(data)