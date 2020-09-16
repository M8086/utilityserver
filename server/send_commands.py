# Module for sending data to the client based
# on the command they send to the server

import zmq
import get_time
import magic_eight
import guestbook
from logging import append_connection_entry

def return_ipv4_address(**kwargs):
    address = kwargs["ip_address"]
    return address

# supported commands with their respective functions
SUPPORTED_COMMANDS = {
    "ip" : return_ipv4_address,
    "time" : get_time.current_time,
    "!eight" : magic_eight.eight_ball,
    "!sign" : guestbook.sign_guestbook,
    "!read" : guestbook.read_guestbook,
}

# send data takes a dictionary of arguments
# the command will always be in the param_0 key
# the function then checks that the command exists
# in the SUPPORTED_COMMANDS keys
# and if it does it called the key's respective function
# and sends the return value of that function to the client
# send an error if the client requests a command that isn't supported
# return the data send to the client for logging purposes
def send_data(**kwargs):
    socket = kwargs["socket"]
    cmd = kwargs["command"]
    try:
        if cmd.lower() in SUPPORTED_COMMANDS.keys():
            data_str = SUPPORTED_COMMANDS[cmd](**kwargs)
            data_bytes = bytes(data_str, "utf-8")
            socket.send(data_bytes)
            append_connection_entry("log/log.txt", kwargs["ip_address"], kwargs["command"], data_str)          
        else:
            socket.send(b"I only respond to 'time', 'ip', '!eight', '!sign', or '!read'.")
    except guestbook.dbNotFound:
        socket.send(b"It looks like the admin hasn't setup the guestbook.")
        db_not_setup_err = "ERROR - guestbook.db has not been created, please run init_db.py"
        append_connection_entry("log/log.txt", kwargs["ip_address"], db_not_setup_err, data_str)          