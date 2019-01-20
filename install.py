import sys
import os

def install():
	os.system("apt update")
	os.system("pip install mechanize json whois python-whois requests bs4 requests[socks] urlparse cookielib") 
	os.system("pip install scapy datetime argparse re threading urllib2 modules builtwith smtplib")
	os.system("pip install whois")
	os.system("pip install builtwith")
	os.system("pip install colorama")
	os.system("pip install dnspython")
	os.system("pip install shodan")
	os.system("apt install python-socks -y")
	os.system("apt install nmap -y")
	os.system("apt install php -y")
	os.system("apt install perl -y")
	os.system("apt install hashcat -y")
	os.system("apt install nc")
	os.system("apt install neofetch")
	os.system("apt install cupp")
"""	os.system("cd /root/tufhub && mkdir wordlists")
	os.system("cd && git clone https://github.com/thelinuxchoice/shellphish")
	os.system("cd && git clone https://github.com/thelinuxchoice/userrecon")
	os.system("cd && git clone https://github.com/thelinuxchoice/instaspam")
	os.system("cd && git clone https://github.com/thelinuxchoice/fastssh")"""
	print "\n"
	print """entering big download region prepare you anus
	if your not ready press ctrl C """
	i = raw_input("press ctrl c to stop hit enter to continue")
	os.system("apt install metasploit-framework -y")
	os.system("cd && git clone https://github.com/trustedsec/social-engineer-toolkit")
	os.system("apt install wifite -y")
	os.system("apt install reaver -y")
	os.system("apt install aircrack-ng -y")
	os.system("cd /root/social-engineer-toolkit && pip install -r requirements.txt")
	os.system("python /root/social-engineer-toolkit/setup.py install")



print "are you running on the real kali linux os   [y/n]"
check = raw_input("[y/n]> ")
if check == "y" :
	print "ok most tools should work for you you might have to install other"
	print "things on your os for this to work if it doesnt work"
	os.system("sleep 2")
	install()

if check == "n" :
	print "then some of the tools in this script might not work"
	print "do you want to continue installation  [y/n]"
	install = raw_input("[y/n]> ")
	if install == "y" :
		def install():
			os.system("apt update")
			os.system("pip install mechanize json whois python-whois requests bs4 requests[socks] urlparse cookielib") 
			os.system("pip install scapy datetime argparse re threading urllib2 modules builtwith smtplib")
			os.system("pip install whois")
			os.system("pip install builtwith")
			os.system("apt install python-socks -y")
			os.system("apt install nmap -y")
			os.system("apt install php -y")
			os.system("apt install perl -y")
			os.system("apt install hashcat")
			os.system("apt install nc")
			os.system("apt install neofetch")
			os.system("apt install cupp")
			os.system("cd /root/tufhub && mkdir wordlists")
"""			os.system("cd && git clone https://github.com/thelinuxchoice/shellphish")
			os.system("cd && git clone https://github.com/thelinuxchoice/userrecon")
			os.system("cd && git clone https://github.com/thelinuxchoice/instaspam")
			os.system("cd && git clone https://github.com/thelinuxchoice/fastssh")"""
			print "\n"
			print """entering big download region prepare you anus
			if your not ready press ctrl C """
			i = raw_input("press ctrl c to stop hit enter to continue")
			os.system("apt install metasploit-framework -y")
			os.system("cd && git clone https://github.com/trustedsec/social-engineer-toolkit")
			os.system("apt install wifite -y")
			os.system("apt install reaver -y")
			os.system("apt install aircrack-ng -y")
			os.system("cd /root/social-engineer-toolkit && pip install -r requirements.txt")
			os.system("python /root/social-engineer-toolkit/setup.py install")

		install()
	if install == "n" :
		print "thanks for checking out my script"
		sys.exit()