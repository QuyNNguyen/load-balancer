
#Name: Quy Nguyen
#python3


import sys
import requests
import ipaddress
import threading


openProxyList = []
threads = []
ipList = []

#check an ip for open proxy
#https :1080
#ftp :3128

def checkOpenProxy(ip):
	try:
		req = requests.get("http://csec.rit.edu",timeout = 1, proxies={"http":"http://"+str(ip)+":3128"})
		openProxyList.append(str(ip))
	except:
		pass


#get a list of IPs between startIP and endIP
def getIPList(startIP, endIP):
	ipList = []
	while startIP <= endIP:
		ipList.append(startIP)
		startIP = startIP+1
	return ipList


#https://docs.python.org/2/library/threading.html
if __name__=="__main__":
	if len(sys.argv) != 3:
		print("Please input a start IP and an end IP address:")
		sys.exit()
	else:

		#Getting IP addresses
		startIP = ipaddress.ip_address(sys.argv[1])
		endIP = ipaddress.ip_address(sys.argv[2])

		ipList = getIPList(startIP, endIP)



		#Starting threads to check proxy for each ip
		for ip in ipList:
			thr = threading.Thread(target=checkOpenProxy, args=(ip,))
			threads.append(thr)
			thr.start()


		#Save guarding the result - dont let the system messup the array
		for thr in threads:
			thr.join()


		#Printing Results

		print("IPs that have open proxy:")
		for ip in openProxyList:
			print(ip)










