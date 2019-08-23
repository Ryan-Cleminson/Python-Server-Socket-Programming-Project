#import socket module!
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket

#Fill in start
print('Creating Socket')
print('Getting hostname')
SERVERHOST = socket.gethostname()	
SERVERPORT = 12000
serverSocket.bind((",serverPort)) # obtain and bind server addresses to the port number! 
print('Socket created')

print('Creating Bind')
serverSocket.bind((SERVERHOST, SERVERPORT))
print('Bind Created')

serverSocket.listen(1)
print('Listening For Friends')
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start              #Fill in end          
    try:
        message = connectionSocket.recv(1024) #Fill in start          #Fill in end     
        print(message)          
        filename = message.split()[1]                 
        f = open(filename[1:])             
        outputdata = f.read() #Fill in start # stores the content of the file requested in a temporary filestate
                   #Fill in end
                           #Send one HTTP header line into socket
                   connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode()) #Sends a HTTP header line ! 
                   ! for i in range(0, len(outputdata)):!
                   #send content to the client 
                   connectionSocket.send(outputdata[i].encode())! 
                   connectionSocket.send("\r\n".encode())! 
                   connectionSocket.close()! 
                   !
except IOError:!
                           #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!
doctype html><html><body><h1>404 Not Found &#9785<h1></body></html>')!
        connectionSocket.close()  !
               !
                               #Close client socket
serverSocket.close()!
connectionSocket.close()!
sys.exit() #Terminate the program after sending the corresponding data                                   
