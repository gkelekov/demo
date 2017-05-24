#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
import subprocess
import time
import re
import pandas as pd

filename = ('c:\\Temp\\infile.log')
tempfile = ('c:\\Temp\\tempfile.txt') 
outfile = ('c:\\Temp\\outfile.txt') 

type = ['WARNING', 'INFO', 'LOG', 'ERROR']

def matchDate(line): # funkcija koja radi provjeru timestamp-a (19 chars) ba početku svakog redka
    matchThis = ""
    matched = re.match(r'\d\d\d\d-\d\d-\d\d\ \d\d:\d\d:\d\d',line)
    if matched:            
        matchThis = matched.group()  #matching datuma 
    else:
        matchThis = "NONE"
    return matchThis

def parseString(row): # funkcija koja gleda da li ima iz "type" liste itema
    for item in type:  
        if item in row:
            return(item)

def newDict(dic): # funkcija koja radi dictionary iz dobivenih podataka i radi split po tri određena tipa podataka
    currentDict = {}
    for line in dic:
        if line.startswith(matchDate(line)):
            if currentDict:
                yield currentDict
            currentDict = {'date':line.split("__")[0][:19],'type': parseString(line),'text':line.split(": ",5)[-1]}
        else:
            currentDict["text"] += line
    yield currentDict

with open(filename) as x:
    listNew = list(newDict(x))
    #print(listNew)

# Export via pandas
export = pd.DataFrame(listNew, columns=['date', 'type', 'text'])
export.to_csv(tempfile, index=False, header=False, sep='-')

def clean(): # funkcija koja radi mali cleanup loga - ovo bi deff trebalo proširiti da se log još bolje formatira ili koristiti os.system sed ili awk
    rf = open(tempfile)
    wf = open(outfile,"w")
    for line in rf:
        nline = line.rstrip('\n"')
        newline = nline.strip('"')
        wf.write(newline)
        wf.write('\n')  # remove to leave out line breaks
    rf.close()
    wf.close()
clean()
