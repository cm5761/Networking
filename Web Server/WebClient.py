#import socket module
import sys
import string
from socket import *
clientSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
port=string.atoi(sys.argv[2])
clientSocket.connect((sys.argv[1],port))
clientSocket.send(str(sys.argv[3]))
import time
time.sleep(2)
server_info=clientSocket.recv(1000)
print server_info


clientSocket.close() 
