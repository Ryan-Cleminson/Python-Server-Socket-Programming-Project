#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#assign a port number
print('Creating Socket')
SERVERPORT = 80
print('Creating Bind')
serverSocket.bind(('', SERVERPORT))#attain and bind serverr address with port number
serverSocket.listen(10)
print('Listening For Connections')



while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #establish connection
    print('Connection Initiated with: ', addr)

    try:

        message = connectionSocket.recv(1024) #receives the request message from the client
        if message != b'':
            print('The Message is: ', message)
            filename = message.split()[1]#extract the second part of HTTP header identiﬁed by [1]
            print('File name is: ', filename)
            f = open(filename[1:]) # because the second part of the HTTP header includes a '/', 
            #this instructs to read from the second character expressed through 
            outputdata = f.read()#store the entire content of the requested ﬁle in a temporary buﬀer

            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())#Send a HTTP header line

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
#Terminate the program after sending the corresponding data  
