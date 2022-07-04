#ip = '127.0.0.1'
#port = 443

info = '''
Scanning port on PC
PORT SCANNER
Zakaria Bouidane
2022

=================================
PORT\tSTATE\tServices
=================================
'''
print(info)

from socket import socket, AF_INET, SOCK_STREAM, getservbyport
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-t', '--target', dest='ip', help='SET IP[pc] PC or IP[site]')
(options, args) = parser.parse_args()

so = socket(AF_INET, SOCK_STREAM)

for ports in range(1, 1000):
	so = socket(AF_INET, SOCK_STREAM)
	so.settimeout(0.1)
	try:
		con = so.connect((ip,ports))
		if con == None:
			print('{}\tOPEN\t{}'.format(ports),getservbyport(ports))
	except Exception:
		print('{}\tCLOSED\t'.format(ports))
