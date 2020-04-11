#You should have a backups folder and uploaded folder and updated the config.py with your valid details before running this.

import json
import subprocess

with open('config.json') as f:
    data = json.load(f)

remote_ip = data["remoteip"]
username  = data["username"]
password  = data["password"]
file_path = data["filepath"]

no_of_files = int(subprocess.check_output("ls backups/ | wc -l",shell=True))

for x in range(no_of_files) :

    file_name = subprocess.check_output("ls backups/ | head -n 1",shell=True)

    if not subprocess.call("sshpass -p {} scp -r backups/{} {}@{}:{}".format(password,file_name,username,remote_ip,file_path).replace('\n',''),shell=True):
        subprocess.call("mv backups/{} uploaded/".format(file_name).replace('\n',''),shell=True)
        subprocess.call("echo {} has been transferred at `date` >> transfer.log".format(file_name).replace('\n','') ,shell=True)
        print('Done...\n')
    else:
        subprocess.call("echo error transferring {} at `date` >> transfer.log".format(file_name).replace('\n','') ,shell=True)
        print('Error transferring....\n')

subprocess.call("echo >> transfer.log",shell=True)        
subprocess.call("sshpass -p {} scp -r {} {}@{}:{}".format(password,"transfer.log",username,remote_ip,file_path).replace('\n',''),shell=True)
