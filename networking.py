from scapy import *

info = '''
+===================================+
+        python-network             +
+           with Zack               +
+===================================+
'''
print(info)
def network(pkt):
	print('NEW PACKETS ......!')
	print('-------------------')
sniff(iface='Wi-Fi', prn=network  )