
import os
import sys
import platform
import time

#------------------[ NETWORK-CHECKER ]-------------------#

import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        pass
    except:
        print("\033[1;37m [\u001b[36m•\033[1;37m] NO NETWORK DETECTED\033[1;37m")
        exit()
connect()

#------------------[ MODULE-INSTALLER ]-------------------#

try:
	import rich , requests , bs4
except ModuleNotFoundError:
	print("\033[1;37m [\u001b[36m•\033[1;37m] MODULE ARE BEEN INSTALLED \033[1;37m")
	os.system('pip install rich --quiet && pip install requests --quiet && pip install bs4 --quiet')
except:exit()
pass

#------------------[ RUN ]-------------------#

bit = platform.architecture()[0]
print("\033[1;37m [\u001b[36m•\033[1;37m] CHECKING FOR UPDATES \033[1;37m")
os.system('git pull -q')
if bit == '32bit' :
	print("\033[1;37m [\u001b[36m•\033[1;37m] 32 BIT DETECTED\033[1;37m")
	os.system('python .RUN')
elif bit == '64bit' :
	print("\033[1;37m [\u001b[36m•\033[1;37m] 64 BIT DETECTED\033[1;37m")
	os.system('python .RUN')