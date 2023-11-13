#!/usr/bin/env python3

import requests

json_url = "https://firestore.googleapis.com/v1/projects/berlayar-ai/databases/(default)/documents/credentials/api"

response = requests.get(json_url)
data = response.json()

fields_data = data.get('fields', {})

for key, value in fields_data.items():
    print(f"{key}={value['stringValue']}")

with open('./functions/.env', 'w') as env_file:
    for key, value in fields_data.items():
        env_file.write(f"{key}={value['stringValue']}\n")

print("Credentials has been added to .env file.")
