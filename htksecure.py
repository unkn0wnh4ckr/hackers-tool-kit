import os
import sys
print "--------------------------------------------------------------------------------------------------"
print """\033[93m!WELCOME TO THE SECURE VERSION OF HACKERS-TOOL-IT WHAT THIS MEANS IS THAT
THE HACKERS-TOOL-KIT WILL BE RUN WITH PROXYCHAINS MAKING YOU NEAR ANONYMOUS EXITING THE TERMINAL
SHOULD STOP THE PROXYCHAINS NOTE SOME STUFF MIGHT NOT WORK OR MIGHT BE SLOW DUE TO THE PROXYCHAINS
YOU HAVE TO HAVE YOUR PROXYCHAINS CONFIG FILE ALREADY SETUP TO USE THIS!\033[0m"""
print "--------------------------------------------------------------------------------------------------"
print "\n"
print "\033[92mWould you like to continue?     y or n\033[0m"
h = raw_input("?: ")
if h == "n":
	print "follow \033[92m@unkn0wn_bali\033[0m on instagram"
	sys.exit()
if h == "y":
	os.system("proxychains python /root/hackers-tool-kit/htk.py")
