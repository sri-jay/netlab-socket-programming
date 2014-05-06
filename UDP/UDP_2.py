#importing the socket package
import socket
  
#udp ip and port settings, modify to your choice!
UDP_IP = "127.0.0.1"
UDP_PORT = 12345

#creating the socket:
# SOCK_DGRAM specifies a UDP type socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#binding the port to ip, or specify tuple in recvfrom() function
sock.bind((UDP_IP, UDP_PORT))

#Receving the message
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print "received message:", data

#get a reply from user to send back
send_reply = raw_input("Enter a reply!")

#send the reply
sock.sendto(send_reply,addr)


#close the socket
sock.close()