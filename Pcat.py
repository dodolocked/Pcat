#你一定是脑子有病，非要自己折腾个工具出来
#我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道怎么写，我也不知道
#轮子都不会造怎么造车！！！滚去学！！
import socket
import threading
import time
class senderhead:
    senderheader = ""
    jumper = None
    def __init__(self,senderheader):
        self.senderheader = senderheader
        self.jumper = False
    def get_senderheader(self):
        return self.senderheader
    def set_senderheader(self,senderheader):
        self.senderheader = senderheader
    def get_jumper(self):
        return self.jumper
    def jumper_settrue(self):
        self.jumper = True
    def jumper_setfalse(self):
        self.jumper = False
def handle_client(client_socket,seherder):
    while True:
        data = client_socket.recv(2048)
        if seherder.get_jumper() == False:        
            data = data.replace(b"\n",b"   ")
            data = data.decode('utf-8')
            if "]#" in data:
                seherder.set_senderheader(data)
            else:
                print(data)
        else:
            if "\n" in data.decode('utf-8'):
                seherder.jumper_setfalse()
def handle_client_sender(client_socket,seherder):
    while True:
        cmd = input(seherder.get_senderheader()).encode('utf-8')
        cmd += b"\r"
        client_socket.send(cmd)
        seherder.jumper_settrue()
        time.sleep(1)
def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address[0]}")
    senderheader = client_socket.recv(2048)
    senderheader = client_socket.recv(2048).decode('utf-8')
    seheader = senderhead(senderheader)
    client_handler = threading.Thread(target=handle_client, args=(client_socket,seheader))
    client_sender = threading.Thread(target=handle_client_sender,args=(client_socket,seheader))
    client_handler.start()
    client_sender.start()
if __name__ == "__main__":
    server_host = "0.0.0.0" 
    server_port = 5555  

    start_server(server_host, server_port)