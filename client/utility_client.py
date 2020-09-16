# tcp client for utility server

# import socket
import zmq
import sys
import urllib.request

# make sure user is specifying server IP and port to connect to
if (len(sys.argv) != 3):
    print("usage: time_client.py IPv4_Address Port")
    sys.exit()

# python sockets could send the server the client's public IPv4 address
# zmq sockets cannot do this
# to retain functionality for the commands
# we can quickly grab the public facing IPv4 address
# and encode it for transfer
# a space is placed at the beginning so that the IP can be split
# into a command list on the server when the command is received
public_ip = urllib.request.urlopen("http://icanhazip.com").read()
ip_str = f" {bytes.decode(public_ip)}".strip('\n')

# get connection parameters and establish a connection to the server
ip_address = sys.argv[1]
port = int(sys.argv[2])
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect(f"tcp://{ip_address}:{port}")
client.setsockopt(zmq.LINGER, 0)

while True:
    try:
        # get command from user and append
        # ip address to the end
        # encode the string for transfer
        cmd = input("enter a command: ")
        cmd += ip_str
        cmd_bytes = cmd.encode("utf-8")

        if cmd.lower().startswith("quit"):
            print("Goodbye!")
            sys.exit()
        
        # send the encoded command
        # begin polling
        # if nothing is received for 10 seconds
        # raise an exception
        client.send(cmd_bytes)
        poller = zmq.Poller()
        poller.register(client, zmq.POLLIN)
        if poller.poll(10*1000): # 10s timeout in milliseconds
            reply_bytes = client.recv()
            print(reply_bytes)
            reply_as_str = reply_bytes.decode("utf-8")
            print(f"{reply_as_str}")
        else:
            raise IOError("Server could not receive command. Disconnecting.")
    # the connection timed out
    # cleanup and exit indicating failure
    except IOError as io:
        print(io)
        client.close()
        context.term()
        sys.exit(-1)