import argparse
import string
import random
import math

def generate_file(file_name):
	with open(file_name,'w', encoding='utf-8') as f:
		x=string.printable
	#	random.seed(99)
		for r in range(0, 280):
			y=random.randint(0, 99)
			z=str(x[y])
			f.write(z)
	f.close()
	print('Generate file: ', file_name)




def calculate_entropy(file_name):
	with open(file_name, 'rb') as f:
		byteArr = bytearray(f.read())
	fileSize = len(byteArr)	
	f.close()

	freqList=[]
	for b in range(256):
		ctr=0
		for byte in byteArr:
			if byte == b:
				ctr +=1
			freqList.append(float(ctr) / fileSize)
	ent = 0.0
	for f in freqList:
		if f>0:
			freq=float(f) / fileSize
			ent=ent+freq*math.log(freq, 2)
	ent = -ent
	print('Shannon entropy:', ent) 
	print ('Calculate Entropy: ', file_name)







## DO NOT NEED TO EDIT ANYTHING UNDER HERE
# setup command line options
parser = argparse.ArgumentParser(description='Generate a random file and calculate its Shannon Entropy')
parser.add_argument('-e', '--execute', dest='fxn', help='Function to be executed: calcaulte, generate, main')
parser.add_argument('-f', '--file', default='lab6.txt', dest='file_name', help='File to either calculate entropy or generate into')

args = parser.parse_args()

if args.fxn == 'generate':
    generate_file(args.file_name)
elif args.fxn == 'calculate':
    calculate_entropy(args.file_name)
elif args.fxn == 'main':
    generate_file(args.file_name)
    calculate_entropy(args.file_name)
else:
    parser.print_help()

