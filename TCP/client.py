# This is Client file for TCP implementation
import socket

ip_addr = "localhost"
port = 2710

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # # AF_INET is ipv4
    # print("Socket creat123ed Sucessfully!!")
except socket.error:
    print(socket.error)
    exit(1)

client_socket.connect((ip_addr, port))
data = client_socket.recv(port)
print(data.decode())

# for getting correct id
data = client_socket.recv(port)
while True:
    # Enter your bill id
    # "123456789"
    client_socket.send((input(data.decode())).encode())
    data = client_socket.recv(port)
    if data.decode() != "Enter Correct Id:":
        break

print(data.decode())
# upto date or ur bill is
if data.decode() != "Your bill is upto date":
    client_socket.send((input()).encode())
    print((client_socket.recv(port)).decode())

client_socket.close()
