import json
import os

with open('config.json') as f:
	data = json.load(f)

rip = data["remoteip"]
uname = data["username"]
pword = data["password"]
fpath = data["filepath"]

if not os.system("sshpass -p "+pword+" scp -r backups/* "+uname+"@"+rip+":"+fpath) :
  os.system("mv backups/* uploaded/")
  print "Done..."+"\n"
else:
  print "Error transferring...."+"\n"  
