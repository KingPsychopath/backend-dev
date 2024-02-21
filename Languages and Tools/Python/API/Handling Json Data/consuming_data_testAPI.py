import requests
import json

response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

#print(response.json()) # print the full response in json format
#print(response.json()['items']) # print the items in the response#

for data in response.json()['items']:
    print(data['title'])
    print(data['link'])
    print(data['owner']['display_name'])
    print(data['owner']['link'])
    print('----------------------------------------------')


# Using inbuilt url library to parse the response
import urllib.request

url = 'http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow'
with urllib.request.urlopen(url) as response:
    data = response.read()
    dict_obj = json.loads(data)

for item in dict_obj['items']:
    print(item['title'])
    print(item['link'])
    print(item['owner']['display_name'])
    print(item['owner']['link'])
    print('----------------------------------------------')
