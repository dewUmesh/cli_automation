import socket
import sys

HOST = 'IN-7PP8PC2-10'  # Symbolic name, meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ( 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ('Socket bind complete')

# Start listening on socket
s.listen(10)
print ('Socket now listening')

# now keep talking with the client
try:
    while 1:
        # wait to accept a connection - blocking call
        conn, addr = s.accept()
        data = conn.recv(1024)
        print ('Connected with ' + addr[0] + ':' + str(addr[1]))
        while data :
            print(data)
            data = conn.recv(1024)

except KeyboardInterrupt :
    s.close();

