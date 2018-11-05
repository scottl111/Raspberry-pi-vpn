import requests

class IpQuery:

	def getIpAddress(self):
		# Query the endpoint to grab the JSON, parse the IP Address and return it.
		endpoint = requests.get('https://ifconfig.co/ip')  
		ipAddress = endpoint.text
		return ipAddress
		
	def getApiUrl(self):
		# TODO
		print('todo')
		
def main():
	ipQuery = IpQuery()
	print(ipQuery.getIpAddress())
	
if __name__ == '__main__':
	main()