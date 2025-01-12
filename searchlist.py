# Automate bing searches
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

try:
    # Set up Edge options and service beecause hadn't set up the path
    options = Options()
    service = Service('E:\\BingAutomation\\msedgedriver.exe')
    
    # Opening the browser
    driver = webdriver.Edge(service=service, options=options)
    # searching for item in a list
    list=['table','chair','pen','book','laptop','phone','bag','shoe','shirt','trouser']
    for i in list:
        driver.get(f'https://www.bing.com/search?q=facts+on+{i}')
        #time.sleep(2)
    
    

finally:
    # Ensure the WebDriver is closed properly
    
    time.sleep(30)
    driver.quit() 