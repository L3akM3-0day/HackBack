#!/usr/bin/env python3.4
import urllib.request
import sys
class Report():
	def __init__(self,log_path):
		self.log_path = log_path
	def failedPassword(self):
		self.IP = []
		users = []
		with open(self.log_path,"rt") as f:
			log = f.readlines()
		for lines in log:
			if 'Failed password for invalid user ' in lines or 'Failed password for root from ' in lines:
				if lines.split('from ')[1].split(' ')[0] not in self.IP:
					self.IP.append(lines.split('from ')[1].split(' ')[0])
		return self.IP
	def xml(self):
		with open('report.xml','w') as f :
			f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
			f.close()
		with open('report.xml','a') as f:
			for i in self.IP:
				f.write('<host>\n')
				f.write('\t<ip>{}</ip>\n'.format(i))
				f.write('</host>\n')
			f.close()

class Host():
	def __init__(self,ip,key):
		self.ip = ip
		self.key = key
		self.url = "https://api.shodan.io/shodan/host/{}?key={}".format(self.ip,self.key)	
	def passiveRecon(self):
		print("[+] Passive recon for {}".format(self.ip))
		response = urllib.request.urlopen(self.url).read()
	def getCountry(self):	
		return "test"
	def getPorts(self):	
		print("\tPort : {}\n\tOrganisation {}\n\t".format(result['ports'],result['org']))
		return "Ports {}".format([33,44,55])
	def getIP(self):
		return self.ip
	def getServices(self):
		return "Services {}".format(["Apache", "Nginx"])

if __name__ == "__main__":
	xml = Report("/var/log/auth.log")
	xml.failedPassword()
