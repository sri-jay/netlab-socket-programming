#importing socket package
import socket

#udp ip and port settings, modify to your choice!
UDP_IP = "127.0.0.1"
UDP_PORT = 12345

#message to send to partner
send_message = raw_input("Enter a message to send!")

#user prompt
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", send_message

#creating the socket:
# SOCK_DGRAM specifies a UDP type socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending the message 
sock.sendto(send_message, (UDP_IP, UDP_PORT))

#receive a reply from the client 
data ,address = sock.recvfrom(1024)
print "Reply : ",data

#close the socket
sock.close()
