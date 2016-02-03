from socket import *
import base64
import ssl

msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.live.com'              
port = 587                          

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,port))

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
 print '220 reply not received from server.'


heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not received from server.'

clientSocket.send('starttls\r\n')
clientSSLSocket = ssl.wrap_socket(clientSocket,      server_side=True,
                             certfile="cert.pem",
                             keyfile="cert.pem",
                             ssl_version= ssl.PROTOCOL_TLSv1)
clientSSLSocket.send('auth login\r\n')
clientSSLSocket.send('base64.b64encode(¡®throw2@hotmail.com¡¯)+\r\n')
clientSSLSocket.send('base64.b64encode(¡®31415926a)+\r\n')

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <throw2hotmail.com>\r\n'
clientSSLSocket.send(mailFromCommand)
recv2 = clientSSLSocket.recv(1024)
print recv2
if recv2[:3] != '250':
 print '250 reply not received from server.'

# Send RCPT TO command and print server response.
reptToCommand = 'RCPT TO: <throw2@hotmail.com>\r\n'
clientSSLSocket.send(reptToCommand)
recv3 = clientSSLSocket.recv(1024)
print recv3
if recv3[:3] != '250':
 print '250 reply not received from server.'

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSSLSocket.send(dataCommand)
recv4 = clientSSLSocket.recv(1024)
print recv4
if recv4[:3] != '354':
 print '250 reply not received from server.'

# Send message data.
clientSSLSocket.send(msg)                
# Message ends with a single period.
clientSSLSocket.send(endmsg)           

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSSLSocket.send(quitCommand)
recv5 = clientSSLSocket.recv(1024)
print recv5
if recv5[:3] != '221':
 print '221 reply not received from server.'
