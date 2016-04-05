import socket
import threading

host = "127.0.0.1"
port = 5000
alias = ""
s = socket.socket()

def send(message):
    s.send(message.encode("utf-8"))

def receiver():
    while True:
        data = ""
        data = s.recv(1024).decode("utf-8")
        print(data)

def Main():

    message = input()
    while message != "q":
        try:
            s.send(message.encode("utf-8"))
        except ConnectionResetError:
            print("[-] Server not responding")
            break
        #data = s.recv(1024).decode("utf-8")
        #print("Received from server: " + data)
        message = input()
    s.close()

if __name__ == "__main__":
    s.connect((host, port))
    alias = input("Alias: ")
    send(alias)
    send = threading.Thread(target=Main)
    rec = threading.Thread(target=receiver)
    send.start()
    rec.start()
