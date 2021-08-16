import socket


ip_addr = "localhost"
port = 2710
ispaid = False

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET is ipv4
    print("Socket created Sucessfully!!")
except socket.error:
    print(socket.error)

server_socket.bind((ip_addr, port))
server_socket.listen(1)
# It returns clients connection status and address of client
while True:
    connection, address = server_socket.accept()
    if connection:
        print("Connection established", address)
        connection.send(
            b"####################----------Electricity Bill Payment System----------####################")

        # Enter your bill id 123456789

        connection.send(b"\nEnter Your Bill id:")
        while connection:
            data = connection.recv(port)
            if data.decode() == "123456789":
                if (ispaid):
                    connection.send(b"Your bill is upto date")
                else:
                    connection.send(
                        b"Your bill amount is to be paid : 72$\nPress Y(to pay now)/N:")
                    # if true then send the status of bill payment and if not paid would user like to pay it now?
                    # if false check client  bill id
                    topay = connection.recv(port)
                    if topay.decode() == "Y":
                        ispaid = True
                        connection.send(
                            b"Your bill has been paid successfully")
                    else:
                        connection.send(b"We will remind You again!")
                break
            else:
                connection.send(b"Enter Correct Id:")
        connection.close()
server_socket.close()
# closed the socket
