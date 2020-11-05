from rethinkdb import RethinkDB
from app.Message import MESSAGES

""" This file creates the database, establishes the connection
    and seeds with messages from the Message class """

r = RethinkDB()

r.connect("database", 28015).repl()


def create_db():
    r.db("test").table_create("messages").run()
    for message in MESSAGES:
        r.table("messages").insert(dict(message)).run()
    print("*Hooray, database created*")


create_db()

