import socket
from _thread import *
from changeWord import *
from whisper import *
import time

#접속자 목록
c_list = []

#접속자 닉네임 목록
c_name = []

#nicknamechange: \x80
def groupChat(c_socket, addr):
    #초기 닉네임 설정 start
    #닉네임설정 데이터 형식: NICKNAMECHANGE::닉네임
    nickname = c_socket.recv(1024).split(b'\x80\x63\x6e')[1].decode('utf-8')
    #닉네임 중복 시 닉네임 뒤에 포트번호 붙임
    if nickname in c_name:
        c_socket.send(b'\x80\x46')
        nickname = c_socket.recv(1024).split(b'\x80\x63\x6e')[1].decode('utf-8')
    else:
        c_socket.send(b'\x80\x54')
    c_name.append(nickname)
    #초기 닉네임 설정 end
    print(f">> {nickname} 님이 입장하셨습니다.")
    b_name = [ x.encode('utf-8') for x in c_name ]
    user_update_data = b'\x81'+b'\x81'.join(b_name)
    for client in c_list:
        client.send(user_update_data)
        time.sleep(0.5)
        client.send(f":::::[ {nickname} 님이 입장하셨습니다. ]".encode('utf-8'))
    c_socket.send(f":::::012Chat에 오신 것을 환영합니다!\n[/w 상대방이름 보낼메시지] 를 입력하여 귓속말을 보낼 수 있습니다.".encode('utf-8'))
    
    bytes_header = (b'\x80', b'\x81')

    while True:
        server_bytes=b"\x30\x31\x32\x73"
        try:
            data = c_socket.recv(1024)
            if not data.startswith(bytes_header):
                if '**'.encode('utf-8') in data:
                    sendTime, recvMessage, check_by = data.decode('utf-8').split('**', 2)
                    msg_bytes = recvMessage.encode('utf-8')
                
            if not data:
                print(f">> {nickname} 님이 대화방을 나갔습니다.")
                break
            
            #닉네임 변경 start
            elif data.startswith(b"\x80\x63\x6e"):
                tmp_nick = data.split(b"\x80\x63\x6e")[1].decode('utf-8')
                
                if tmp_nick in c_name and tmp_nick != nickname:
                    c_socket.send(b'\x80\x46')
                    c_name.remove(nickname)
                    
                    nickname = c_socket.recv(1024).split(b"\x80\x63\x6e")[1].decode('utf-8')
                else:
                    c_socket.send(b'\x80\x54')
                    c_name.remove(nickname)
                    nickname = tmp_nick
                c_name.append(nickname)
                b_name = [ x.encode('utf-8') for x in c_name ]
                user_update_data = b"\x81"+b'\x81'.join(b_name)
                for client in c_list:
                    client.send(b'\x81'+user_update_data)
            #닉네임 변경 end

            #귓속말 기능
            elif msg_bytes.startswith(b'\x2F\x77\x20'):
                whisper(recvMessage,sendTime,c_name,c_list,nickname,c_socket, check_by)

            #존재하지 않는 명령어 입력했을 때
            elif msg_bytes.startswith(b'\x2F'):
                c_socket.send(f":::::입력하신 명령어가 존재하지 않습니다.\n'/w 상대방이름 메시지' 를 입력하여 귓속말을 보낼 수 있습니다.".encode('utf-8'))

            #일반 채팅
            else:
                #채팅
                if check_by.startswith('\x63\x68\x61\x74'):
                    #금칙어 처리
                    filtered_data = (changeWord(recvMessage).encode('utf-8')).decode('utf-8')
                    #오가는 메시지들 로깅
                    print(f"{nickname} - {recvMessage}  {sendTime}")

                    #자신 포함 모든 접속자에게 메시지 전송
                    for client in c_list:
                        #발신자 정보, 시간, 금칙어 처리 메시지 보내기
                        client.send(server_bytes+f'**{nickname}**{sendTime}**{filtered_data}**{check_by}'.encode('utf-8'))

                #이모티콘     
                elif check_by.startswith('\x65\x6D\x6F\x6A\x69'):
                    #오가는 메시지들 로깅
                    print(f"{nickname} - {recvMessage}  {sendTime}")

                    #자신 포함 모든 접속자에게 메시지 전송
                    for client in c_list:
                        #발신자 정보, 시간, 금칙어 처리 메시지 보내기
                        client.send(server_bytes+f'**{nickname}**{sendTime}**{recvMessage}**{check_by}'.encode('utf-8'))
                                   
        except ConnectionResetError as e:
            print(f">> {nickname} 님이 대화방을 나갔습니다.")
            for client in c_list:
                if client != c_socket:
                    client.send(f":::::[ {nickname} 님이 대화방을 나갔습니다. ]".encode('utf-8'))
            break
                            
    if c_socket in c_list:
        c_name.remove(nickname)
        c_list.remove(c_socket)
        print('>> 접속자 목록을 갱신했습니다 - 접속자 수 : ', len(c_list))
        print(c_list)
        b_name = [ x.encode('utf-8') for x in c_name ]
        user_update_data = b'\x81'+b'\x81'.join(b_name)
        for client in c_list:
            client.send(user_update_data)
        
    c_socket.close()


def start_server():
    PORT = 12346
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind(('', PORT))
    s_socket.listen()

    print('>> 012 Chat Server Start')
    print('>> 접속자를 기다리는 중...\n')

    try:
        while True:
            c_socket, addr = s_socket.accept()
            c_list.append(c_socket)
            print("접속자 수 : ", len(c_list))
            start_new_thread(groupChat, (c_socket, addr))

    except Exception as e:
        print('에러 발생:', e)
    finally:
        s_socket.close()


if __name__ == "__main__":
    start_server()
