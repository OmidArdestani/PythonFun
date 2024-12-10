from selenium import webdriver    #pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver-manager
from selenium.webdriver.common.keys import Keys
import time


def search_and_click(target_website_url, topic):
    # Step 1: Set up Chrome options for Incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Step 2: Set up the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open Google and search for the given topic
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")  # Find the search box
    search_box.send_keys(topic)  # Type the topic
    search_box.submit()  # Press Enter

    # Target website name or URL
    max_pages = 5  # Limit the number of pages to search through
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
                try:
                    next_button = driver.find_element(By.XPATH, "//span[@class='oeN89d' and text()='Next']")

                    next_button.click()  # Click the 'Next' button to go to the next page
                    page_number += 1
                    time.sleep(2)  # Wait for the next page to load
                    print(f"Moving to page {page_number}")
                    continue
                except Exception as e:
                    print("Error while navigating to the next page:", e)
                    break
        except Exception as e:
            print(f"Error: {e}")
            break

    # Wait for a few seconds to see the result (for demonstration)
    driver.implicitly_wait(5)

    # Close the browser
    driver.quit()
    
    
keys = ['viratak telecommunication', 'viratak telecommunications', 'viratak communications', 'viratak communication']
url = 'viratak-en.com'

for item in keys:
    web_search_automation(url, item)