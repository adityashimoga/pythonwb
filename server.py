import socket
s=socket.socket()
s.bind(("",8080))
s.listen(2)
while True:	
	c,addr=s.accept()
	print c.read(1000)
	c.close()