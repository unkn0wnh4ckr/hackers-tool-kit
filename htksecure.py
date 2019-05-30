import os
import sys
print "--------------------------------------------------------------------------------------------------"
print """\033[93m!WELCOME TO THE SECURE VERSION OF HACKERS-TOOL-IT WHAT THIS MEANS IS THAT
THE HACKERS-TOOL-KIT WILL BE RUN WITH PROXYCHAINS AND OTHER TOOLS MAKING YOU NEAR ANONYMOUS EXITING 
THE TERMINAL SHOULD STOP THE PROXYCHAINS NOTE SOME STUFF MIGHT NOT WORK OR MIGHT BE SLOW DUE TO THE
PROXYCHAINS YOU HAVE TO HAVE YOUR PROXYCHAINS CONFIG FILE ALREADY SETUP TO USE THIS!\033[0m"""
print "--------------------------------------------------------------------------------------------------"
print "\n"
print "\033[92mWould you like to continue?     y or n\033[0m"
h = raw_input("?: ")
if h == "n":
	print "follow \033[92m@tuf_unkn0wn\033[0m on instagram"
	sys.exit()
if h == "y":
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
	print "\nSTARTING HTK WITH PROXYCHAINS\n"
	os.system("proxychains python /root/hackers-tool-kit/htk.py")
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
