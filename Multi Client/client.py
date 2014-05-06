import socket

sockets = []

ports = 99999999

request = """GET / HTTP/1.1/ \r\n
Connection: keep-alive\r\n
"""

while ports!= 0:

	S = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

	S.connect(("127.0.0.1",80))

	S.send(request)

	ports = ports - 1

	print ports