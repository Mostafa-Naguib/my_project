from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.gsmarena.com")

search = driver.find_element("id", "topsearch-text")
search.send_keys("Samsung galaxy S23 ultra")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
