# This is Client file for TCP implementation
import socket

ip_addr = "localhost"
port = 2710
data = None


def main():
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # # AF_INET is ipv4
        # print("Socket created Sucessfull!!")
    except socket.error:
        print(socket.error)

    s.connect((ip_addr, port))
    # for getting correct id
    while True:
        data = s.recv(port)
        # Enter your bill id
        # "123456789"
        s.send((input(data.decode())).encode())
        data = s.recv(port)
        if data.decode() != "Enter Correct Id":
            break
        print(data.decode())

    print(data.decode())
    # upto date or ur bill is
    if data.decode() != "Your bill is upto date":
        s.send((input()).encode())
        print((s.recv(port)).decode())

    s.close()


if __name__ == "__main__":
    main()


# AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses). When you create a socket, you have to specify its address family, and then you can only use addresses of that type with the socket.
#  the SOCK_STREAM socket type works like a pipe. In the Internet domain, the SOCK_STREAM socket type is implemented on the Transmission Control Protocol / Internet Protocol (TCP / IP) protocol.
# A stream socket provides for the bidirectional, reliable, sequenced, and unduplicated flow of data without record boundaries. Aside from the bidirectionality of data flow, a pair of connected stream sockets provides an interface nearly identical to pipes.

# A "socket error" indicates that data sent over the network has not arrived in time.
