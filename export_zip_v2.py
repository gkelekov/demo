import os
import sys
import glob
import logging
import time
from time import gmtime, strftime
import zipfile

# Setting path and switch to path direcotry
path = ('c:\\Temp\\testing\\')
os.chdir(path)
db = ['cinder', 'cinder', 'cinder']   #db = ['username', 'password', 'database_name']
cname = ('unified_event')  # common name for tables
num=('10001', '10002', '10008') # number in table names
e=['.csv', '.zip'] # type of files

# Logging info
startTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
logging.basicConfig(filename='extract.log',level=logging.INFO)
logging.info('-------------------------------------------------------')
logging.info(' Starting backup procedure @ '+ startTime)
logging.info('-------------------------------------------------------')
logging.info ('Setting working directory: '+ path)

# Setting proper day of year
doy = time.localtime().tm_yday
rdoy = int (doy)-1
logging.info ('Setting doy for yesterday: '+ str(rdoy))

# Table naming
cnt = str(rdoy)
t=[cname + '_' + num[0] + '_' + cnt, cname + '_' + num[1] + '_'+ cnt, cname + '_' + num[2] + '_'+ cnt]
logging.info ('Setting table names...')

# Running queris
psql = 'psql -P format=unaligned -P tuples_only -P fieldsep="|" -c "select * from data_part.' # raw psql 

os.system ( psql + t[0] + '" > ' + t[0] + e[0] + ' -U ' + db[0] + ' -d ' + db[2] )  
logging.info('Extracted and created ' + t[0] + e[0] + ' file.')

os.system ( psql + t[1] + '" > ' + t[1] + e[0] + ' -U ' + db[0] + ' -d ' + db[2] )  
logging.info('Extracted and created ' + t[1] + e[0] + ' file.')

os.system ( psql + t[2] + '" > ' + t[2] + e[0] + ' -U ' + db[0] + ' -d ' + db[2] )  
logging.info('Extracted and created ' + t[2] + e[0] + ' file.')

# Zipping
zip = zipfile.ZipFile(str(t[0] + e[1]), 'w')
zip.write(str(path + t[0] + e[0]), compress_type=zipfile.ZIP_DEFLATED)
logging.info('Extracted file ' + t[0] + e[0] + ' file zipped.')
zip = zipfile.ZipFile(str(t[1] + e[1]), 'w')
zip.write(str(path + t[1] + e[0]), compress_type=zipfile.ZIP_DEFLATED)
logging.info('Extracted file ' + t[1] + e[0] + ' file zipped.')
zip = zipfile.ZipFile(str(t[2] + e[1]), 'w')
zip.write(str(path + t[2] + e[0]), compress_type=zipfile.ZIP_DEFLATED)
logging.info('Extracted file ' + t[2] + e[0] + ' file zipped.')

zip.close()

# Delete old csv files
logging.info('Deleting non zipped files.')
for r in glob.glob ("unified_event_*.csv"):
    os.remove(r)
    
logging.info('Deleting done.')

endTime=strftime("%Y-%m-%d %H:%M:%S", gmtime())

logging.info('-------------------------------------------------------')
logging.info(' Process complete @ ' + endTime )
logging.info('-------------------------------------------------------')







