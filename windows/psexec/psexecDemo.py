import subprocess

# command = 'python D:/attrobot3/Scripts/psexec.py Administrator:admin@192.168.168.93 "net stop IxiaEndpoint"'
# command = 'python D:/attrobot3/Scripts/psexec.py Administrator:admin@192.168.168.93 "python D:/demo.py"'
command = 'python D:/attrobot3/Scripts/wmiexec.py Administrator:admin@192.168.168.93 "python D:/demo.py"'
p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
print(p.read().decode('utf-8'))


