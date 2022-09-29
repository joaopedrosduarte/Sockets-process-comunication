# Trabalho de infra de comunicação 

Nesse repositório será exposto como ocorre os mecanismos de comunicação entre processos, buscando mostrar na perspectiva da rede, tendo como o objetivo principal apresentar como acontece essa comunicação e as possiveis variações que podem advim nesse fenômeno como falha de comunicação e erro.




# Web Socket Second Version


## Usage

Entre na pasta do projeto:
```bash
cd Sockets-process-comunication
```
##
- Verificar seu endereço ip para adicionar na variavel ```SERVER``` dentro do arquivo ```client.py```


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
