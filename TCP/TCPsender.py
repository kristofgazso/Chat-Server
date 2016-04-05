import socket
import threading

host = "127.0.0.1"
port = 5000
alias = ""
s = socket.socket()

def send(message):
    s.send(message.encode("utf-8"))

def Main():

    message = input()
    while True:
        try:
            s.send(message.encode("utf-8"))
        except ConnectionResetError:
            print("[-] Server not responding")
            break
        message = input()
    s.close()

if __name__ == "__main__":
    s.connect((host, port))
    alias = input("Alias: ")
    send(alias)
    Main()
