import requests

url = "http://127.0.0.1:5500/test.html"
response = requests.get(url)
print(response.text)