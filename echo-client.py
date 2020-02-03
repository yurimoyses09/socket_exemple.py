import socket

HOST = '127.0.0.1'  # Endereço da interface de loopback padrão (localhost)
PORT = 65432  # Porta para escutar (portas não privilegiadas são> 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = str(input("\nDigite sua mensagem ao mundo!!: "))
    if msg == '':
        print('\nNao existe ninguem aqui!!')
    else:
        print('\nReceived message!!')
    s.sendall(b'Hello, world')
    data = s.recv(1024)
