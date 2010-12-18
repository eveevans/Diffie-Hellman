import socket
import exp_mod

puerto = raw_input("puerto: ")
y = raw_input("y: ")

print "[ Escuchando::::: ]"

miSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
miSocket.bind( ("", int(puerto) ) )
miSocket.listen( 1 )

while 1:
	channel, details = miSocket.accept()
	recibido=channel.recv(1024)
 	print "Se\ ha conectado %s" % (str(details))
	
	#0,1,2	
	#n,g,g^x mod n
	val= recibido.split(",")	
	print val

	env=exp_mod.exp_mod(long(val[1]),long(y),long(val[0]) )	
	print str(env) 	
	channel.send(str(env))
	
	clave = exp_mod.exp_mod(long(val[2]),long(y),long(val[0]))	
	print clave

	#channel.close()
