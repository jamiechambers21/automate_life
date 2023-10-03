# Test

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Not necessary
# PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://jqueryui.com/")
print(driver.title)

search = driver.find_element(by=By.NAME, value="s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

content = driver.find_element(by=By.ID, value="content")

articles = content.find_elements(by=By.TAG_NAME, value="article")
for article in articles:
    header = article.find_element(by=By.CLASS_NAME, value="entry-title")
    print(header.text)



# Wait that I´m not using 
# wait = WebDriverWait(driver, timeout=2)

# wait.until(lambda d : content.is_displayed())
# print(content.text)

time.sleep(20)
