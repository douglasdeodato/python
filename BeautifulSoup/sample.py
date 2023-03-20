from bs4 import BeautifulSoup
import requests

# send a request to the URL
url = 'https://www.example.com'
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# print the title of the webpage
print(soup.title.string)

# find all links on the webpage and print their href values
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
