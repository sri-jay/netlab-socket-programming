import socket

#connecting to server
connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
connection.connect(("127.0.0.1",1234))

#asking for nickname
handle = raw_input("Enter a nockname!\n")
#get message form user
message = raw_input("Enter a message to send to server!\n")

message = handle +" : "+message

#send message to server
connection.send(message)
#get reply from server
reply = connection.recv(1024)
#print server reply
print "\n",reply

connection.close()
#progrma ends