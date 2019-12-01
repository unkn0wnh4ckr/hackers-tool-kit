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

def netscan():
	print """
{0}1: scan for devices in your network

{1}2: scan for networks around you
\033[0m
go back: go back to main menu
	""".format(random.choice(colorlist), random.choice(colorlist))
	try:
		choice = raw_input("\033[1mScan:\033[0m ")

		if choice == "1":
			os.system("netdiscover")
		if choice == "2":
			os.system("iwconfig")
			m = raw_input("\033[1mSelect Interface:\033[0m ")
			os.system("airmon-ng start " + m)
			print Y+"WOULD YOU LIKE TO SAVE YOUR SCAN RESULTS?\033[0m"
			j = raw_input("\033[1m[y/n]>\033[0m ")
			if j == "y":
				os.system("airodump-ng -w /root/SCAN " + m)
				print Y+"! SCAN RESULTS SAVED IN /root/ DIRECTORY !\033[0m"
			if j == "n":
				os.system("airodump-ng " + m)
			os.system("airmon-ng stop " + i)
		if choice == "go back":
			os.system("")
	except:
		print "\n"
netscan()
