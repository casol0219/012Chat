def p2pchat(recvMessage):
    recipient_port=int(recvMessage.split(' ')[1]) #일단은 포트 번호로 구분하도록 해놓음
    recipient_socket=None
    for client in c_list:
        client_ip, client_port=client.getpeername()
        if client_port==recipient_port:
            recipient_socket=client
            break
        if recipient_socket:
            c_connections[c_socket]=recipient_socket
            recipient_socket.send(f"{addr[1]}님이 1:1 대화를 요청하셨습니다.\n수락하시겠습니까?(Y/N): ".encode())
        else:
            c_socket.send("상대방이 존재하지 않습니다.".encode())