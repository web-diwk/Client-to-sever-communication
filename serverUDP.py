# This is Server file for TCP implementation
import socket


def main(ip_addr, port, ispaid):
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # SOCK_DGRAM instead of SOCK_STREAM means that it is a UDP socket.
        # AF_INET is ipv4 address
        print("Socket created Sucessfully!!")
    except socket.error:
        print(socket.error)

    s.bind((ip_addr, port))
    # s.listen(1)
    
    # s.accept returns clients connection status and adress of client
    while True:
        connection, address = s.recvfrom(ip_addr,port)
        if connection:
            print("Connection established", address)
        while connection:
            # Enter your bill id 123456789

            connection.sendto(b"Enter Your Bill id:")
            data = connection.recvfrom(port)
            if data.decode() == "123456789":
                if (ispaid):
                    connection.sendto(b"Your bill is upto date")
                else:
                    connection.sendto(
                        b"Your bill amount is to be paid : 72$\nPress Y(to pay now)/N:")
                    # if true then send the status of bill payment and if not paid would user like to pay it now?
                    # if false check client  bill id
                    topay = connection.recvfrom(port)
                    if topay.decode() == "Y":
                        ispaid = True
                        connection.sendto(
                            b"Your bill has been paid successfully")
                    else:
                        connection.sendto(b"We will remind You again!")
                break
            else:
                connection.sendto(b"Enter Correct Id")
        connection.close()
    s.close()
    # closed the socket


if __name__ == "__main__":
    ip_addr = "localhost"
    port = 2710
    ispaid = False
    main(ip_addr, port, ispaid)


#sendto and s.recvfrom() for UDP 