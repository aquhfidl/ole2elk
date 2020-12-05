import socket
import os
import subprocess
import requests
import json
from pygrok import Grok



home_dir = '/opt/evedence/'


olescan = []

list_file = os.listdir(home_dir)
print(list_file)


#run ole
for i in list_file:
	tmp = 'file ' + home_dir + i


#check all files
#for i in list_file:
#	tmp = 'file ' + home_dir + i
#	#print(tmp)
#	file = subprocess.check_output(tmp.split(), universal_newlines=True)
#	print()
#	print("rez:")
#	print(file)
#	print()