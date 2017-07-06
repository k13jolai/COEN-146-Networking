import socket
import sys
from sys import stdin
def client(host, port):
	try:
		server= socket.gethostbyname(host)
	except socket.gaierror:
		print('error, no such host')
		exit(1)
	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
#	sock.sendto('encoded data', (host, port))
#change while condition

	print('Please input a prime number')
	a=stdin.readline()
	p= int(a)
	#b=a.encode('ascii', 'ignore')
	print('Please input a primitive root of the prime number')
	c=stdin.readline()	
	r=int(c)
	print('Please input private key 1')
	d=stdin.readline()
	alice=int(d)
	print('Please input private key 2')
	e=stdin.readline()
	bob=int(e)		
	k1=(r*alice)%p
	k2=(r*bob)%p
	ka=(k2*alice)%p
	kb=(k1*bob)%p
	print('The shared key is')
	print(ka)
	

if __name__== '__main__':
	if len(sys.argv) > 2:
		try:
			host=sys.argv[1]
			port=int(sys.argv[2])
			client (host, port)
		except ValueError:
			print ('Second argument should be an integer representing port number')
	else:
		print('Usage: python3 client.py host port')

