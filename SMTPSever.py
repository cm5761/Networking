from socket import *
msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver.
mailserver = smtp.live.com
port = 25
# Create socket called clientSocket and establish a TCP connection with mailserver.
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer,port))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
print '220 reply not received from server.'
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not received from server.'
# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <throw2@hotmail.com>\r\n'
clientSocket.send(mailFromCommand)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
 print '250 reply not received from server.'
# Send RCPT TO command and print server response.
reptToCommand = 'RCPT TO: <Throw1@126.com>\r\n'
clientSocket.send(reptToCommand)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '250':
 print '250 reply not received from server.'
# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand)
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '354':
 print '354 reply not received from server.'
# Send message data.
clientSocket.send(msg)
# Message ends with a single period.
clientSocket.send(endmsg)
# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand)
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != '221':
 print '221 reply not received from server.'













 
