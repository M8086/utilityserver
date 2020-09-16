# utilityserver
A TCP client/server writting in Python 3 using zmq sockets

A client connecting to the server can do the following things:
* Get their time based on their public IPv4 address
^ Get their public IPv4 address
* Ask a magic 8 ball a question
* sign a guestbook that has the entries stored in an squlite db

Run the server by providing the local IP and port to bind to

Example:
```Python
Python3 utility_server.py 127.0.0.1 5000
```
Run the client by specifying the server IP and port to connect to

```Python
Python3 utility_client.py 10.0.0.1 5000
```
