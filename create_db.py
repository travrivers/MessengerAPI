from rethinkdb import RethinkDB
from api.Message import MESSAGES

""" This file creates the database, establishes the connection
    and seeds with messages from the Message class """

r = RethinkDB()

r.connect("localhost", 28015).repl()


def create_db():
    r.db("test").table_create("messages").run()
    for message in MESSAGES:
        r.table("messages").insert(dict(message)).run()


create_db()

