# Trabalho de infra de comunicação 

Nesse repositório será exposto como ocorre os mecanismos de comunicação entre processos, buscando mostrar na perspectiva da rede, tendo como o objetivo principal apresentar como acontece essa comunicação e as possiveis variações que podem advim nesse fenômeno como falha de comunicação e erro.




# Web Socket 


## Usage

Entre na pasta do projeto:
```bash
cd Sockets-process-comunication
```
## IP
- Verificar seu endereço ip para adicionar na variavel ```SERVER``` dentro do arquivo ```client.py```
- No console Linux execute o comando “sudo ifconfig” 
- No console Windows execute o comando ipconfig


## Iniciar socket 
- Primeiramente Iniciar server =>``` python .\server.py```
- Em seguida inciar cliente =>``` python .\client.py ```( número de clientes ilimitados na conversa )
- endereços são gerenciados e mensagens são trocados normalmente

## Tratamemto de Erros / Erros
Os possíveis erros a serem testados são:
- ```Erro de Conexão``` 
- ```Erro de Envio de Pacote```
- ```Erro de Recepção de Pacote```

Para cada um dos erros existe uma flag correspondente com valor default de False que ao ser alterada simula o erro.
No caso do erro de conexão existem duas flags para simulação do erro, uma em cada arquivo portanto é necesário setar o valor destas duas,
já nos outros erros existem apenas a flag no aruivo ```server.py```

## Análise / Checklist Implementação
-  Conexão Cliente-Servidor
-  Mapeamento de conexão, armazenamento e exibição de endereçamento na conexão, requisição e envio de respotas 
  ![image](https://user-images.githubusercontent.com/76250531/193143063-a48540a0-5ddc-4bf0-9918-a778f9f28422.png)

-  Capacidade de múltiplas conexões (modelo de sala privada (grupo))
  ![image](https://user-images.githubusercontent.com/76250531/193142851-4e75c5ca-ef64-46e5-9959-0cb62b22c105.png)

-  Capacidade de envio de todas as mensagens trocadas para uma nova conexão que surgir após a troca destas
  ![image](https://user-images.githubusercontent.com/76250531/193142939-f6dfb4b1-fd5f-4c5f-9bb8-8e55899b3556.png)

-  Capacidade de simulação de erro de envio de mensagem, onde caso a flag seja setada como True, o sistema dispara a falha de onde ocoreu a falha do envio da mensagem e onde as conexões da sala não recebem esta mensagem, bloqueando função de entrega de mensagens individual e aramazenamento desta no array de mensagens arquivadas

  ![image](https://user-images.githubusercontent.com/76250531/193141893-fcdc3d87-470f-4255-9d4d-47cbbc986985.png)

-  Capacidade de simular errro de Conexão do cliente com servidor, onde ao setar a flag como True, tanto o cliente como o servidor recebem a mensagem de falha ao se conectar 

 ![image](https://user-images.githubusercontent.com/76250531/193141605-78c392d1-54ce-4dfb-85e0-6fc7c75ba597.png)
 
- Capacidade de simular Erro na recepção do pacote ou perda do pacote
  ![image](https://user-images.githubusercontent.com/76250531/193142405-f59bec66-5cf7-4e9e-8657-cbafb8dc63db.png)


