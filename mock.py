# This is a Mock project for DevOps class

# Python-Paramiko (Module)
# SSH client online
# Python-OS (Module)	- create directory
# 	


import paramiko
import requests


url = 'http://www.google.com'
loc='/home/index.html'

def google(url,loc):
	
	r=requests.get(url)
	#print r.status_code
	file=open(loc, 'wb')
	o=r.status_code
	for output in r.iter_content():
		if o == 200:
			file.write(output)
		else:
			print "Code Faulty"
			return

google(url,loc)

def clt():
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect( '192.168.0.13' , username='ahsan', password='ahsankhan')
	ins, out, err = ssh.exec_command("mkdir /opt/google ; cd /opt/google " )
	
	e=err.read()
	if e == []:
		print "Permission is good"
	else:
		print e
	
clt()


