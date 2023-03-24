import xml.etree.ElementTree as ET
from xml.dom import minidom

# Parse the XML document
tree = ET.parse('sitemap.xml')
root = tree.getroot()

# Create a pretty-printed string of the XML document
xml_str = ET.tostring(root, encoding='unicode', method='xml')
pretty_xml = minidom.parseString(xml_str).toprettyxml(indent='')

# Remove unnecessary newlines and whitespace
pretty_xml = '\n'.join([line for line in pretty_xml.split('\n') if line.strip()])

# Write the formatted XML to a new file
formatted_xml_file = 'sitemap-clean.xml'
with open(formatted_xml_file, 'w') as f:
    f.write(pretty_xml)
