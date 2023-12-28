import json
import requests
import sys

# Check if the file path is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: python3 ./pushdata.py <path_to_json_file>")
    print("   ex: python3 ./pushdata.py people.json")
    sys.exit(1)

# Set the path of the JSON file from the command line argument
json_file_path = sys.argv[1]

# Set the bearer token
bearer_token = 'ds1LZKoAqGMqdPKIZtsT:Vhz_HBFuM3aDS7QOF7Tln14VJJzHO7NM'

# API endpoint
url = 'https://141741533462.collect.observeinc.com/v1/http/cdp/customer_records'

# Read JSON data from the file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Set headers
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
}

# Make the POST request
response = requests.post(url, headers=headers, json=json_data)

# Check the response
if response.status_code == 200:
    print("Data successfully posted.")
else:
    print(f"Failed to post data. Status code: {response.status_code}, Response: {response.text}")
