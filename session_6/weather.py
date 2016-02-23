import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units": "metric", "appid": "44db6a862fba0b067b1930da0d769e98"}

response = requests.get(endpoint, params=payload)

print response.url
print response.status_code
print response.headers["content-type"]

#print response.text
data =  response.json()
temperature = data['main']['temp']
name = data["name"]
weather = data['weather'][0]['main']

print u"It's {}C in {}, and the sky is {}".format(temperature,name,weather)
