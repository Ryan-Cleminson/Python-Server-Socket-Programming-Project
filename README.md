# Python-Server-Socket-Programming-Project
In this assignment, I use the basics of socket programming for TCP connections in Python: creating a socket, binding it to a specific address and port, as well as send and receive a HTTP packet. Basic HTTP header formats are used to display the relevnat page elements to the user.
This web server has been created to handle one HTTP request at a time. The web server accepts and parses the HTTP request, gets the requested file from the server’s file system, creates a HTTP response message consisting of the requested file preceded by header lines, and then send the relevant response directly to the client. 
Should the requested file not be present in the server, the server will send an HTTP “404 Not Found” message back to the client.
