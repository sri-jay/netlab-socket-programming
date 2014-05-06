import socket
import time
import os
from threading import Thread

CLIENT_LIB = []

THREAD_LIBRARY = []

def send_data(message):

	for client in CLIENT_LIB :

		client.send(message)


def receive_(socket_):

	while True :

		data = socket_.recv(1024)

		print data


def send_to_clients(handle):

	while True:

		message = raw_input()

		message = handle + " : " + message

		send_data(message)


def main_thread():

	welcome_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

	welcome_socket.bind(("127.0.0.1",1234))

	handle = raw_input("Enter a handle!")

	os.system("cls")

	client_limit = raw_input("Enter the Client Connection limit")

	client_limit = int(client_limit)

	welcome_socket.listen(client_limit)

	send_to_clients_ = Thread(target=send_to_clients,args=(handle,))
	send_to_clients_.start()
	THREAD_LIBRARY.append(send_to_clients_)


	while client_limit != 0:

		client_socket, data = welcome_socket.accept()

		client_limit = client_limit - 1

		CLIENT_LIB.append(client_socket)

		receive_thread_ = Thread(target = receive_,args=(client_socket,))
		receive_thread_.start()
		THREAD_LIBRARY.append(receive_thread_)

main_thread()