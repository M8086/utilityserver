# utilityserver
A TCP client/server written in Python 3 using zmq sockets

A client connecting to the server can do the following things:
* Get their time and timezone based on their public IPv4 address
* Get their public IPv4 address
* Ask a magic 8 ball a question
* Sign a guestbook that has the entries stored in an sqlite db

Run the server by providing the local IP and port to bind to.

Example:
```Python
Python3 utility_server.py 127.0.0.1 5000
```
Run the client by specifying the server IP and port to connect to.

Example:
```Python
Python3 utility_client.py 10.0.0.1 5000
```
The server offers some basic logging that will be stored to the log folder.

Make sure to run the init_db.py script in the server/db folder to get the sqlite db setup for using the guestbook.

Be sure to install the zmq library
```Python
pip install pyzmq
```
