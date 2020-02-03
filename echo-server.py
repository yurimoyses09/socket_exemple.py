import socket

HOST = '127.0.0.1'  # Endereço da interface de loopback padrão (localhost)
PORT = 65432        # Porta para escutar (portas não privilegiadas são > 1023)

# Os argumentos transmitidos ao socket () especificam a família de endereços e o tipo de socket.
# AF_ANET -> família de endereços da Internet para IPv4. SOCK_STREAM é o tipo de soquete para TCP,
# o protocolo que será usado para transportar nossas mensagens na rede;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind () -> é usado para associar o soquete a uma interface de rede e número de porta específico;
    # Os valores passados para bind () dependem da família de endereços do soquete;
    # Estamos usando o socket.AF_INET (IPv4). Portanto, espera uma tupla de 2: (host, porta);
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()  # accept () bloqueia e aguarda uma conexão de entrada.
    with conn:
        print('Conneted by', addr)
        while True:
            data = conn.recv(1024)
            if not data:  # Se conn.recv () retornar um objeto de bytes vazios, b '', o cliente fechará a conexão e o
                # loop será encerrado
                break
            conn.sendall(data)  # Isso lê todos os dados que o cliente envia e os repete usando conn.sendall ()
