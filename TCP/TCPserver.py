import socket
import threading

host = "127.0.0.1"
port = 5000
connList = []

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(5)

def send_to_all(message):
    for connection in connList:
        connection.send(message.encode("utf-8"))

def Main():

    c, addr = s.accept()
    connList.append(c)
    adress = addr[0]+":"+str(addr[1])
    try:
        alias = c.recv(1024).decode("utf-8")
    except ConnectionResetError:
        print("[-] Quit before giving alias " + "("+adress+")")
        connList.remove(c)
        return
    print("[+] Connection from: " + alias + " ("+adress+")")
    send_to_all(alias + " ("+adress+") has joined the server")
    while True:
        try:
            data = c.recv(1024).decode("utf-8")
        except ConnectionResetError:
            print("[-] Connection lost from " + alias + " ("+adress+")")
            connList.remove(c)
            send_to_all(alias + " left the server")
            break
        if not data:
            continue
        print("[+] From "+ alias + ": " + data)
        alias_data = alias + ": " + data
        print("[+] Sending: " + data)
        send_to_all(alias_data)
    c.close()

for i in range(5):
    threading.Thread(target=Main).start()


"""if __name__ == "__main__":
    Main()"""