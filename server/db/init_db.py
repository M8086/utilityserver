# creates a guestbook.db file in this folder
# guestbook.db needs to be created for !sign and !read commands
# otherwise they will notify the user that the db file has not been created
# this script will attempt to warn you if a guestbook.db file exists already
# BUT IT WILL HAPPILY OVERWRITE IT IF YOU TELL IT TO (you have been warned)

import sqlite3
import os
from sys import exit

def create_db():
    conn = sqlite3.connect("guestbook.db")
    cur = conn.cursor()
    # sqlite apparently does not care about the number
    # parameter in varchar and it is safe to use for long strings
    # I have to admit I just saw the number 20 in a book I was reading
    cur.execute("""CREATE TABLE guests
    (time VARCHAR(20) PRIMARY KEY,
     message VARCHAR(20))""")
    cur.close()
    conn.close()

# this is the only place in this program with a nasty if-else tree :)
if os.path.exists("guestbook.db"):
    overwrite_choice = input("guestbook.db exists. Overwrite (y/n)?: ")
    if overwrite_choice.lower().startswith('n'):
        exit()
    else:
        confirm = input("Please type 'delete' to DELETE AND RECREATE guestbook.db")
        if confirm == "delete":
            os.remove("guestbook.db")
            create_db()
        else:
            print("database kept")
            exit()
else:
    create_db()


