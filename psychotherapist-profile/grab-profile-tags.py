import requests
from bs4 import BeautifulSoup
import json

# create a variable for the repeated ID portion
repeated_id = 'FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater'
             
# make a request to the web page
url = 'https://iahip.org/Sys/PublicProfile/53252855'
response = requests.get(url)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# define a list of possible IDs for the category label and value
value_ids = [f'{repeated_id}_ctl01_BulletedList12344025', f'{repeated_id}_ctl02_BulletedList12344025']
name_value_ids = [f'{repeated_id}_ctl01_TextBoxLabel12237001', f'{repeated_id}_ctl02_TextBoxLabel12237001']


# loop through the possible IDs until the desired elements are found
for value_id in zip( value_ids):
    category_value = soup.find('ul', {'id': value_id})
for name_id in name_value_ids:
    name_value = soup.find('span', {'id': name_id})
areas_of_interest_value = soup.find('span', {'id': f'{repeated_id}_ctl03_TextBoxLabel12221067'})
work_email_value = soup.find('span', {'id': f'{repeated_id}_ctl04_TextBoxLabel12203176'})
work_phone_value = soup.find('span', {'id': f'{repeated_id}_ctl05_TextBoxLabel12221066'})
work_address_value = soup.find('span', {'id': f'{repeated_id}_ctl06_TextBoxLabel12230379'})
regions_value = soup.find('ul', {'id': f'{repeated_id}_ctl07_BulletedList14515976'})
language_value = soup.find('ul', {'id': f'{repeated_id}_ctl08_BulletedList14856966'})
speciality_value = soup.find('ul', {'id': f'{repeated_id}_ctl04_BulletedList14533344'})
about_me_value = soup.find('span', {'id': f'{repeated_id}_ctl06_TextBoxLabel14530473'})
website_value = soup.find('span', {'id': f'{repeated_id}_ctl08_TextBoxLabel12221249'})

# create a dictionary with the extracted information
data = {"Category Listing": category_value.text.strip() if category_value else "",
        "Name": name_value.text.strip() if name_value else "",
        "Areas of Interest": areas_of_interest_value.text.strip() if areas_of_interest_value else "",
        "Work Email": work_email_value.text.strip() if work_email_value else "",
        "Work Phone": work_phone_value.text.strip() if work_phone_value else "",
        "Work Address": work_address_value.text.strip() if work_address_value else "",
        "Regions": regions_value.text.strip() if regions_value else "",
        "Language": language_value.text.strip() if language_value else "",
        "Speciality": speciality_value.text.strip() if speciality_value else "",
        "About Me": about_me_value.text.strip() if about_me_value else "",
        "Website": website_value.text.strip() if website_value else ""
       }

# save the data in a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)


# save the data in a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
