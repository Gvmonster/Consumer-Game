import socket as sk
import json
from threading import Thread

#As funções abaixo se referem a configuração do servidor
def startServer():
    address = ('', 1234)
    connection = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    connection.bind(address)
    connection.listen(4)

    while True:
        userConnection, userAddress = connection.accept()
        threadConnection = Thread(target=handle, daemon=True, args=(userConnection,))


def handle(connection):
    pass

#As funções abaixo trata especificamente do consumo de dados entre enviados pela EC2 do producer
def receive():
    server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))  
    server_socket.listen(1)

    print("Servidor aguardando conexão...")
    conn, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")

    data = conn.recv(1024).decode()
    dicionario = json.loads(data)
    print("Dados recebidos:", dicionario)

    conn.close()
    server_socket.close()
