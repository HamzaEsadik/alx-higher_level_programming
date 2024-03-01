#!/usr/bin/python3
'''task 0'''
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
    response = r.read()
    print(f'''Body response:
           \n\t- type: {type(response)}
           \n\t- content: {response}
           \n\t- utf8 content: {response.decode('utf-8')}''')
