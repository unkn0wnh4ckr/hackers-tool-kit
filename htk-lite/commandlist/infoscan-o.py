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
def specscan():
	print """\033[1m
Scans Available:\033[0m

1:  simple nmap portscan

2:  show document info of target with curl
 
3:  nmap OS detection, version detection, script scanning, and traceroute scan

4:  nmap dns bruteforce

5:  get a hosts ip address

6:  check if a host is online

7:  who-is lookup

8:  dns-lookup

9:  get a hosts source code

10: web application firewall scanner

11: run a ssl scan

12: find the location of a ip address

13: reverse ip lookup

14: host search

15: reverse dns 

16: find shared dns

17: cloudflare bypass

18: sslscan

19: directory scan / bruteforce

20: nikto scan [this might take awhile to finish]

go back: go back to main menu

	"""
	print "Type a number then your target   Ex: 5 www.pornhub.com\n"
	j = False
	while not j:
		try:
			option, target = raw_input("\033[1mScan:\033[0m ").split()
			if option == "1":
				os.system("nmap {0}".format(target))
			if option == "2":
				os.system("curl -I {0}".format(target))
			if option == "3":
				os.system("nmap -A {0}".format(target))
			if option == "4":
				os.system("nmap --script dns-brute {0}".format(target))
			if option == "5":
				ip = socket.gethostbyname(target)
				print """
		Host: {0}
		IP: {1}
				""".format(target, ip)
			if option == "6":
				ht = raw_input("\033[1mHTTP or HTTPS:\033[0m ")
				if ht == "https":
					targetht = "https://"
				if ht == "http":
					targetht = "http://"
				request = requests.get(targetht + target)
				http = request.status_code
				if http == 200:
					print("\nServer: [\033[32monline\033[0m]")
				else:
					print("\nServer: [\033[31moffline\033[0m]")
			if option == "7":
				whois = requests.get("https://api.hackertarget.com/whois/?q=" + target).content.decode("UTF-8")
				print(whois)
			if option == "8":
				os.system("curl https://api.hackertarget.com/dnslookup/?q={0}".format(target))
			if option == "9":
				os.system("curl {0}".format(target))
			if option == "10":
				os.system("wafw00f {0}".format(target))
			if option == "11":
				os.system("sslscan {0}".format(target))
			if option == "12":
				os.system("curl https://api.hackertarget.com/geoip/?q={0}".format(target))
			if option == "13":
				os.system("curl https://api.hackertarget.com/reverseiplookup/?q={0}".format(target))
			if option == "14":
				os.system("curl https://api.hackertarget.com/hostsearch/?q={0}".format(target))
			if option == "15":
				os.system("curl https://api.hackertarget.com/reversedns/?q={0}".format(target))
			if option == "16":
				os.system("curl https://api.hackertarget.com/findshareddns/?q={0}".format(target))
			if option == "17":
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
			if option == "18":
					a = 'sslscan {0}'.format(target)
					os.system(a)
			if option == "19":
				ht = raw_input("HTTP or HTTPS: ")
				if ht == "https":
					targetht = "https://"
				if ht == "http":
					targetht = "http://"
				a = 'dirb {0}{1}/'.format(targetht,target)
				os.system(a)
			if option == "20":
				port = raw_input("\033[1mPort:\033[0m ")
				os.system("nikto -h {0} -p {1}".format(target,port))
			if target == "back":
				break
		except:
			print "\n"
			break
	j = True
specscan()
