#!/usr/bin/python3
'''task 0'''

if __name__ == '__main__':
    import urllib.request
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        r = response.read()

    print("Body response:")
    print("\t- type: {}".format(r.__class__))
    print("\t- content: {}".format(r))
    print("\t- utf8 content: {}".format(r.decode('ascii')))
