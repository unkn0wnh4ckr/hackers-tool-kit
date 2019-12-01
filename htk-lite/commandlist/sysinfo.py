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

def sysinfo():
	os.system("iwconfig")
	k = raw_input("\033[1mInterface:\033[0m ")
	os.system("clear")
	os.system("ifconfig")
	print "\n"
	os.system("iwconfig")
	print "\n"
	os.system("neofetch")
	print "\n"
	gw = os.popen("ip -4 route show default").read().split()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	gateway = gw[2]
	host = socket.gethostname()
	print (" IP: ", ipaddr, " Gateway: ", gateway, " Host: ", host)
	print "\n        Router IP"
	print "----------------------------\033[92m"
	os.system('curl "http://myexternalip.com/raw"')
	print "\n\033[0m----------------------------"
	print "\n"
	show = 'macchanger -s {0}'.format(k)
	os.system(show)
	os.system("uname -a")
	os.system("whoami")
sysinfo()
