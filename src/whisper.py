from changeWord import *

def whisper(recvMessage,sendTime,c_name,c_list,nickname,c_socket,check_by):
    recipient_name=recvMessage.split(' ')[1]
    print(f"{recipient_name}")
    whisper_message=' '.join(recvMessage.split(' ')[2:])
    filtered_data = changeWord(whisper_message)
    print(c_name)

    if recipient_name in c_name:
        recipient_idx=c_name.index(recipient_name)
        r_socket=c_list[recipient_idx]
        server_bytes=b"\x30\x31\x32\x73"
        r_socket.send(server_bytes+f'**{nickname} 님의 귓속말**{sendTime}**{filtered_data}**{check_by}'.encode('utf-8'))
        c_socket.send(server_bytes+f'**{recipient_name} 님에게 귓속말**{sendTime}**{filtered_data}**{check_by}'.encode('utf-8'))
    else:
        c_socket.send(f":::::상대방이 존재하지 않습니다.".encode('utf-8'))

    #로깅
    print(f"[whisper] {nickname} to {recipient_name} - {recvMessage}  {sendTime}")
