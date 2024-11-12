import csv

import paramiko as paramiko
from utilities.configurations import *

# connection needs IPaddress, Port, username, password
username = getConfig()['Server']['username']
password = getConfig()['Server']['password']
host = getConfig()['Server']['host']
port = getConfig()['Server']['port']
key = paramiko.RSAKey.from_private_key_file(getConfig()['Server']['key_path'])

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, pkey=key)

# Run Commands
#stdin, stdout, stderr = ssh.exec_command('ls -a')
stdin, stdout, stderr = ssh.exec_command('cat demofile')
result = stdout.readlines()
print(result)
print(result[1])

#Upload files
sftp = ssh.open_sftp()
destinationPath = "script.py" # no relative path is mention, it will be placed on home
localPath = "batchFiles/script.py"
sftp.put(localPath, destinationPath)

destinationPath = "loanasa.csv"
localPath = "batchFiles/loanasa.csv"
sftp.put(localPath, destinationPath)

#Trigger the batch commands
ssh.exec_command('python3 script.py')

#Download the file to your local
sftp.get('loanasa.csv', 'outputFiles/loanasa.csv')

# Parse Output file csv
with open('outputFiles/loanasa.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        if row[0] == '32321':
            assert row[1] == 'rejected'
ssh.close()
