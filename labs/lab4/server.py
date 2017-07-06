import socket
import sys
def server(port):
	users= {}

	host='linux60816'
	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((host,port))

	print(socket.gethostname())
	print('Server established')
	data = 'none'
	wdata= 'none'
	while True:
		data, address = sock.recvfrom(2024)
		print(address)
		print('Connection established with', address)
		print('receiving data...')
		wdata=data.decode('utf-8', 'ignore')


		#First check if someone sends QUIT and dictionary is EMPTY
		if wdata.startswith('quit') or wdata.startswith('QUIT'):
			if len(users) == 0:
				print(address, ":", wdata)
				print('Exit message acknowledged, now closing server')
				break 
			else: 
				print(users[address], ":", wdata)
				del users[address]
				if len(users) == 0:
					print('Exit message acknowledged, now closing server')
					break
				else:
					print('Waiting on other users before quitting')

		if wdata.startswith('::'):
			z=wdata.lstrip(':')
			print('username confirmed as', z)
			users[address] = z
		elif wdata.startswith(';;'):
			z=wdata.lstrip(';')
			if address in users:
				print(users[address], ":", z)
			else:
				print(address, ":", z)
		else:
			print('not a valid username or message')
			continue 


#Once loop is broken out of and socket can close
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
