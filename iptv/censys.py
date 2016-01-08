import sys
import json
import requests
from termcolor import colored


API_URL = ""
UID = ""
SECRET = ""

def censys(self, page=1):

	if API_URL == "":
		segale_rosso = colored ('[*]','red')
		print (segale_rosso + " require The Censys API, https://www.censys.io/api ")
	else:
		q = "Xtream Codes v1.0.59.5 Copyright 2014-2015"
		params = {'query' : q, 'page' : page}

		res = requests.post(API_URL + "/search/ipv4", json = params, auth=(UID, SECRET))
		payload = res.json()

		for r in payload['results']:
			print ("http://" + r["ip"])
