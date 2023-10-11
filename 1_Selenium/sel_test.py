# Test

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)


def use_search_bar():
    # Will go onto a website and search for somethimg using the search bar
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
    # Practice using the mouse and navagating through pages
    driver.get("https://jqueryui.com/")
    print(driver.title)
    
    link = driver.find_element(by=By.LINK_TEXT, value="Add Class")
    link.click()

    try:
        wait = WebDriverWait(driver, timeout=5)

        # Can't get working, Revisit later
        elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="ui-state-default ui-corner-all"]')))
        elem.click()

        driver.back()
        driver.back()
        # driver.forward()

    except:
        driver.quit()

def action_chains():
    # Practice using action chains with the cookie clicker weiste
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    # Here we are getting past the consent/language settings
    driver.implicitly_wait(10) # Wait 10 seconds
    consent = driver.find_element(by=By.CLASS_NAME, value="fc-button-label")
    consent.click()
    lang = driver.find_element(by=By.ID, value="langSelect-EN")
    lang.click()
    driver.implicitly_wait(10) # Wait 10 seconds
    print("wait over")

    # Set up where are the elements
    cookie = driver.find_element(by=By.ID, value="bigCookie")
    cookie_count = driver.find_element(by=By.ID, value="cookies")
    items = [driver.find_element(by=By.ID, value=f"productPrice{i}") for i in range(1,-1,-1)]

    cookie.click()

    actions = ActionChains(driver)
    actions.click(cookie)

    for _ in range(5000):
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()


        
# use_search_bar()
# use_mouse()
# action_chains()