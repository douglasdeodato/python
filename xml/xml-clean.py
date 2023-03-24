import xml.etree.ElementTree as ET

# Load the XML file
xml_file = 'sitemap.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

# Remove all extra whitespace and indentation
for elem in root.iter():
    elem.tail = None
    elem.text = elem.text.strip() if elem.text else None

# Write the formatted XML to a new file
formatted_xml_file = 'sitemap-clean.xml'
tree.write(formatted_xml_file, encoding='utf-8', xml_declaration=True)
