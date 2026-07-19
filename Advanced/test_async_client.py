import socket

def test_echo_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 25000))
    
    messages = [b'Hello', b'World', b'Test']
    
    for msg in messages:
        sock.sendall(msg)
        response = sock.recv(1024)
        print(f'Sent: {msg.decode()}')
        print(f'Received: {response.decode()}\n')
    
    sock.close()

if __name__ == '__main__':
    test_echo_server()
