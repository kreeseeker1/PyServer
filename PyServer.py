#this is version 1.0

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


        
        connectionSocket, addr = serverSocket.accept()#Fill in start   #Fill in end
        print('connection made.....')
        
        try:
                message = connectionSocket.recv(1024)#Fill in start   #Fill in end
                filename = message.split()[1]
                f = open(filename[1:])
                
                outputdata = f.read()#Fill in start   #Fill in end
                
                print(outputdata)
                print(filename)
                print(message)
                
                #Send one HTTP header line into socket
                        #Fill in start   
                header = '\nHTTP/1.1 200 OK\n\n'
                connectionSocket.send(header.encode())
                
                
                         #Fill in end
                
                #Send the conent of the requested file to the client    
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                    print(outputdata[i].encode())
                        
                connectionSocket.close()
                print('Finished......')
                        
        except IOError:
                #Send response message for file not found
                        #Fill in start
                print('404 ERROR')
                error404 = '\nHTTP/1.1 404 Not Found\n\n'
                
                connectionSocket.send(error404.encode())
               
                       #Fill in end
                        
                        #Close client socket
                        #Fill in start
                
                connectionSocket.close()
        except OSError:
               print('OS Error')
                        #Fill in end
                        
serverSocket.close()
