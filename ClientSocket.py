import socket
import sys


HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

# Bind socket to local host and port

#try:
#    s.bind((HOST, PORT))
#except socket.error as msg:
#    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
#    sys.exit()
#
#print ('Socket bind complete')

#s.listen(10)
print ('Socket now listening')
s.connect(("IN-7PP8PC2-10",8888))

# What is str in python

data= 'foobar\n' * 10 * 1024 * 1024
#data ="Hello umesh"
assert s.send(str.encode(data))