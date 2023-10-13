# Takes an XML file and prints it to the terminal as JSON

import xmltodict
import json

# Specify the path to your XML file
xml_file_path = '<path-to>.xml'

# Open and read the XML file
with open(xml_file_path, 'r') as xml_file:
    # Parse the XML data using xmltodict
    data_dict = xmltodict.parse(xml_file.read())

# Convert the dictionary to JSON
json_data = json.dumps(data_dict, indent=4)

# Print the JSON data
print(json_data)
