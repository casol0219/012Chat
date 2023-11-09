import socket
from _thread import *

c_list = []
forbidden_words = ["시발", "미친", "꺼져", "놈"]

def changeWord(message):
    for word in forbidden_words:
        if word in message:
            replacement = '@' * len(word)   #금칙어에 걸린 문자열의 길이만큼 '@'로 대체
            message = message.replace(word, replacement)
    return message

def groupChat(c_socket, addr):
    sender_info = f"{addr[0]}:{addr[1]}"  #발신자 정보
    print(f">> {sender_info} 님이 입장하셨습니다.")
    
    while True:
        try:
            data = c_socket.recv(1024).decode('utf-8')
            recvMessage, sendTime = data.split(' ', 1)    #받은 메시지, 보낸 시간 분리
            
            if not data:
                print(f">> {sender_info} 님이 대화방을 나갔습니다.")
                break

            # 금칙어 처리
            filtered_data = changeWord(recvMessage)
            print(f"{sender_info} - {recvMessage}  {sendTime}")  #오가는 메시지들 로깅
            
            for client in c_list:
                if client != c_socket:
                    client.send(filtered_data.encode('utf-8'))

                    
        except ConnectionResetError as e:
            print(f">> {sender_info} 님이 대화방을 나갔습니다.")
            for client in c_list:
                if client != c_socket:
                    client.send(f">> {sender_info} 님이 대화방을 나갔습니다.".encode('utf-8'))
            break
                            
    if c_socket in c_list:
        c_list.remove(c_socket)
        print('>> 접속자 목록을 갱신했습니다 - 접속자 수 : ', len(c_list))
        print(c_list)
        
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
