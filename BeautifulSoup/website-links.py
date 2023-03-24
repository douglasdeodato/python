from requests_html import HTMLSession
from collections import Counter
from urllib.parse import urlparse

session = HTMLSession()
r = session.get("website here")
unique_netlocs = Counter(urlparse(link).netloc for link in r.html.absolute_links)
for link in unique_netlocs:
    print(link, unique_netlocs[link])