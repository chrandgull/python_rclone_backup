import subprocess
from os import listdir

#Make the summit volume is mounted

listOfFiles = listdir('/mnt/summit')

if 'backup_marker' not in listOfFiles:
    print("The remote backup directory does not seem to be mounted. (/mnt/summit)")
    exit(12)
else:
    print("Remote directory is mounted. Proceeding")


print("Beginning backups of virtual machines")
returnCode = subprocess.run(["rclone","--dry-run","--fast-list","sync","/mnt/proxmox_backup/","encrypt_b2_virtual_machines:"],capture_output=True,text=True)
print("Return code of VM backups() : ", returnCode.returncode)

printOutPut = returnCode.stderr 

print(printOutPut)

#printList = printOutPut.split("\n")




















