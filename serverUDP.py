# This is Server file for TCP implementation
import socket



def main(ip_addr, port, ispaid, servert):
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
    
    # s.accept returns clients connection status and address of client
    data, address = s.recvfrom(1024)
    if data:
        print("Connection established", address)
        # while connection:
            # Enter your bill id 123456789

    while True:
            s.sendto(b"Enter Your Bill id:",address)
            data,address = s.recvfrom(1024)
            print(data)
            if data.decode() == "123456789":
                if (ispaid):
                    s.sendto(b"Your bill is upto date",address)
                else:
                    s.sendto(
                        b"Your bill amount is to be paid : 72$\nPress Y(to pay now)/N:", address)
                    # if true then send the status of bill payment and if not paid would user like to pay it now?
                    # if false check client  bill id
                    topay,address = s.recvfrom(1024)
                    if topay.decode() == "Y":
                        ispaid = True
                        s.sendto(
                            b"Your bill has been paid successfully",address)
                    else:
                        s.sendto(b"We will remind You again!",address)
                break
            else:
                s.sendto(b"Enter Correct Id",address)
        
    s.close()
    # closed the socket


if __name__ == "__main__":
    ip_addr = "localhost"
    port = 2710
    ispaid = False
    servert=(ip_addr, port)
    
    main(ip_addr, port, ispaid,servert)


#sendto and s.recvfrom() for UDP 