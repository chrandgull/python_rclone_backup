import subprocess
from os import listdir
from datetime import date
import time



def backup(backupMountPoint, rcloneBackupID, description):    
    print("Beginning backup(s) of " + description)
    
    if rcloneBackupID == "encrypt_b2_data:":
        returnCode = subprocess.run(["rclone", "--config=/root/.config/rclone/rclone.conf","--skip-links","--exclude-from","/root/exclude_from_backup.txt","--fast-list","sync",backupMountPoint,rcloneBackupID],capture_output=True,text=True)
    else:
        returnCode = subprocess.run(["rclone","--config=/root/.config/rclone/rclone.conf","--skip-links","--fast-list","sync",backupMountPoint,rcloneBackupID],capture_output=True,text=True)
   
    print("Return code of backups for: " + description + ": ", returnCode.returncode)
    
    printOutPut = returnCode.stderr
    printList = printOutPut.split("\n")
    #printList = print(returnCode.stderr.split("\n"))

    if returnCode.stderr != 0:
        print(printList)
    else:
        for line in printList:
            if not line.startswith("20"): #only get the summary from backblaze
                print(line)

#Make the summit volume is mounted

# dd/mm/YYYY

listOfFiles = listdir('/mnt/summit')

if 'backup_marker' not in listOfFiles:
    print("The remote backup directory does not seem to be mounted. (/mnt/summit)")
    exit(12)
else:
    print("Remote directory is mounted. Proceeding")


#Backup virtual machines
backup("/mnt/proxmox_backup/","encrypt_b2_virtual_machines:","Virtual Machines")

#Backup home directory
backup("/mnt/summit/Home","encrypt_b2_home:","Home Directory")

#General data
backup("/mnt/summit/Home","encrypt_b2_data:","General Data")


print("All backups complete")





















