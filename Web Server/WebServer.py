#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('192.168.1.155',6008))                   
serverSocket.listen(1)
while True:
 #Establish the connection
 print 'Ready to serve...'
 connectionSocket, addr = serverSocket.accept()          
 try:
  message = connectionSocket.recv(1000)
  print message
  #filename = message.split()[1]
  f = open(message)
  #filename = "HelloWorld.html"
  #f = open(filename)
  outputdata = f.read()                                   
  #Send one HTTP header line into socket
  connectionSocket.send('HTTP/1.1 200 OK')
  connectionSocket.send('Content-Type: html\r\n\r\n')
  #Send the content of the requested file to the client
  for i in range(0, len(outputdata)):
   connectionSocket.send(outputdata[i])
  connectionSocket.close()
 except IOError:
  #Send response message for file not found
  connectionSocket.send('404 Not Found')  
  #Close client socket
  connectionSocket.close()
serverSocket.close() 
