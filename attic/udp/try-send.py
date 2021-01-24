import socket

address = ('192.168.178.50', 10086)
data = b'hello udp'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("data is type {}".format(type(data)))

sock.sendto(data, address)