#import socket module
from socket import *
import sys # In order to terminate the program

#Prepare a sever socket
#Fill in start
print('Creating Socket')
SERVERHOST = '10.0.0.147'	
SERVERPORT = 12000	
serverSocket = socket(AF_INET, SOCK_STREAM)
print('Socket created')
print('Creating Bind')
serverSocket.bind((SERVERHOST, serverPort))
print('Bind Created')
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =   #Fill in start              #Fill in end          
    try:
        message =   #Fill in start          #Fill in end               
        filename = message.split()[1]                 
        f = open(filename[1:])                        
        outputdata = #Fill in start       #Fill in end                   
        #Send one HTTP header line into socket
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
