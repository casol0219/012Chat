import socket
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from _thread import *

#서버 데이터 받기
#닉네임 변경: \x80
#   성공: \x80\x46
#   실패: \x80\x54
#사용자목록갱신: \x81
def receive(c_socket, window, callback):
    global nickname, datetime
    while True:
        try:
            recvData = c_socket.recv(1024)
            if not recvData:
                print("연결이 종료되었습니다.")
                window.close()
                break
            if recvData.startswith(b"\x80\x46"):
                print("실패")
                change_nick(window,1)
            elif recvData.startswith(b"\x80\x54"):
                print("성공")
                change_nick(window,0)
            elif recvData.startswith(b'\x81'):
                memlist = recvData.split(b'\x81')[1:]
                memlist = [ x.decode('utf-8') for x in memlist ]
                update_memlist(window,memlist)
            else:
                decoded_data = recvData.decode('utf-8')
            
                display_text = ""
                if decoded_data.count('**') >= 3:
                    nickname, datetime, data, byt = decoded_data.split('**', 3)
                    display_text = f"{byt}**{nickname}   {datetime}\n{data}"
                    callback(display_text)
                
                elif ':::::' in decoded_data:
                    data=decoded_data.split(':::::')[1]
                    display_text=f"\n{data}"
                    callback(display_text)

        except Exception as e:
            print(f"예외가 발생했습니다: {e}")
            window.close()
            break

# 서버 연결
def connect_to_server(window, callback):
    global c_socket
    HOST = "127.0.0.1"
    PORT = 12346

    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((HOST, PORT))

    start_new_thread(receive, (c_socket, window, callback))

def my_portNum():
    return str(c_socket.getsockname()[1])

def changing_nickname(new):
    global tmp
    tmp = new
    c_socket.send(b"\x80\x63\x6e"+tmp.encode('utf8')) #행동+닉네임

def change_nick(window,flag):
    global tmp
    print(tmp)
    if flag:
        tmp += window.port
        c_socket.send(b"\x80\x63\x6e"+tmp.encode('utf8'))
    if window.Text_myName:
        window.nickname = tmp
        window.Text_myName.setText(window.nickname)
    else:
        window.nickname = tmp

def update_memlist(window,memlist):
    print(f"updating memlist")
    window.memberTable.clear()
    for member in memlist:
        item=QtWidgets.QListWidgetItem()
        item.setText(member)
        window.memberTable.addItem(item)

#메시지, 입력 시간 보내기
def send_message(check_byte, message):
    sendTime = time.strftime('%Y/%m/%d %H:%M:%S')  # 입력시간
    c_socket.send((f'{sendTime}**{message}**{check_byte}').encode('utf-8'))

#서버 연결 종료
def close_connection():
    try:
        c_socket.close()
    except Exception as e:
        print(f"서버 연결 종료 중 오류 발생: {e}")
