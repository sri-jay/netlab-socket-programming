import socket
from threading import Thread

#contains client sockets
CLIENT_LIB = []
#contains threads
THREAD_LIBRARY = []

#sends data passed to it to all clients
def send_data(message):

	for client in CLIENT_LIB :

		client.send(message)

#receive and print data from a client
def receive_(socket_):

	while True :

		data = socket_.recv(1024)

		print data

#attaches the nickname to message and passes
#the message to send_data(), which sends data to all clients
def send_to_clients(handle):

	while True:

		message = raw_input()

		message = handle + " : " + message

		send_data(message)

#main function, like int main
#not necessary like int main
def main_function():

	#Creating welcome socket
	welcome_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

	#binding the welcome socket
	welcome_socket.bind(("127.0.0.1",1234))

	#asking the nickname of server, like nickname in chat
	handle = raw_input("Enter a name!\n")

	#asking the connection limit, the number of clients that can connect
	client_limit = raw_input("Enter the Client Connection limit, the max number of clients that can connect\n")

	#converting string to int, as socket returns only strings
	client_limit = int(client_limit)

	#make the welcome socket listen for clients
	welcome_socket.listen(client_limit)

	#Setting up a function which sends data to all clients
	#This function runs on a thread so that it can continually send data
	#without waiting for other functions to finish executing
	send_to_clients_ = Thread(target=send_to_clients,args=(handle,))
	#staring the function on the thread
	send_to_clients_.start()
	#jst stoing the thread, in case i need to access it
	THREAD_LIBRARY.append(send_to_clients_)

	#loop to keep acceptiong clients till limit is reached
	while client_limit != 0:

		#client connects, and i get a socket for that client
		client_socket, data = welcome_socket.accept()

		print "A client has connected @",data
		client_limit = client_limit - 1

		print "# of clients that can connect further :",client_limit

		CLIENT_LIB.append(client_socket)

		#the function which recieves data for each client is put on a seperate thread
		#so i can receive data as it comes, instead of waiting to get data from one cleint, then another
		receive_thread_ = Thread(target = receive_,args=(client_socket,))
		receive_thread_.start()
		THREAD_LIBRARY.append(receive_thread_)

#run the main function
main_function()