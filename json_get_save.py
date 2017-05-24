#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import glob
import wget
import json
import requests

path = ('c:\\Temp\\')
filename = ('json.txt')
outfile = (path + filename) 
os.chdir(path)

'''super url za testiranje jsona: https://jsonplaceholder.typicode.com'''

url='https://jsonplaceholder.typicode.com/photos'
'''url = 'http://md5.jsontest.com/?text=goran_kelekovic' # simple md5 hash generator '''

import requests
r = requests.get(url)
content=r.json()

''' # wget solution
fs = wget.download(url)
with open(fs, 'r') as f:
  content = f.read()
print(content)
'''

with open(outfile, 'w') as out:
  json.dump(content, out, indent=4)

''' # clenaup if using wget solution
for r in glob.glob ("*.wget"): 
  os.remove(r)