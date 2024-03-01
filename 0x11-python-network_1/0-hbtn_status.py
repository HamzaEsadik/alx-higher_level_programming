#!/usr/bin/python3
'''task 0: fetch data'''

if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as r:
        response = r.read()
        print(f'''Body response:
            \n\t- type: {response.__class__}
            \n\t- content: {response}
            \n\t- utf8 content: {response.decode('utf-8')}''')
