# -*- coding: utf-8 -*-
from config import *

import json

from httpHelpers import *

ips = [
'128.0.0.1'
]

URLSTUB = BASEURL + "addrinfo?api_key=" + API_KEY 
for ip in ips:
	url = URLSTUB + "&addr=" + ip
	response = openUrl(url, data = None, headers = None)
	response_dict = json.loads(response.read())
	if not response_dict.has_key('error'):
		print(response_dict['address'] + " " + response_dict['city'])
	else: 
		print ("ERROR: " + ip + " " + response_dict['error'] )




