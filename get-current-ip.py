# Class for querying the current machines IP address and pushing the resulting IP address to a DNS server
import requests

class IpQuery:

	# The URL for getting the IP address of the machine hitting the endpoint.
	IFCONFIG_URL = 'https://ifconfig.co/ip'
	
	# The URL for updating the goggle DNS with the new IP address.
	DNS_URL = 'https://httpbin.org/'

	def get_ip_address(self):
		# Query the endpoint to grab the JSON, parse the IP Address and return it.
		endpoint = requests.get(self.IFCONFIG_URL)
		ipAddress = endpoint.text
		return ipAddress
		
	def get_api_url(self): 
		# todo
		return self.DNS_URL
		
	def push_url_to_dns(self, url):
		payload = {'key','value'}
		endpoint = requests.get(self.DNS_URL, params=payload)
		print(endpoint)
		
def main():
	# Create an instance of the ip query class. 
	ip_query = IpQuery()
	
	# Get the current IP address of the machine. Does it matter what type of address it is? - IPv4? IPv6? 
	machines_ip = ip_query.get_ip_address()

	print('''This machines IP address is ''' + machines_ip)

if __name__ == '__main__':
	main()
	# TODO in order to use requests it needs installing as it's not part of the standard python library. To do this, pip will need installing. See get-pip.py to install pip. 
	# Once pip is installed, requests can be installed using the command 'python -m pip install requests'. Maybe with --user on the end if permissions are a problem. 
	# This should then be good to go for running. 