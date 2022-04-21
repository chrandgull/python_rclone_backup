# Rclone Backup Script

This is a small python script that invokes rclone to backup a local or remote directory to Backblaze B2.

## Getting started

Create your [rclone](https://rclone.org/) remotes as described in the [rclone documentation](https://rclone.org/docs/).

Create a blank file named 'backup_marker' in the root directory containing the sub directories you want to back up. This is a easy/cheap way to make sure the directory is mounted and accessible before starting the backup. 

`touch backup_marker`

## Purpose

This runs rclone commands sequentially, captures the return code, and prints the status to stdout.

### Sucessful run output

`Remote directory is mounted. Proceeding`

`Beginning backup(s) of Virtual Machines`

`Return code of backups for: Virtual Machines:  0`


`Beginning backup(s) of Home Directory`

`Return code of backups for: Home Directory:  0`


`Beginning backup(s) of General Data`

`Return code of backups for: General Data:  0`

`All backups complete`


## Adding directories and remotes 

At the bottom of the script, prior to the last line, add the following where:

**Operand 1** is a local or remote directory directory on your linux machine. (/mnt/proxmox_backup)

**Operand 2** is the name of the remote in your rclone config file (encrypt_b2_virtual_machines)

**Operand 3** is a general description for printing to standard output during runtime. (Virtual Machines)

### Example
`backup("/mnt/proxmox_backup/","encrypt_b2_virtual_machines:","Virtual Machines")`


## Adding the script to crontab


MAILTO="your_email_address@domain.com"              <- Change as needed

SHELL=/bin/bash                                     <- Change as needed

HOME=/root                                          <- Change as needed

0 5 * * * python3 /root/python_rclone.py            <- Run every day at 05:00 UTC

[Crontab generator](https://crontab-generator.org/) can be used to generate crontab entries.
