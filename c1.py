import socket
import exp_mod

puerto = raw_input("puerto: ")
n = raw_input("n: ")
g = raw_input("g: ")
x = raw_input("x: ")

tempa = exp_mod.exp_mod(long(g),long(x),long(n) )
cat1= n+','+g+','+str(tempa)

miSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
miSocket.connect( ("", int(puerto) ) )

print "[ enviando: " + cat1 + "]"
miSocket.send(cat1)	

data, server = miSocket.recvfrom( 100 )

print data
clave = exp_mod.exp_mod(long(data),long(x),long(n))


print clave

	


#miSocket.close()
