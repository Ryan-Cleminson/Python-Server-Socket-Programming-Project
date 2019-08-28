# import socket module
from socket import *
import sys, threading  # In order to terminate the program


# Class to create a new thread for each client socket connection
class ClientThread(threading.Thread):
    def __init__(self, address, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("\r\nNew connection added: ", address)

    def run(self):
        print("Connection from : ", addr)
        while True:
            try:
                message = self.csocket.recv(1024)  # Fill in start          #Fill in end
                #msg = message.decode()
                #if msg == 'bye':                   #Placeholders as they don't work for html Files
                    #break
                print(message)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()  # Stores the file content in a temporary filestate

                self.csocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())  # Sends a HTTP header line
                for i in range(0, len(outputdata)):
                    self.csocket.send(outputdata[i].encode())  # send content to the client

                self.csocket.send("\r\n".encode())
                print("Socket Recieved and Data Sent\r\n")

            except IOError:

                self.csocket.send('HTTP/1.1 404 Not Found\r\n<'.encode())
                self.csocket.send('<html><head></head><body><h1>404 Not Found<h1></body></html>\r\n'.encode())
                print("Socket Error and Data Sent")
        self.csocket.close() #closes the socket
        print("Client at ", addr, " disconnected...")
        sys.exit() # Terminate the program after sending the corresponding data has to go somewhere



serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
print('Creating Socket')

SERVERPORT = 12000
print('Creating Bind')

serverSocket.bind((gethostname(), SERVERPORT))
print('Bind Created')

print('Socket created')

serverSocket.listen(10)
print('Listening For Friends')

print('Ready to serve...')
while True:
    # Establish the connection

    connectionSocket, addr = serverSocket.accept()
    newthread = ClientThread(addr, connectionSocket)
    newthread.start()
