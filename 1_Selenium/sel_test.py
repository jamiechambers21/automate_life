# Test

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()



def use_search_bar():
    driver.get("https://jqueryui.com/")
    print(driver.title)

    search = driver.find_element(by=By.NAME, value="s")
    search.clear() # Clear search bar 
    search.send_keys("test")
    search.send_keys(Keys.RETURN)

    content = driver.find_element(by=By.ID, value="content")

    articles = content.find_elements(by=By.TAG_NAME, value="article")
    for article in articles:
        header = article.find_element(by=By.CLASS_NAME, value="entry-title")
        print(header.text)

def use_mouse():
    driver.get("https://jqueryui.com/")
    print(driver.title)
    
    link = driver.find_element(by=By.LINK_TEXT, value="Add Class")
    link.click()

    try:
        wait = WebDriverWait(driver, timeout=5)

        elem = wait.until(EC.presence_of_element_located((By.ID, "button")))
        elem.click()

        driver.back()
        driver.back()
        # driver.forward()

    except:
        driver.quit()

# use_search_bar()
use_mouse()


time.sleep(5)
