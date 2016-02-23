import requests

endpoint = "http://api.giphy.com/v1/gifs/search"
payload = {"q": "cat", "api_key": "dc6zaTOxFJmzC"}

response = requests.get(endpoint, params=payload)

print response.url
print response.status_code
print response.headers["content-type"]

data =  response.json()
gif = data['data'][0]['images']['fixed_height']['url']
print gif
