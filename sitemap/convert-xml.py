import re
from bs4 import BeautifulSoup
from datetime import datetime

# Read the clean-html.html file
with open('clean-html.html', 'r') as f:
    clean_html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(clean_html, 'html.parser')

# Find all the profile links
profile_links = soup.find_all('a', href=True)

# Generate the sitemap XML
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'

for link in profile_links:
    url = link['href']
    profile_id = url.rsplit('/', 1)[-1]

    # Add the URL to the sitemap XML
    sitemap_xml += '<url>\n'
    sitemap_xml += f'<loc>{url}</loc>\n'
    
    current_date = datetime.now().strftime('%Y-%m-%d')
    sitemap_xml += f'<lastmod>{current_date}</lastmod>\n'
    
    sitemap_xml += '<changefreq>weekly</changefreq>\n'
    sitemap_xml += '<priority>0.5</priority>\n'
    sitemap_xml += '</url>\n'

sitemap_xml += '</urlset>\n'

# Write the sitemap XML to a file
with open('sitemap.xml', 'w') as f:
    f.write(sitemap_xml)
