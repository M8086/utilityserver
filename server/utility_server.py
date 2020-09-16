# utility_server.py - a TCP server that
# returns helpful and fun information requested by a client
# gives time based on user's IP address, a random 8-ball answer
# or the user's IP address
# includes a guestbook that saves entries to a sqlite db file
# a throwback to those guestbooks that were on every website

from send_commands import send_data
import zmq
import sys

# make sure an IPv4 address and port is specified for the socket to bind to
if (len(sys.argv) != 3):
    print("Need IPv4 address and port to bind to.")
    sys.exit()

# store IP and Port and setup TCP socket
ip_address = sys.argv[1]
port = int(sys.argv[2])
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind(f"tcp://{ip_address}:{port}")

# all the work is in a while loop so that
# the server does not close when a client disconnects
# consider running the server with & at the end of the command
# to run the server in the background
while True:

    # zmq takes care of receiving large items
    # no max size required like with standard sockets
    cmd_as_bytes = server.recv()
    cmd = cmd_as_bytes.decode("utf-8")

    # split the string provided and build
    # a dictionary with predictable locations
    # for the items
    # the dictionary will be passed to various functions
    # check out send_commands.py for more information
    arg_list = cmd.split(" ")
    args = {}
    args["command"] = arg_list[0]
    args["params"] = arg_list[1:-1]
    args["ip_address"] = arg_list[-1]
    args["socket"] = server
    
    # send the command to the client
    # see the send_commands.py module for more information
    send_data(**args)
