import json
from bs4 import BeautifulSoup

# Load the HTML file
with open('clean-html.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all the rows in the table
rows = soup.find_all('tr')

# Create an empty list to store the dictionaries
data = []

# Loop through each row and extract the data
for row in rows:
    name = row.find('td', {'class': 'name'}).text
    certification = row.find('td', {'class': 'certification'})
    certification = certification.text if certification else ""
    profile_link = row.find('td', {'class': 'profile-link'}).find('a').get('href')

    # Create a dictionary for each row and append it to the data list
    data.append({
        'name': name,
        'certification': certification,
        'profile_link': profile_link
    })

# Write the data to a JSON file
with open('therapists.json', 'w') as f:
    json.dump(data, f, indent=4)
