import socket
from _thread import *
from changeWord import *
from whisper import *

#접속자 목록
c_list = []

#접속자 닉네임 목록
c_name = []


def groupChat(c_socket, addr):
    #초기 닉네임 설정 start
    #닉네임설정 데이터 형식: NICKNAMECHANGE::닉네임
    nickname = c_socket.recv(1024).decode('utf8').split("::")[-1]
    #닉네임 중복 시 닉네임 뒤에 포트번호 붙임
    if nickname in c_name:
        c_socket.send("NICKNAMECHANGE::FALSE".encode('utf8'))
        nickname = c_socket.recv(1024).decode('utf8').split("::")[-1]
    else:
        c_socket.send("NICKNAMECHANGE::TRUE".encode('utf8'))
    c_name.append(nickname)
    #초기 닉네임 설정 end
    print(f">> {nickname} 님이 입장하셨습니다.")
    user_update_data = "USERUPDATE::"+'|'.join(c_name)
    for client in c_list:
        client.send(user_update_data.encode('utf8'))
        client.send(f":::::[ {nickname} 님이 입장하셨습니다. ]".encode('utf-8'))
    
    while True:
        try:
            data = c_socket.recv(1024).decode('utf-8')
            if "NICKNAMECHANGE" != data.split("::")[0]:
                if '**' in data:
                    sendTime, recvMessage = data.split('**', 1)    #받은 메시지, 보낸 시간 분리
                    msg_bytes=recvMessage.encode('utf-8')
                
            if not data:
                print(f">> {nickname} 님이 대화방을 나갔습니다.")
                break
            
            #닉네임 변경 start
            elif "NICKNAMECHANGE" == data.split("::")[0]:
                tmp_nick = data.split("::")[1]
                
                if tmp_nick in c_name and tmp_nick != nickname:
                    c_socket.send("NICKNAMECHANGE::FALSE".encode('utf8'))
                    c_name.remove(nickname)
                    
                    nickname = c_socket.recv(1024).decode('utf8').split("::")[-1]
                else:
                    c_socket.send("NICKNAMECHANGE::TRUE".encode('utf8'))
                    c_name.remove(nickname)
                    nickname = tmp_nick
                c_name.append(nickname)
                user_update_data = "USERUPDATE::"+'|'.join(c_name)
                for client in c_list:
                    client.send(user_update_data.encode('utf8'))
            #닉네임 변경 end

            #귓속말 기능
            elif msg_bytes.startswith(b'\x2F\x77\x20'):
                whisper(recvMessage,sendTime,c_name,c_list,nickname,c_socket)

            #존재하지 않는 명령어 입력했을 때
            elif msg_bytes.startswith(b'\x2F'):
                c_socket.send(f":::::입력하신 명령어가 존재하지 않습니다.\n'/w 상대방이름 메시지' 를 입력하여 귓속말을 보낼 수 있습니다.".encode('utf-8'))

            #일반 채팅
            else:
                #금칙어 처리
                filtered_data = (changeWord(recvMessage).encode('utf-8')).decode('utf-8')
                #오가는 메시지들 로깅
                print(f"{nickname} - {recvMessage}  {sendTime}")

                #자신 포함 모든 접속자에게 메시지 전송
                for client in c_list:
                    #발신자 정보, 시간, 금칙어 처리 메시지 보내기
                    client.send(f'{nickname}**{sendTime}**{filtered_data}'.encode('utf-8'))
                    
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
        for client in c_list:
            user_update_data = "USERUPDATE::"+'|'.join(c_name)
            client.send(user_update_data.encode('utf8'))
        
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
