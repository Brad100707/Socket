import socket
Header = 64
Port =5050
Format = 'utf-8'
Dissconnect_msg = "!Disconnect"
SERVER = "100.64.208.151"
ADDR = (SERVER,Port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(Format)
    msg_length = len(message)
    send_length = str(msg_length).encode(Format)
    send_length += b' ' * (Header-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(Format))

while True:
    send(input())
