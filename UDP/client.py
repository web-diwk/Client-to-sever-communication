import socket
BUFFER_SIZE = 102400


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(1.0)

message = b'Hello Server!'
addr = ("127.0.0.1", 12000)

client_socket.sendto(message, addr)

# try:
data, address = client_socket.recvfrom(BUFFER_SIZE)
print(data.decode())
data, address = client_socket.recvfrom(BUFFER_SIZE)
while True:
    client_socket.sendto((input(data.decode())).encode(), address)
    data, address = client_socket.recvfrom(BUFFER_SIZE)
    if data.decode() != "Enter Correct Id:":
        break

print(data.decode())
# upto date or ur bill is
if data.decode() != "Your bill is upto date":
    client_socket.sendto((input()).encode(), address)
    print((client_socket.recvfrom(BUFFER_SIZE))[0].decode())

# except socket.timeout:
#     print('REQUEST TIMED OUT')

client_socket.close()
