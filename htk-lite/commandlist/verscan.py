#!/usr/local/bin/python
# coding: latin-1
#if you use this code give me credit @tuf_unkn0wn
#i do not give you permission to show / edit this script without my credit
#to ask questions or report a problem message me on instagram @tuf_unkn0wn
"""


 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████ ▓█████▄ 
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▒██▀ ██▌
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ░██   █▌
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ░▓█▄   ▌
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░▒████▓ 
 ▒ ▒░▒ ▒▒   ▓▒█ ░▒ ▒  ░▒ ▒▒ ▓▒ ▒░ ░ ▒▒▓  ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░ ░ ▒  ▒ 
 ░   ░  ░   ▒   ░        ░  ░    ░    ░ ░  ░ 
 ░  ░  ░      ░   ░      ░  ░      ░  ░   ░    
                  ░                       ░      


"""
import os
import sys
import random
lred = '\033[91m'
lblue = '\033[94m'
lgreen = '\033[92m'
yellow = '\033[93m'
cyan = '\033[1;36m'
purple = '\033[95m'
red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
orange = '\033[33m'

colorlist = [red, blue, green, yellow, lblue, purple, cyan, lred, lgreen, orange]
randomcolor = random.choice(colorlist)
banner3list = [red, blue, green, purple]

def verscan():
	print """
Services available:

{0}ssh

{1}mysql
\033[0m
	""".format(random.choice(colorlist), random.choice(colorlist))
	try:
		service = raw_input("\033[1mService: \033[0m")
		if service == "ssh":
			f = raw_input(G+"\033[1mTarget: \033[0m")
			g = raw_input(G+"\033[1mPort: \033[0m")
			t = raw_input(G+"\033[1mThreads: \033[0m")
			b = raw_input(G+"\033[1mTimeout: \033[0m")
			os.system('echo "use auxiliary/scanner/ssh/ssh_version\n" >> sshver.rc')
			os.system('echo "set RHOSTS {0}\n" >> sshver.rc'.format(f))
			os.system('echo "set RPORT {0}\n" >> sshver.rc'.format(g))
			os.system('echo "set THREADS {0}\n" >> sshver.rc'.format(t))
			os.system('echo "set TIMEOUT {0}\n" >> sshver.rc'.format(b))
			os.system('echo "show options\n" >> sshver.rc')
			os.system('echo "run\n" >> sshver.rc')
			os.system('echo "exit\n" >> sshver.rc')
			os.system("service postgresql restart")
			os.system('msfconsole -q -r sshver.rc')
			os.system('rm -rf sshver.rc')

		if service == "mysql":
			f = raw_input(G+"\033[1mTarget: \033[0m")
			g = raw_input(G+"\033[1mPort: \033[0m")
			t = raw_input(G+"\033[1mThreads: \033[0m")
			os.system('echo "use auxiliary/scanner/mysql/mysql_version\n" >> mysqlv.rc')
			os.system('echo "set RHOSTS {0}\n" >> mysqlv.rc'.format(f))
			os.system('echo "set RPORT {0}\n" >> mysqlv.rc'.format(g))
			os.system('echo "set THREADS {0}\n" >> mysqlv.rc'.format(t))
			os.system('echo "show options\n" >> mysqlv.rc')
			os.system('echo "run\n" >> mysqlv.rc')
			os.system('echo "exit\n" >> mysqlv.rc')
			os.system("service postgresql restart")
			os.system('msfconsole -q -r mysqlv.rc')
			os.system('rm -rf mysqlv.rc')
	except:
		print "\n"
verscan()
