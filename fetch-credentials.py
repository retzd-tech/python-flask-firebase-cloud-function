#!/usr/bin/env python3

import requests

# Replace 'YOUR_JSON_URL' with the actual URL of the JSON data
json_url = "https://firestore.googleapis.com/v1/projects/berlayar-ai/databases/(default)/documents/credentials/api"

# Fetch JSON data from the URL
response = requests.get(json_url)
data = response.json()

# Extract the list of data objects inside the fields object
fields_data = data.get('fields', {})

# Print the list of data objects
for key, value in fields_data.items():
    print(f"{key}={value['stringValue']}")

with open('./functions/.env', 'w') as env_file:
    for key, value in fields_data.items():
        env_file.write(f"{key}={value['stringValue']}\n")

print("Credentials has been added to .env file.")
