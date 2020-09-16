# Writes formatted entries to a log file
# Time entries are local to the server

from datetime import datetime

def append_connection_entry(log_file, ip_address, command, data_sent):
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} <-- RECEIVE -- {ip_address} connected and issued {command}\n")
        log.write(f"{datetime.now()} -- SENT--> Server sent to {ip_address} -- {data_sent}\n")