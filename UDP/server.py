import socket

BUFFER_SIZE = 102400
ispaid = False

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print(socket.error)

server_socket.bind(('', 12000))

print("UDP server started runningy!!")

while True:
    message, address = server_socket.recvfrom(BUFFER_SIZE)
    print("receiving data from ", address)
    # message=Hello Server
    server_socket.sendto(
        b"####################----------Electricity Bill Payment System----------####################", address)
    server_socket.sendto(b"Enter Your Bill id:", address)
    while True:
        message, address = server_socket.recvfrom(BUFFER_SIZE)
        if message.decode() == "123456789":
            if (ispaid):
                server_socket.sendto(b"Your bill is upto date", address)
            else:
                server_socket.sendto(
                    b"Your bill amount is to be paid : 72$\nPress Y(to pay now)/N:", address)
                # if true then send the status of bill payment and if not paid would user like to pay it now?
                # if false check client  bill id
                topay, address = server_socket.recvfrom(BUFFER_SIZE)
                if topay.decode() == "Y":
                    ispaid = True
                    server_socket.sendto(
                        b"Your bill has been paid successfully", address)
                else:
                    server_socket.sendto(b"We will remind You again!", address)
            break
        else:
            server_socket.sendto(b"Enter Correct Id:", address)
server_socket.close()
