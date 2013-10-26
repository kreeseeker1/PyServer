#Version 1.0
#Basic version can retrieve text-only files
#import socket module

from socket import *


serverPort = 9876

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
    #Fill in start
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
        #Fill in end

while True:

        #Establish the connection
        
        print ('Ready to serve...')
        
        connectionSocket, addr = serverSocket.accept()
        
        try:
                message = connectionSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                print('opening ' ,filename)
                outputdata = f.read()
                
                #Send one HTTP header line into socket
                        #Fill in start
                headertext = '\nHTTP/1.1 200 OK\n\n'
                print(headertext)
                connectionSocket.send(headertext.encode())
                
                        #Fill in end
                
                #Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                                
                connectionSocket.close()
                print('entire message has been sent...')
                        
        except IOError:
                  

                errormessage = '\nHTTP/1.1 404 No Page like this is to be found here\n\n'

                connectionSocket.send(errormessage.encode())
                

                connectionSocket.close()

                        
serverSocket.close()
raw_input()#keep cmd window open
