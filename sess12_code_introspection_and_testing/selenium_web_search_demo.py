# Python script to demonstrate opening a website (Python official site) and searching for
# a term ('lists' in our case) on the site

# NB: ensure the 'selenium' module is installed by running `pip install selenium` on the terminal

# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup the browser files
driver = webdriver.Firefox()

# Create an explicit wait object (wait for upto 20 seconds)
wait = WebDriverWait(driver, 20)

# Open the official Python website
driver.get("https://www.python.org")

# Wait for the search box to be present and interactable
search_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "q"))
)

# Enter our search term 'lists' and submit
search_box.send_keys("List")
search_box.send_keys(Keys.RETURN)

# Explicitly wait for the search results to load
results = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.list-recent-events li h3"))
)

# Print / display the titles of the search results
for result in results:
    print(result.text)

# Close the browser
driver.quit()