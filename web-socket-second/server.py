import socket
import threading
import time

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050 # 8080 ou 5050 
ADDR = (SERVER_IP, PORT) # usado para fazer o srver bind 
FORMATO = 'utf-8' # formato usado para decodificar a mensagem

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # servidor(classe do socket,  tipo de entrada e saida)
server.bind(ADDR)

conexoes = []
mensagens = []

error_send_message= False
error_connection = False
error_recepcao = True

def enviar_mensagem_individual(conexao): #envia mensagem para uma pessoa
    if(error_recepcao):
            print(f"Falha no envio dos pacotes pelo usuário {conexao['addr']}")
    else:
        print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
        for i in range(conexao['last'], len(mensagens)):
            mensagem_de_envio = "msg=" + mensagens[i]
            conexao['conn'].send(mensagem_de_envio.encode())
            conexao['last'] = i + 1
            time.sleep(0.2)

def enviar_mensagem_todos(): # envia mensagem para todas as pessoas
    global conexoes
    if(error_send_message):
        print("falha no envio da mensagem")
    else:
        for conexao in conexoes:
            enviar_mensagem_individual(conexao)

"""
1 vez que o cliente entrar, vai mandar o nome:
nome=.....
E as mensagens vem:
msg=
"""

def handle_clientes(conn, addr):#lidamos com clientes, recebemos suas mensagens e mandamos para todos os clientes
    if(error_connection):
        print(f"Erro ao se conectar com usuario de endereço {addr}")
    else:
        print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}")#mensagem nova conexão com endereçamento
        global conexoes # vAariavel global conexão
        global mensagens# variavel global mensagens
        nome = False # inicializa nome como false

        while(True): #espera mensagem do cliente
            msg = conn.recv(1024).decode(FORMATO) # 1024 tamanho maximo da msg e decodifica em uft8
            if(msg):# se a mensagem nao for nula
                if(msg.startswith("nome=")): # se a mensagem for nome 
                    mensagem_separada = msg.split("=")# seprando string a partir do igual
                    nome = mensagem_separada[1] # pegando apenas nome que ta na posição 1 do array
                    mapa_da_conexao = {#adiciona atributos da conexão
                        "conn": conn,
                        "addr": addr,
                        "nome": nome,
                        "last": 0
                    }
                    conexoes.append(mapa_da_conexao)#adiciona conexão
                    enviar_mensagem_individual(mapa_da_conexao)
                elif(msg.startswith("msg=")):# se for uma mensagem
                    mensagem_separada = msg.split("=")#separa para pegar mensagem
                    mensagem = nome + "=" + mensagem_separada[1]#
                    mensagens.append(mensagem)
                    enviar_mensagem_todos()



def start():
    print("[INICIANDO] Iniciando Socket") # mensagem de inicialização 
    server.listen()#servidor ouvindo cliente
    while(True):#while true para ele nunca sair do loop
        conn, addr = server.accept() # aguarda conexão de cliente infinitamente, quando conecta passa para comnado abaixo (conexão, endereço)
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))#criando thread para conexão estabelecida
        thread.start()#inicia thread

start()