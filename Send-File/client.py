#including libraries
import socket

#creating and configuring the socket
my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

#connecting to server's welcome socket 
my_socket.connect(("127.0.0.1",12345))

#get a file-interface for message.txt
#open message.txt in read mode : "r"
#other modes are "w" - write mode, "a" - append "r+" read/write
message = open("message.txt","r")

#read the data inside the textfile and close
message_content = message.read()
message.close()

#send the data to server
my_socket.send(message_content)

#receive reply from server
server_reply = my_socket.recv(1024)

#printing server_reply
print server_reply

#reopen file in write mode and APPEND server-reply to file
message = open("message.txt","a")
message.write(server_reply)
message.close()

#close client socket
my_socket.close()

#program ends