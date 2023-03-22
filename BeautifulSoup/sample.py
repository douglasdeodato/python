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

# create an empty list to store the links
links = []

# find all links on the webpage and append their href values to the links list
for link in soup.find_all('a'):
    href = link.get('href')
    links.append(href)
    # print the href value
    print(href)

# create a dictionary to store the links
data = {'links': links}

# write the dictionary to a JSON file
with open('links.json', 'w') as f:
    json.dump(data, f)
    # print a message to the terminal
    print("JSON file created!")
