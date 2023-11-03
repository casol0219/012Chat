#자기가 입력하는 도중에 상대방이 전송하면 자신의 말이 끊긴다는 점을 보완하기 위해
#GUI를 구현함
import socket
from _thread import *

#접속 클라이언트 목록
c_list=[]

#groupChat : 단체 채팅 구현
#sender 클라이언트에게 받은 데이터를 sender 클라이언트를 제외한 나머지 클라이언트들의 소켓에 보냄
#접속 클라이언트 목록인 c_list를 이용함
def groupChat(c_socket,addr):
    print(addr[0],':',addr[1],'님이 입장하셨습니다.')
    
    while True: #클라이언트가 접속을 끊을 때까지 반복
        
        try:
            data=c_socket.recv(1024) #데이터가 수신되면 클라이언트에 다시 전송 (에코)
            
            if not data:
               print('>> ',addr[0],':'.addr[1],'에서 접속이 종료되었습니다.')
               break
               
            print(addr[0],':',addr[1],' >> '+data.decode()) #오가는 메시지들 로깅            
            for client in c_list:
                if client!=c_socket:
                    client.send(data)
                    
        except ConnectionResetError as e: #접속 종료시
            print(addr[0],':',addr[1],' 접속 종료')
            for client in c_list:
                    client.send(addr[0],':',addr[1],'님이 접속을 종료하였습니다.')
            break
                            
    if c_socket in c_list:
        c_list.remove(c_socket)
        print('접속자 목록을 갱신했습니다. 접속자 수 : ',len(c_list))
        print(c_list)
    c_socket.close()


#HOST = "127.0.0.1"
PORT = 12346

#서버 소켓 생성
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(('', PORT))
s_socket.listen()

print('>> 012Chat Server Start')

try:
    while True:
        print('>> 접속자를 기다리는 중...')
        
        c_socket,addr=s_socket.accept()
        c_list.append(c_socket) #클라이언트 목록 갱신
        start_new_thread(groupChat,(c_socket,addr))
        print("접속자 수 :",len(c_list))

except Exception as e:
    print('에러 발생:',e)
finally:
    s_socket.close()
