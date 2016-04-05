import socket
import threading

host = "127.0.0.1"
port = 5000
alias = ""
s = socket.socket()

def receiver():
    while True:
        data = ""
        data = s.recv(1024).decode("utf-8")
        print(data)

if __name__ == "__main__":
    s.connect((host, port))
    rec = threading.Thread(target=receiver)
    rec.start()
