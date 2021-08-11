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
        # print("Socket creat123ed Sucessfully!!")
    except socket.error:
        print(socket.error)

    s.connect((ip_addr, port))
    data1=s.recv(port)
    print(data1.decode())
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
