# Class for querying the current machines IP address and pushing the resulting Ip address to a DNS server
import requests

class IpQuery:

	# The URL for getting the IP address of the machine hitting the endpoint.
	IFCONFIG_URL = 'https://ifconfig.co/ip'
	
	# The URL for updating the goggle DNS with the new IP address.
	DNS_URL = 'https://httpbin.org/'

	def getIpAddress(self):
		# Query the endpoint to grab the JSON, parse the IP Address and return it.
		endpoint = requests.get(self.IFCONFIG_URL)
		ipAddress = endpoint.text
		return ipAddress
		
	def getApiUrl(self): 
		# todo
		return self.DNS_URL
		
	def pushToDNS(self, url):
		payload = {'key','value'}
		endpoint = requests.get(self.DNS_URL, params=payload)
		print(endpoint)
		
def main():
	# Create an instance of the ip query class. 
	ipQuery = IpQuery()
	
	# Get the current IP address of the machine. Does it matter what type of address it is? - IPv4? IPv6? 
	newIpAddress = ipQuery.getIpAddress()
		
	print(ipQuery.getApiUrl())
	print(newIpAddress)

if __name__ == '__main__':
	main()