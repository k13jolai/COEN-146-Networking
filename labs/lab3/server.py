import socket
import sys
def server(port):
	host=socket.gethostname()
	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((host,port))

	print(socket.gethostname())
	print('Server established')
	data = 'none'
	wdata= 'non'
	while wdata != ' ':
		data, address = sock.recvfrom(2024)
		print('Connection established with', address)
		print('receiving data...')
		print('Server received', repr(data))

		fname='testfile.txt'
		f=open(fname, 'a')
		wdata=data.decode('utf-8', 'ignore')
		f.write(wdata)
		f.close()


		print('Successfully got the file!')
	sock.close()
if __name__ == '__main__':
	if len (sys.argv) > 1:
		try:
			port = int(sys.argv[1])
			server (port)
		except ValueEror:
			print ('Usage python3 server.py port\nport must be an int')
			sys.exit(0)
	else:
		print ('Usage: python3 server.py port')
