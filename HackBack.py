#!/usr/bin/env python3.4
import os
import parseLog
from modules.scanner.passive import recon
running = True
class Splash:
	def __init__(self):
		self.title = """
 _   _   ___  _____  _   ________  ___  _____  _   __
| | | | / _ \/  __ \| | / /| ___ \/ _ \/  __ \| | / /
| |_| |/ /_\ \ /  \/| |/ / | |_/ / /_\ \ /  \/| |/ / 
|  _  ||  _  | |    |    \ | ___ \  _  | |    |    \ 
| | | || | | | \__/\| |\  \| |_/ / | | | \__/\| |\  \\
\_| |_/\_| |_/\____/\_| \_/\____/\_| |_/\____/\_| \_/
"""
	def printTitle(self):
		print(self.title)
	def printMODT(self):
		print("Hack the Hacker with HackBack current feature :\n\t[-] Passive recon\n\t[-] Geoip\n\t[-] Honeypot\n\t[-] Ssh bruteforce\n\t[-] Search exploit\n")
		print('type "help" for more information')
	def clearScreen(self):
		os.system('clear')
	
def menu():
	global running
	choice = input("HackBack>")
	if "quit" in choice:
		print("Bye Bye !")
		running = False
	elif "help" in choice or "?" in choice:
		help()
	elif "show modules" in choice:
		print("\t-> modules available:")
		for modules in dict(dir(recon)):	
			print("\n\t\tNone".format(modules))	
	elif "use " in choice:
		if "shodan" in choice:
			log = parseLog.Report('/var/log/auth.log').failedPassword()
			print(log)
			for ip in log:
        			test = recon.Shodan(ip)
        			print(test.getPorts(), test.getCountry(), test.getServices())	
		else:
			print('"{}" is not available use "show modules" to see available modules'.format(choice.split("use ")[1]))
	elif "splash" in choice:
		Splash().clearScreen()
		Splash().printTitle()
		Splash().printMODT()
	elif "clear" in choice:
		os.system('clear')
	
	else:
		print('type "help" for more information')
		
def help():
	print("\t-> help : Show this menu")
	print("\t-> show modules : show available modules")
	print("\t-> use [module name] : use the specified module")
if __name__ == "__main__":
	splash = Splash()
	splash.clearScreen()
	splash.printTitle()
	splash.printMODT()
	while running:
		menu()
