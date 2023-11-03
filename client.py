import socket
from _thread import *

def receive(c_socket):
	while True:
		recvData=c_socket.recv(1024)
		print('상대방 :',recvData.decode('utf-8')) #여기에는  전송자 이름 뜨도록 구현해야 함
HOST = "127.0.0.1"
PORT = 12346

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_socket.connect((HOST, PORT))
	
print('>> Welcome to 012 Chat!')

start_new_thread(receive,(c_socket,))

while True:
	sendData=input('>>>')
	if sendData=='exit':
		break
	c_socket.send(sendData.encode('utf-8'))

c_socket.close()