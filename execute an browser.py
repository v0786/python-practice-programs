from selenium
import webdriver

# Initialize the Chrome WebDriver (you need to have chromedriver installed)
chrome_driver_path = 'path_to_chromedriver.exe'  # Replace with your chromedriver path
driver = webdriver.Chrome(chrome_driver_path)

# Open a website
website_url = 'https://www.google.com'  # Replace with the URL of the website you want to open
driver.get(website_url)

# Wait for a few seconds (optional)
import time
time.sleep(5)

# Close the browser
driver.quit()
