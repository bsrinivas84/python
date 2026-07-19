import asyncio

async def echo_handler(client, loop):
    """Handle a single client connection."""
    while True:
        data = await loop.sock_recv(client, 10000)
        if not data:
            break
        await loop.sock_sendall(client, b'Got:' + data)
    print('Connection closed')
    client.close()


async def echo_server(address):
    """Echo server that accepts connections and echoes back data."""
    import socket
    loop = asyncio.get_event_loop()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    
    while True:
        client, addr = await loop.sock_accept(sock)
        print(f'Connection from {addr}')
        loop.create_task(echo_handler(client, loop))


if __name__ == '__main__':
    asyncio.run(echo_server(('', 25000)))
