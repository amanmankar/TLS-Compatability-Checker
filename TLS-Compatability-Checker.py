#Uses Python3
import re
import subprocess
import sys
import os
import socket
import ipaddress
import shutil
from ipaddress import IPv4Address

def Range():	
	
	sip = input("Enter Start IP: ")
	eip = input("Enter End IP: ")
	print ("********************")
	if '.' not in sip:
		print("IP address is invalid.")
		sys.exit()
	if '.' not in sip:
		print("IP address is invalid.")
		sys.exit()
	
	try:
		socket.inet_aton(sip)
		socket.inet_aton(eip)
	except socket.error:
		print ("IP address is invalid.")
		sys.exit()  

	start_ip = ipaddress.IPv4Address(sip)
	end_ip = ipaddress.IPv4Address(eip)
	file2 = open("IP_List.txt","a")
	file2.seek(0)
	file2.truncate()
	for ip_int in range(int(start_ip), int(end_ip)+1):
		addr = ipaddress.IPv4Address(ip_int)
		file2 = open ("IP_List.txt","a")
		file2.write(str(addr))
		file2.write("\n")
		file2.close()

def SingleIP():
		
	singleip = input("Enter IP: ")
	if '.' not in singleip:
		print("IP address is invalid.")
		sys.exit()	
	try:
		socket.inet_aton(singleip)
		
	except socket.error:
		print ("IP address is invalid.")
		sys.exit()
	  
	return singleip

def readFile(passed_list, inputvalue):
		
	if inputvalue == "3":
		file1 = open("IP_List.txt", "w")
		file1.close()
		fname = input("Enter File Name: ")
		try:
			shutil.copyfile(fname, "IP_List.txt")
		except:
			print("File not Found")
			os.remove("IP_List.txt")
			sys.exit()	
	file1 = open("IP_List.txt", "r")
	
	iplist = []
	for ip in file1:
		ip = ip.rstrip()
		njio
		if '.' not in ip:
			print("IP address is invalid.")
			sys.exit()	
		try:
			socket.inet_aton(ip)
		
		except socket.error:
			print ("IP address is invalid.")
			sys.exit()
		
		result = switch(ip)
		iplist.append(result)	
		
	file1.close()
	if inputvalue == "3":		
		os.remove("IP_List.txt")

	filename2 = input("\nEnter Filename to store TLSv0 IP's: ")
	file3 = open(filename2,"a")
	file3.seek(0)
	file3.truncate()
	file3.close()

	print ("IP's found with TLSv1.0 Enabled. Stored in file named %s" % filename2)
	for ip in iplist:
		file4 = open(filename2, "a")
		line1 = "".join(ip)
		if line1 is not '':
			print ("IP: %s" % (line1))
			file4.write(line1)
			file4.write("\n")
			file4.close()

def switch(ip):
	iplist1 = []	
	store = subprocess.check_output(["nmap", "--script", "ssl-enum-ciphers", "-p", "443", ip])
	if b'TLSv1.0' in store:
		print (ip + " -> TLS1.0 FOUND")
		iplist1.append(ip)
	else:
		print (ip + " -> TLS1.0 NOT FOUND")
	if b'TLSv1.1' in store:
		print (ip + " -> TLS1.1 FOUND")
	else:
		print (ip + " -> TLS1.1 NOT FOUND")
	if b'TLSv1.1' in store:     
		print (ip + " -> TLS1.2 FOUND")
		print ("********************")
	else:
		print (ip + " -> TLS1.2 NOT FOUND")
		print ("********************")
	return iplist1
	
def main():
	iplist2 = ''
	inputvalue = input("Select an option: \n 1: Check Single IP \n 2: Check IP Range \n 3: Check IP's using file \n\n Your Input: ")
	
	if inputvalue == "1":
		singleip1 = SingleIP()
		switch(singleip1)
	elif inputvalue == "2":			
		Range()
		readFile(switch(iplist2), inputvalue)
	elif inputvalue == "3":
		passedlist = ''
		readFile(passedlist, inputvalue)
	else:
		print("Wrong option selected")
		sys.exit()
	return inputvalue
if __name__ == "__main__":
	main()




