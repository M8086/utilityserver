# guestbook module storing entries in sqlite db
# time entries are local to the server
# make sure to run init_db.py in the db folder
# or the !sign and !read commands will notify the client 
# that the db file does not exist

import sqlite3
import os
from datetime import datetime

class dbNotFound(Exception):
    pass

def sign_guestbook(**kwargs):
    if os.path.exists("db/guestbook.db") == False:
        raise dbNotFound
        return

    conn = sqlite3.connect("db/guestbook.db")
    cur = conn.cursor()
    
    time = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    message = " ".join(kwargs["params"])
    entry = (time, message)
    cur.execute('INSERT INTO guests(time, message) VALUES(?, ?)', entry)

    conn.commit()
    return "Thanks for signing!"

def read_guestbook(**kwargs):
    if os.path.exists("db/guestbook.db") == False:
        raise dbNotFound
        return
    
    conn = sqlite3.connect("db/guestbook.db")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM guests")
    rows = cur.fetchall()

    # magic to send the entire guestbook back to the client as a single string
    entry = "(Server's) Time\t    Name(optional)/Message\n"
    for el in rows:
        entry += f"{' '.join(el)}"
        entry += '\n'
    
    cur.close()
    conn.close()
    return entry