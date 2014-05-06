#including libraries
import socket

#creating and configuring the socket
my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

#connecting to server's welcome socket 
my_socket.connect(("127.0.0.1",12345))

#get some data rom user to send to server
data_to_send_to_server = raw_input("Enter a message to be sent to server")

#send the data to server
my_socket.send(data_to_send_to_server)

#receive reply from server
server_reply = my_socket.recv(1024)

#print server reply
print server_reply

#close client socket
my_socket.close()

#program ends