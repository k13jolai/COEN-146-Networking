import socket
import sys
def client(host, port, file_name):
	try:
		server= socket.gethostbyname(host)
	except socket.gaierror:
		print('error, no such host')
		exit(1)
	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
#	sock.sendto('encoded data', (host, port))

	with open(file_name,'r') as f:
		for line in f:
			x=line.encode('ascii', 'ignore')
			sock.sendto(x, (host, port))
	
	y=' '
	x=y.encode('ascii', 'ignore')
	sock.sendto(x, (host, port))
	f.close()
	sock.close()

if __name__== '__main__':
	if len(sys.argv) > 2:
		try:
			host=sys.argv[1]
			port=int(sys.argv[2])
			file_name = sys.argv[3]
			client (host, port, file_name)
		except ValueError:
			print ('Second argument should be an integer representing port number')
	else:
		print('Usage: python3 client.py host port')

