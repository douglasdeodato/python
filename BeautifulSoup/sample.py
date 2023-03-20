import json
import requests
from bs4 import BeautifulSoup

# read the JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

# get the URL from the config dictionary
url = config['url']

# send a request to the URL and get the response
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# print the title of the webpage
print(soup.title.string)

# find all links on the webpage and print their href values
links = soup.find_all('a')
for link in links:
    print(link.get('href'))