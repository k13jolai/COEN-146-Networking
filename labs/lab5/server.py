import socket
import sys
import json
from sys import stdin
def server(host, sendto, port):
	users= {}

	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((host,port))

	print(socket.gethostname())
	print('Server established')
	data = 'none'
	wdata= 'none'
	while True:
		packet={}
		ptype='ACK'
		checksum=0
		data, address = sock.recvfrom(2024)
		print(address)
		print('Connection established with', address)
		print('receiving data...')
		wdata=data.decode('utf-8', 'ignore')
		packet=json.loads(wdata)
		#CHECK CHECKSUM
		sentmessage=packet['message']
		s=0
		while (s< len(sentmessage)):
			checksum+=ord(sentmessage[1])
			s+=1
		if checksum != int(packet['checksum']):
			print('Incorrect checksum detected')
			j=(json.dumps(packet))
			k=j.encode('ascii', 'ignore')
			sock.sendto(k, (sendto, 6666))
			continue
		#First check if someone sends QUIT and dictionary is EMPTY
		if sentmessage.startswith('fin') or sentmessage.startswith('FIN'):
			print('Exit message acknowledged, now closing server')
			break
		else:
			print('{}: {}'.format(packet['number'], packet['message']))
			packet['number']=int(packet['number'])+1
			j=(json.dumps(packet))
			k=j.encode('ascii', 'ignore')
			sock.sendto(k, (sendto, 6666))

#Once loop is broken out of and socket can close
	sock.close()



	
if __name__ == '__main__':
	if len (sys.argv) > 3:
		try:
			host=sys.argv[1]
			sendto=sys.argv[2]
			port = int(sys.argv[3])
			server (host, sendto, port)
		except ValueError:
			print ('Usage python3 server.py port\nport must be an int')
			sys.exit(0)
	else:
		print ('Usage: python3 server.py port')
