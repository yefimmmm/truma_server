# import socket
# import os
# from _thread import *

# ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = "localhost"
# port = 5000
# ServerSocket.bind((host, 5000))
# ServerSocket.listen(25)




# def multi_thread_client(conn):
#     data = conn.recv(2048)
#     response = (data.decode('utf-8'))

#     # conn.send(response.encode())
#     print(response)

#     conn.close()




# while True:
#     Client, address = ServerSocket.accept()
    
#     print('Connected to: ' + address[0] + ':' + str(address[1]))

#     start_new_thread(multi_thread_client, (Client, ))


# ServerSocket.close()

import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print("Received message from client:", message)  # Print the received message
        await websocket.send(message)  # Echo the message back to the client

async def main():
    async with websockets.serve(echo, "localhost", 5000):
        await asyncio.Future()  # Run forever

asyncio.run(main())