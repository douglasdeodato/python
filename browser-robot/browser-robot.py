import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# read the JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

# get the URL from the config dictionary
url = config['url']

# start a new web driver and open the URL
driver = webdriver.Chrome()
driver.get(url)

# find the export button by its ID and click it
export_button = driver.find_element_by_id('id-here')
export_button.click()

# close the web driver
driver.quit()
