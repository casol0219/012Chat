def whisper(recvMessage):
    recipient_port=int(recvMessage.split(' ')[1]) #일단은 포트 번호로 구분하도록 해놓음
    print(f"port : {recipient_port}")
    whisper_message=' '.join(recvMessage.split(' ')[2:])
    for client in c_list:
        client_ip, client_port=client.getpeername()
        print(client_ip,client_port)
        if client_port==recipient_port:
            client.send(f"{addr[1]}님으로부터의 귓속말: {whisper_message}".encode())
            print(whisper_message)
            break