#!/usr/bin/python3
'''task 1: print X-Request-Id'''

if __name__ == "__main__":
    import sys
    import urllib.request
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    with urllib.request.urlopen(url, data) as response:
        print(f"Your email is: {response.read()}")
