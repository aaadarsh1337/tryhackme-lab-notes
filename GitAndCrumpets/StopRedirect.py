#!/usr/bin/python3

import os
import requests

url = "http://git-and-crumpets.thm/"
r = requests.get(url, allow_redirects=False)
file = open("index.html", "w")
command = "firefox " + os.path.dirname(os.path.realpath(__file__)) + "/index.html"
file.write(r.text)
file.close()
os.system(command)

"""
Simple Script To Stop That Redirect and Save the response and then open it in firefox
"""
