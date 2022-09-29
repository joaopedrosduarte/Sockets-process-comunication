import socket
import threading

PORT = 5050
FORMATO = 'utf-8'
# SERVER = "192.168.15.103"
SERVER = "172.26.13.45"
ADDR = (SERVER, PORT)

error_connection = False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def handle_mensagens():
    while(True):
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))

def enviar_mensagem():
    mensagem = input()
    enviar("msg=" + mensagem)

def enviar_nome():
    nome = input('Digite seu nome: ')
    enviar("nome=" + nome)

def iniciar_envio():
    enviar_nome()
    enviar_mensagem()

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    if(error_connection):
        print("Erro de conexão com o servidor")
    else:
        thread2.start()

iniciar()