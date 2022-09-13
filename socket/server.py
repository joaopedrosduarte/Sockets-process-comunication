import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("0.0.0.0", 8080))
serv.listen((5))

while True:
        clientsocket, address = serv.accept()
        print(f"Connection from {address} has been established!")

        clientsocket.send(bytes("Welcome to the Server!", "utf-8"))
        i = 0
        while True:
                msg = clientsocket.recv(1024)
                full_msg = msg.decode("utf-8")
                
                if full_msg == "quit":
                        clientsocket.close()
                        print(f"Client {address} disconnected!\n")
                        break
                
                elif full_msg == "shutdown":
                        print(f"Client {address} disconnected!")
                        clientsocket.close()
                        print(f"Servidor foi finalizado pelo cliente {address}!\n")
                        serv.close()
                        exit(0)
                else:
                        print(f"Package {i}: {full_msg}")
                        i+=1
                

        
        


       