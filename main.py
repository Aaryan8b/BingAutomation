# Automate bing searches
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

try:
    # Set up Edge options and service beecause hadn't set up the path
    options = Options()
    #give path to webdriver
    service = Service('E:\\BingAutomation\\msedgedriver.exe')
    
    # Opening the browser
    driver = webdriver.Edge(service=service, options=options)
    # searching for table of 15 to 35
    for i in range(15, 35):
        driver.get(f'https://www.bing.com/search?q=table+of+{i}&form=ANNTH1&refig=d180d3a2e0554f7d9bb46a558d7d4ecd&pc=EDBBAN&adppc=EDGEDBB')
        #time.sleep(2)
    
    

finally:
    # Ensure the WebDriver is closed properly
    
    time.sleep(30)
    driver.quit() 
