import socket
import time
from _thread import *
import threading

decoded_data = ""
c_socket = None

# 서버 연결
def connect_to_server(HOST, PORT):
    global c_socket
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive)
    receive_thread.daemon = True  #쓰레드를 데몬으로 설정
    receive_thread.start()

#서버 데이터 받기
def receive():
    global c_socket, decoded_data, data, sender, dataTime
    while True:
        try:
            recvData = c_socket.recv(1024)
            if not recvData: 
                break
            decoded_data = recvData.decode('utf-8', errors='ignore')
            print(decoded_data)  #데이터 수신 시 출력 (디버깅용)
            data, sender, dataTime = decoded_data.split(' ', 2) #받은 데이터 각 변수로 분리

        except Exception as e:
            print(f"데이터 수신 중 예외 발생: {e}")
            break
        
    close_connection()  # 연결 종료


#메시지, 입력 시간 보내기
def send_message(message):
    sendTime = time.strftime('%Y/%m/%d %H:%M:%S')  # 입력시간
    c_socket.send((f'{message} {sendTime}').encode('utf-8'))

#서버 연결 종료
def close_connection():
    try:
        c_socket.close()
    except Exception as e:
        print(f"서버 연결 종료 중 오류 발생: {e}")
