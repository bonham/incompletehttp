from urllib.request import urlopen, build_opener, HTTPDefaultErrorHandler
from pprint import pprint as pp

#opener = build_opener(HTTPDefaultErrorHandler)
#with opener.open("http://localhost:9999") as r:

with urlopen("http://localhost:9999") as r:
#with urlopen("https://elfu.de") as r:
    print(r.url)
    print(r.code)
    print(r.headers)
    print()    
#    pp(r.read())
    print(r.read().decode('utf-8'))
