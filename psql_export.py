#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
import time
from time import gmtime, strftime

args = sys.argv[1:]
if not args:
    print('Usage is: [--db username][--db password][--database_name][--directory_path]')
    sys.exit(1)
            
if len(args) != 4:
    print('Error. Some arguments are missing\nUsage is: [--db username][--db password][--database_name][--directory_path]')
    sys.exit(1)
else:    
    dbuser = args[0]
    dbpass = args[1]
    dbname = args[2]
    path = args[3]
    #del args[1:] 
        
# Logging info
startTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print('Dump started @ '+ startTime)

# Settings
#dbuser = ''
#dbpass = ''
#dbname = ''
#path = ''
os.chdir(path)
e=['_scheme.sql', '_data.sql']
psql = ['pg_dump --format plain --encoding UTF8 --schema-only -U ' , 'pg_dump --data-only -U ']

# Running pure dump
os.system ( psql[0]  + dbuser +  ' -d ' + dbname + ' > ' + dbname + e[0])
os.system ( psql[1]  + args[0] +  ' -d ' + args[2] + ' > ' + args[2] + e[1])    
print('Dump finised')

