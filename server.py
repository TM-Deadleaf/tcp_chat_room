import socket
import threading

host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.rcv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            clients.close(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast("This {} has been disconnected form the server!".format(nickname).encode("ascii"))
            break


def recieve():
    client, address = server.accept()
    print(f"Connected with {str(address)}")
    client.send("Nick".encode("ascii"))
    nickname = client.recv(1024).decode("ascii")
    nicknames.append(nickname)
    clients.append(client)
    print(f"nickname of the client is {nickname}")
    broadcast(f"{nickname} has been connected!".encode("ascii"))
    client.send("Connected to the server!!".encode("ascii"))
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()


recieve()
