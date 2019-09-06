#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
print('Creating Socket')
SERVERPORT = 80
print('Creating Bind')
serverSocket.bind(('', SERVERPORT))
serverSocket.listen(10)
print('Listening For Connections')



while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('Connection Initiated with: ', addr)

    try:

        message = connectionSocket.recv(1024)
        if message != b'':
            print('The Message is: ', message)
            filename = message.split()[1]
            print('File name is: ', filename)
            f = open(filename[1:])
            outputdata = f.read()

            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

            for i in range(0,len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            print("Socket Recieved and Data Sent\r\n")
            connectionSocket.send("\r\n".encode())

    except IOError:

        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())

        connectionSocket.send('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'.encode())

        print("Socket Error and Data Sent")
        connectionSocket.close

serverSocket.close()
