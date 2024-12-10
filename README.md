# PythonFun

This repository contains simple, small, and useful Python functions that can be easily integrated into various projects. It serves as a collection of code snippets to help automate common tasks and enhance your Python development experience. All functions are designed to be easy to understand and implement.

## Function: `web_search_automation.search_and_click(target_website_url, topic)`

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
import web_search_automation

keys = ['viratak telecommunication', 'viratak telecommunications', 'viratak communications', 'viratak communication']
url = 'viratak-en.com'

for item in keys:
    web_search_automation.search_and_click(url, item)
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
