from urllib.request import urlopen
from pprint import pprint as pp

with urlopen("http://localhost:13000") as r:
#with urlopen("https://elfu.de") as r:
    print(r.url)
    print(r.code)
    print(r.headers)
    print()    
#    pp(r.read())
    print(r.read().decode('utf-8'))
