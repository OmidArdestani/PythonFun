# PythonFun

This repository contains simple, small, and useful Python functions that can be easily integrated into various projects. It serves as a collection of code snippets to help automate common tasks and enhance your Python development experience. All functions are designed to be easy to understand and implement.

## Function: `web_search_automation(target_website_url, topic)`

### Description:
The `web_search_automation` function automates the process of searching for a specified topic on Google and navigating through search result pages until it finds the target website URL. It opens Google in **Incognito mode** using Selenium and clicks on the first link that matches the given target website URL.

### Parameters:
- `target_website_url` (str): The exact URL of the website to look for in the search results (e.g., `"https://www.python.org"`).
- `topic` (str): The search term to query on Google (e.g., `"Python programming"`).

### Functionality:
1. Opens Google in Incognito mode.
2. Searches for the given topic on Google.
3. Checks search result pages for the target website URL.
4. Clicks on the first result that matches the target website URL.
5. Automatically navigates to the next page if the target website is not found on the current page.

### Example Usage:
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def web_search_automation(target_website_url, topic):
    # Set up Chrome options for Incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    
    # Specify path to chromedriver manually
    chromedriver_path = "path_to_your_chromedriver"  # Replace with the actual path to chromedriver
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open Google and search for the given topic
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")  # Find the search box
    search_box.send_keys(topic)  # Type the topic
    search_box.submit()  # Press Enter
    
    # Limit the number of pages to search through
    max_pages = 5
    page_number = 1
    
    while page_number <= max_pages:
        try:
            # Find all search result links on the current page
            search_results = driver.find_elements(By.XPATH, "//h3/parent::a")
            
            for result in search_results:
                result_url = result.get_attribute("href")  # Get the URL of the search result
                if target_website_url in result_url:  # Match the URL
                    result.click()  # Click the target website
                    print(f"Found and clicked on {target_website_url}")
                    break
            else:
                # If not found on this page, go to the next page
                next_button = driver.find_element(By.XPATH, "//span[@class='oeN89d' and text()='Next']")
                next_button.click()  # Click the 'Next' button to go to the next page
                page_number += 1
                time.sleep(2)  # Wait for the next page to load
                print(f"Moving to page {page_number}")
                continue
        except Exception as e:
            print(f"Error: {e}")
            break
    
    # Wait for a few seconds to see the result (for demonstration)
    driver.implicitly_wait(5)
    
    # Close the browser
    driver.quit()
```

### Requirements:
**Selenium:** To interact with the web browser and automate the search process.
**Chrome WebDriver:** To control the Chrome browser (make sure the version matches your installed Chrome browser).
**Python 3.x:** The script is written in Python and requires Python 3.

### Installation:
1. Install Selenium:
```pip install selenium```
2. Download ChromeDriver and ensure it's compatible with your version of Google Chrome.
3. Set the ```chromedriver_path``` in the script to the location of the ChromeDriver.

# License:
This project is licensed under the MIT License.
