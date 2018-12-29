#!/usr/bin/env python
""" Provides a means for updating a DNS server with a new ip address dynamically.

IPQuery holds the URLs and method for getting the current machines IP and posting it the DNS.
"""
import requests
import sys

__author__ = "Scott Lockett"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Scott Lockett"
__email__ = "scottlockett1994@gmail.com"


class IpQuery:
	# The URL for getting the IP address of the machine hitting the endpoint.
	IFCONFIG_URL = 'https://ifconfig.co/ip'

	# The URL for updating the goggle DNS with the new IP address.
	# e.g. See arens_vpn_update_url.txt file for example of URL. This file is NOT checked in for security reasons.
	DNS_URL = ''

	def get_ip_address(self):
		# Query the endpoint to grab the JSON, parse the IP Address and return it.
		endpoint = requests.get(self.IFCONFIG_URL)
		ipAddress = endpoint.text
		return ipAddress

	def get_api_url(self):
		return self.DNS_URL

	def push_url_to_dns(self, url):
		dns_and_new_ip = self.get_api_url() + url
		print('''Posting to ''' + dns_and_new_ip)
		response = requests.get(dns_and_new_ip)
		return response


def main(argv):
	# Create an instance of the ip query class. 
	ip_query = IpQuery()
	ip_query.DNS_URL = argv[0]

	# Get the current IP address of the machine. Does it matter what type of address it is? - IPv4? IPv6? 
	machines_ip = ip_query.get_ip_address()
	print('''This machines IP address is ''' + machines_ip)

	# Post the new URL to the endpoint and see whats returned.
	response = ip_query.push_url_to_dns(machines_ip)
	print('''Response from server was ''' + str(response))


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("""" usage: get-current-ip.py "<DNS URL>" """)
		sys.exit()
	else:
		main(sys.argv[1:])
# TODO in order to use requests it needs installing as it's not part of the standard python library. To do this, pip will need installing. See get-pip.py to install pip.
# Once pip is installed, requests can be installed using the command 'python -m pip install requests'. Maybe with --user on the end if permissions are a problem.
# This should then be good to go for running.
