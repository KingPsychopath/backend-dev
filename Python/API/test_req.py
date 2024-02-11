import requests
import json

response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

#print(response.json()) # print the full response in json format
#print(response.json()['items']) # print the items in the response#

# Consuming an API using requests
for data in response.json()['items']:
    print(data['title'])
    print(data['link'])
    print(data['owner']['display_name'])
    print(data['owner']['link'])
    print('----------------------------------------------')