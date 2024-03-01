#!/usr/bin/python3
'''task 0: fetch data'''

if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as r:
            response = r.read()
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
