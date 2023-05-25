import os, sys, time, socket
from time import sleep

#tampilan
print ('\n')
print ('SCRIPT BY : Mr./Malware03')
print ('YOUTUBE   : Mr./malware03')
time.sleep(3)
os.system('clear')
os.system('figlet InfoWeb')
print ('\n')
print ('[1] cari informasi website')
print ('[2] cari ip website')
print ('[3] keluar')
print ('')
pilih = int(input('[•] Choose: '))

#data
if pilih ==1:
   os.system('clear')
   os.system('figlet InfoWeb')
   print ('masukan nama domain target')
   domain = input('nama domain : ')
   print ('mencari data...')
   time.sleep(5)
   print ('\n')
   print ('========== [INFORMASI WEBSITE] ==========')
   os.system('whois ' + domain)

if pilih ==2:
   os.system('clear')
   os.system('figlet InfoWeb')
   print ('\n')
   host = input('masukan nama domain : ')
   ip_address = socket.gethostbyname(host)
   print ('')
   print (f'domain     : ', host)
   print (f'ip-address : ', ip_address)

if pilih ==3:
   exit()