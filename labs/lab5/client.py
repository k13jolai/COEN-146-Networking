import socket
import sys
import json
from sys import stdin
def client(host, clientname,  port):
	try:
		server= socket.gethostbyname(host)
	except socket.gaierror:
		print('error, no such host')
		exit(1)
	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	sock.bind((clientname, 6666))
#	sock.sendto('encoded data', (host, port))

	z=socket.gethostbyname(host)
	wdata= 'none'
	number=0
	while True:
		packet={}
		usermessage=stdin.readline()
		ptype=""
		checksum=0;
		c=0
		packet['number']=number
		while (c < len(usermessage)):
			checksum+=ord(usermessage[1])
			c+=1
		if usermessage.startswith('FIN') or usermessage.startswith('fin'):
			print('Exit command acknowledged, now exiting')
			ptype='FIN'
			packet['ptype']=ptype
			packet['checksum']=checksum
			packet['message']=usermessage
			j=(json.dumps(packet))
			k=j.encode('ascii', 'ignore')
			sock.sendto(k, (host, port))
			exit(0)
		else:
			packet['ptype']=ptype
			packet['checksum']=checksum
			packet['message']=usermessage
			j=(json.dumps(packet))
			k=j.encode('ascii', 'ignore')
			sock.sendto(k, (host, port))
			#after sending, wait for response. If ACK, proceed, if not, 
			#resend the current packet
			data, address = sock.recvfrom(2024)
			wdata=data.decode('utf-8', 'ignore')
			wdata2=json.loads(wdata)
			flag=0
			if wdata2['number'] == packet['number']:
				while flag != 3:
					print('Acknowledge for packet resend received. Resending..')
					sock.sendto(k, (host, port))
					flag+=1
			else:
				number+=1
				print('Message has successfully been sent to server...send another?')
			if flag == 3:
				print('Too many attempts to resend packet. Now exiting..')
				break
	
	sock.close()

if __name__== '__main__':
	if len(sys.argv) > 3:
		try:
			host=sys.argv[1]
			clientname=sys.argv[2]
			port=int(sys.argv[3])
			client (host, clientname,  port)
		except ValueError:
			print ('Second argument should be an integer representing port number')
	else:
		print('Usage: python3 client.py host port')

