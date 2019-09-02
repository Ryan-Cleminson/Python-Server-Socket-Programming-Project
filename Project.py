# import socket module
from socket import *
import sys, threading  # In order to terminate the program


# Class to create a new thread for each client socket connection
class ClientThread(threading.Thread):
    def __init__(self, address, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.caddr = address
        print("\r\nNew connection added: ", self.caddr )

    def run1(self):
        print("Connection from : ", self.caddr )
        while True:
            try:
                message = self.csocket.recv(1024)  # this line is to transmit the request message from the client
                message = message.decode()
                #if msg == 'bye':                   #Placeholders as they don't work for html Files
                    #break
                print(message)
                filename = message.split()[1] #contain the 2nd point of the header of the HTTP found by [1]
                
                f = open(filename[1:]) # because the second part of the HTTP header includes a '/', this instructs to read from the second character expressed through '[1:]'                      !

                outputdata = f.read()  # Stores the file content in a temporary filestate

                self.csocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())  # Sends a HTTP header line
                for i in range(0, len(outputdata)): #send content to the client
                    self.csocket.send(outputdata[i].encode())  # send content to the client

                self.csocket.send("\r\n".encode())
                
                print("Socket Recieved and Data Sent\r\n")
                connectionSocket, addr = serverSocket.accept()
                newthread = ClientThread(addr, connectionSocket)
                newthread.run1()

            except IOError:

                self.csocket.send('HTTP/1.1 404 Not Found\r\n<'.encode()) # if error in the socket 
                self.csocket.send('<html><head></head><body><h1>404 Not Found<h1></body></html>\r\n'.encode())
                self.csocket.close() #closes the socket
                print("Socket Error and Data Sent")
        self.csocket.close() #closes the socket
        print("Client at ", self.caddr, " disconnected...")
        sys.exit() # Terminate the program after the data is sent 



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

while True:
    # Establish the connection
    # Written by Ryan, Tylar and Aayush
    print('Ready to serve...1')

    connectionSocket, addr = serverSocket.accept()
    newthread = ClientThread(addr, connectionSocket)
    newthread.run1()
    print('Ready to serve...2')
    