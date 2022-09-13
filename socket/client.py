import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.10", 8080))


full_msg = ''
msg = client.recv(1024)
print(msg.decode("utf-8"));
while True:
	if len(msg) <= 0:
		break
	full_msg += msg.decode("utf-8")
 
	while True:
		enviar = input()
		client.send(bytes(enviar, "utf-8"))
		if enviar == "quit":
			exit(0)
		elif enviar == "shutdown":
			exit(0)

print(full_msg)


               