
# Including required packages.
# The socket pacakage contains functions and classes for socket programming in python.
import socket

#creating welcome socket 
welcome_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

#binding welcome socket to some address
welcome_socket.bind(("127.0.0.1",12345))

#enable listening on welcome socket, accept at most 1 connection
welcome_socket.listen(1)

#welcome socket return client socket and client data(IP and PORT #) specific to client
client_socket,data = welcome_socket.accept()

# Data recevied from client. The recv function receives specified amount of data and returns it 
data_from_client = client_socket.recv(1024)

#print data recevied
print data_from_client

#taking input from user to send to client
send_message = raw_input("Enter a message to send to client")

#send the data to client
client_socket.send(send_message)

#close client socket
client_socket.close()

#close welcome socket
welcome_socket.close()

#program ends