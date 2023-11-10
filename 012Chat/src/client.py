import socket
import time
from _thread import *

#서버 데이터 받기
def receive(c_socket):
    global decoded_data
    while True:
        try:
            recvData = c_socket.recv(1024)
            if not recvData:
                print("연결이 종료되었습니다.")
                break
            decoded_data = recvData.decode('utf-8')
            print(decoded_data)  #데이터 수신 시 출력 (디버깅용)
        except Exception as e:
            print(f"예외가 발생했습니다: {e}")
            break

# 서버 연결
def connect_to_server():
    global c_socket
    HOST = "127.0.0.1"
    PORT = 12346

    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((HOST, PORT))

    start_new_thread(receive, (c_socket,))

    #receive_thread = threading.Thread(target=receive)
    #receive_thread.daemon = True  #쓰레드를 데몬으로 설정
    #receive_thread.start()

#메시지, 입력 시간 보내기
def send_message(message):
    sendTime = time.strftime('%Y/%m/%d %H:%M:%S')  # 입력시간
    c_socket.send((f'{sendTime} {message}').encode('utf-8'))

#서버 연결 종료
def close_connection():
    try:
        c_socket.close()
    except Exception as e:
        print(f"서버 연결 종료 중 오류 발생: {e}")
