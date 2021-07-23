import requests

data = {
  'command': 'Hi'
}

response = requests.post('http://chillhack.thm/secret/', data=data)
print(response.text)
