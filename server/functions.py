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

#As funções abaixo trata especificamente do envio de dados entre a EC2 do consumer e a EC2 do jogo
def send_data(data, IP_EC2):
    serialized_data = json.dumps(data)
    client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    client_socket.connect((IP_EC2, 5000))
    client_socket.send(serialized_data.encode())
    client_socket.close()
