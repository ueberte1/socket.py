import socket
SERVER_IP = '192.168.56.1'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('server listen.....')
    s.listen(1)
    conn, addr = s.accept()
    print(f'connected to {addr}')  # Corrigido para "connected"

    with conn:
        while True:
            conn.send(b'Hello World')
            break
