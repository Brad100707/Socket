import socket
import threading

Header = 64
Port =5050
SERVER =  socket.gethostbyname(socket.gethostname())
#or socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, Port)
Format = 'utf-8'
Dissconnect_msg = "!Disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected.")

    connect = True
    while connect:
        msg_length = conn.recv(Header).decode(Format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(Format)
            if msg == Dissconnect_msg:
                connect = False
            print(f"[{addr}] {msg}")
            conn.send("Msg receive".encode(Format))

def start():
    server.listen()
    print(f"[Listening] Sever is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[Active Connection] {threading.active_count()-1}")

print("[Starting] sever is starting")
start()