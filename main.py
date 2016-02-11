# -*- coding: utf-8 -*-
from config import *

import json

from httpHelpers import *

ips = [
		'82.16.20.9',
'149.254.56.139',
'77.102.78.62',
'2.223.49.117',
'188.29.164.170',
'188.29.165.134',
'90.194.188.196',
'213.205.251.89',
'109.73.65.224',
'213.205.251.22',
'5.80.238.184',
'149.254.56.94',
'85.255.233.124',
'5.80.239.51',
'109.144.182.142',
'86.134.29.165',
'213.205.251.103',
'86.145.133.157',
'90.202.101.38',
'109.153.49.164',
'213.205.199.19',
'213.205.199.6',
'31.55.88.89',
'212.183.140.1',
'86.187.188.142',
'109.144.156.190',
'31.55.100.165',
'31.48.144.235',
'5.80.239.51',
'149.254.56.6',
'81.141.12.58',
'94.196.227.64'
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




