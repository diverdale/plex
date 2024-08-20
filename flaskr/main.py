import requests
import json
from pprint import pprint
from flaskr.json_parser import JsonParser


base_url = "http://192.168.2.50:32400"
recent_url = "/library/recentlyAdded?X-Plex-Token=s8z171bdCv2oYHmHTxjy"

results = requests.get(base_url + recent_url, headers = {"Accept": "application/json"} ).json()

json_data = results['MediaContainer']['Metadata']

# for item in json_data:
#     print(json.dumps(item, indent=4))
keys = ['title', 'parentTitle', 'art', 'summary', 'librarySectionTitle']

data = JsonParser(json_data, keys)

result = data.get_data()
print(json.dumps(result, indent=4))
