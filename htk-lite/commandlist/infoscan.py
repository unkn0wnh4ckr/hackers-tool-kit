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

def infoscan():
	try:
		target = raw_input("\033[1mTarget:\033[0m ")
		port = raw_input("\033[1mPort:\033[0m ")
		print "\033[93m! HTTP OR HTTPS !\033[0m\n"
		ht = raw_input("[https/http]: ")
		if ht == "http":
			targetht = 'http://'
		if ht == "https":
			targetht = 'https://'
		print "\033[31m-----\033[33m-----\033[93m-----\033[32m-----\033[1;36m-----\033[94m-----\033[95m-----\033[31m-----\033[33m-----\033[93m-----\033[32m-----\033[1;36m-----\033[94m-----\033[95m-----\033[0m\n"
		os.system("curl {0}".format(target))
		print "\n"
		ip = socket.gethostbyname(target)
		print G+"------------------------\033[0m"
		print N+"\033[1mHost:\033[32m ", target
		print N+"\033[1mIP:\033[32m ", ip
		print G+"------------------------\033[0m"
		os.system("curl -I {0}".format(target))
		print "\n"
		request = requests.get(targetht + target)
		http = request.status_code
		if http == 200:
			print("\nServer: [\033[32monline\033[0m]")
		else:
			print("\nServer: [\033[31moffline\033[0m]")
			exit()
		print "\n"
		whois = requests.get("https://api.hackertarget.com/whois/?q=" + target).content.decode("UTF-8")
		print(whois)
		print "\n"
		os.system("curl https://api.hackertarget.com/dnslookup/?q={0}".format(target))
		print "\n"
		os.system("wafw00f {0}".format(target))
		print "\n"
		os.system("sslscan {0}".format(target))
		print "\n"
		os.system("curl https://api.hackertarget.com/geoip/?q={0}".format(target))
		print "\n"
		os.system("curl https://api.hackertarget.com/reverseiplookup/?q={0}".format(target))
		print "\n"
		os.system("curl https://api.hackertarget.com/hostsearch/?q={0}".format(target))
		print "\n"
		os.system("curl https://api.hackertarget.com/reversedns/?q={0}".format(target))
		print "\n"
		os.system("curl https://api.hackertarget.com/findshareddns/?q={0}".format(target))
		print "\n"
		def daf():
		     subdomainlist = ["ftp", "cpanel", "webmail", "localhost", "local", "mysql", "forum", "driect-connect", "blog",
		                         "vb", "forums", "home", "direct", "forums", "mail", "access", "admin", "administrator",
		                         "email", "downloads", "ssh", "owa", "bbs", "webmin", "paralel", "parallels", "www0", "www",
		                         "www1", "www2", "www3", "www4", "www5", "shop", "api", "blogs", "test", "mx1", "cdn", "mysql",
		                         "mail1", "secure", "server", "ns1", "ns2", "smtp", "vpn", "m", "mail2", "postal", "support",
		                         "web", "dev"]
		
		     for sublist in subdomainlist:
		         try:
		             hosts = str(sublist) + "." + str(target)
		             showip = socket.gethostbyname(str(hosts))
		             print "\033[0m\033[32mHIT\033[0m:\033[1m " + str(showip) + ' | ' + str(hosts)
		         except:
		             print "\033[0mBypassing..."
		
		daf()
		print "\033[0m"
		print "\n"
		os.system("nmap -A {0}".format(target))
		print "\n"
		os.system("nmap --script dns-brute {0}".format(target))
		print "\n"
		a = 'dirb {0}{1}/'.format(targetht,target)
		os.system(a)
		print "\n"
		os.system("nikto -h {0} -p {1}".format(target,port))
		print "\n\033[31m-----\033[33m-----\033[93m-----\033[32m-----\033[1;36m-----\033[94m-----\033[95m-----\033[31m-----\033[33m-----\033[93m-----\033[32m-----\033[1;36m-----\033[94m-----\033[95m-----\033[0m"
	except:
		print "\033[91mError Something Went Wrong Maybe The Specified Target Is Not Available\033[0m"
infoscan()
