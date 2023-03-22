import re
from bs4 import BeautifulSoup
import requests
import json

# Load the URL from a JSON file
with open('config.json') as f:
    config = json.load(f)
url = config['url']

# Step 1: Sort the table rows alphabetically by name and write to a file called "sorted_table.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'cellpadding': '0', 'cellspacing': '0', 'width': '594'})
rows = table.find_all('tr')[1:]  # exclude the header row
rows.sort(key=lambda row: row.find_all('td')[1].get_text().strip())

table_html = f'<table>\n<tr>{"".join(str(cell).strip() for cell in rows[0].find_all("td"))}</tr>\n'
for row in rows[1:]:
    table_html += f'<tr>{"".join(str(cell).strip() for cell in row.find_all("td"))}</tr>\n'
table_html += '</table>'

with open('sorted_table.html', 'w') as f:
    f.write(table_html.strip())

# Create a new HTML file called "clean-html" with headers for each letter
with open('sorted_table.html', 'r') as f:
    sorted_table_html = f.read()

letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
clean_html = ''
for letter in letters:
    rows_with_letter = [row for row in rows if row.find_all('td')[1].get_text().startswith(letter)]
    if rows_with_letter:
        clean_html += f'<h2>{letter}</h2>\n'
        clean_html += '<table>\n'
        for row in rows_with_letter:
            cells = row.find_all("td")[1:]  # exclude the first cell
            profile_id = cells[1].a["href"].rsplit('/', 1)[-1]
            clean_html += "<tr>"
            clean_html += f'<td class="name">{cells[0].get_text()}</td>'
            for cell in cells[2:]:
                clean_html += str(cell).strip()
            clean_html += f'<td class="profile-link" id="{profile_id}"><a href="https://iahip.org{cells[1].a["href"]}"><button>View Profile</button></a></td>'
            clean_html += "</tr>\n"
        clean_html += '</table>\n'


# Remove <font> tags with style attribute and font-size: 16px
clean_html = re.sub(r'<font .*?style="font-size: 16px;".*?>', '', clean_html)

# Remove </font> tags
clean_html = re.sub(r'</font>', '', clean_html)

# Add class to td element containing "MIAHIP" for better SEO
clean_html = re.sub(r'<td>(MIAHIP)</td>', r'<td class="certification">\1</td>', clean_html)

# Write formatted table code to file
with open('clean-html.html', 'w') as f:
    f.write('<html>\n<head>\n')
    f.write('<link rel="stylesheet" type="text/css" href="style.css">\n')
    f.write('</head>\n<body>\n')
    f.write(clean_html.strip())
    f.write('\n</body>\n</html>')
