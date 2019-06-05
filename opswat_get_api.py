import requests
sha256hash = '441f2a6775621af8c5d1ead7082e9573ad878bc90675ed55f86abfc8a9e8cc6f'
url = "https://api.metadefender.com/v4/hash/"+sha256hash
headers = {
    'apikey': "af950d69e443d7da681eddf12d4e4849"
    }
response = requests.request("GET", url, headers=headers)
print(response.text)

