from changeWord import *

def whisper(recvMessage,sendTime,c_name,c_list,nickname,c_socket):
    recipient_name=recvMessage.split(' ')[1]
    print(f"{recipient_name}")
    whisper_message=' '.join(recvMessage.split(' ')[2:])
    filtered_data = changeWord(whisper_message)
    print(c_name)

    if recipient_name in c_name:
        recipient_idx=c_name.index(recipient_name)
        r_socket=c_list[recipient_idx]
        r_socket.send(f"{nickname}님으로부터의 귓속말: {filtered_data}".encode('utf-8'))
    else:
        c_socket.send(f"상대방이 존재하지 않습니다.".encode('utf-8'))

    #로깅
    print(f"[whisper] {nickname} to {recipient_name} - {recvMessage}  {sendTime}")
