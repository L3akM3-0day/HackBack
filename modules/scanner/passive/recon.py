import urllib.request
import json
class Shodan():
	def __init__(self,ip):
		
		self.ip = ip
		self.key = "7OThNwtEfTM7nwgAbHWt7yE72fUykNwT"
		self.url = "https://api.shodan.io/shodan/host/{}?key={}".format(self.ip,self.key)	
		print("[+] Passive recon for {}".format(self.ip))
		try:
			self.response = json.loads(urllib.request.urlopen(self.url).read().decode('utf-8'))
		except urllib.error.HTTPError:
			self.response = "Can't Retrive information"
			print(self.response)
	def getCountry(self):	
		if isinstance(self.response, str):
			pass
		else:
			return "\tCountry Code :{}\n\tCountry Name : {}\n".format(self.response['country_code3'], self.response['country_name'])	
	def getPorts(self):	
		if isinstance(self.response, str):
			pass
		else:
			return "\tPorts {}\n".format(self.response['ports'])
	def getIP(self):
		if isinstance(self.response, str):
			pass
		else:
			return self.ip
	def getServices(self):
		if isinstance(self.response, str):
			pass
		else:
			return "\tServices :\n\t\tProduct {}\n\t\tVersion {}\n\t\tPort : {}\nMore Info\n\n{}".format(self.response['data'][0]['product'],self.response['data'][0]['version'],self.response['data'][0]['port'], (self.response['data'][0]['data']))
if __name__ == "__main__":
	test = Shodan('195.154.62.184')
