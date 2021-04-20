import socket
import threading
nickname=input("choose a nickname:")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",55555))

def client():
    while True:
        try:
            message=client.recv(1024).decode("ascii")
            if message=="Nick":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("An error ocurred")
            client.close()
            break
def write():
    while True:
        message=f"{nickname}: {input('')}"
        client.send(message.encode("ascii"))

client_thread=threading.Thread(target=client)
client_thread.start()
write_thread=threading.Thread(target=write)
write_thread.start()




