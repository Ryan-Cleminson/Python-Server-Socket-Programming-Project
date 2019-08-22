#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

#Fill in start
print('Creating Socket')
print('Getting hostname')
SERVERHOST = socket.gethostname()	
SERVERPORT = 12000
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
        message = connection.recv(1024).decode('utf-8') #Fill in start          #Fill in end     
        print(message)          
        filename = message.split()[1]                 
        f = open(filename[1:])                        
        outputdata = ??? #Fill in start       #Fill in end                   
        #Send one HTTP header line into socket
        # -> Send back a responce message to computer - I think 200 OK?

        #Fill in start
        #Fill in end                
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start        
        #Fill in end
        #Close client socket
        #Fill in start
        #Fill in end            
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data                                    
