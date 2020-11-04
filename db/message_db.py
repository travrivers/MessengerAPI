from rethinkdb import RethinkDB

from api.Message import Message
from api.MessageQuery import MessageQuery

r = RethinkDB()
r.connect("localhost", 28015).repl()


def get_data(query: MessageQuery = None):
    data = []

    if query.sender_id == None and query.recepient_id == None:
        cursor = (
            r.table("messages")
            .filter(r.now() - r.row["date"] < (60 * 60 * 24 * 30))
            .run()
        )
        for message in cursor:
            data.append(message)
        return data[:100]

    if query.sender_id and query.recepient_id:
        cursor = (
            r.table("messages")
            .filter(
                (r.row["sender_id"] == query.sender_id)
                & (r.row["recepient_id"] == query.recepient_id)
                & (r.now() - r.row["date"] < (60 * 60 * 24 * 30))
            )
            .run()
        )

        for message in cursor:
            data.append(message)
        return data[:100]

    if query.sender_id:
        cursor = (
            r.table("messages")
            .filter(
                (r.row["sender_id"] == query.sender_id)
                & (r.now() - r.row["date"] < (60 * 60 * 24 * 30))
            )
            .run()
        )

        for message in cursor:
            data.append(message)
        return data[:100]

    if query.recepient_id:
        cursor = (
            r.table("messages")
            .filter(
                (r.row["recepient_id"] == query.recepient_id)
                & (r.now() - r.row["date"] < (60 * 60 * 24 * 30))
            )
            .run()
        )

        for message in cursor:
            data.append(message)
        return data[:100]


def post_data(message: Message):
    return r.table("messages").insert(dict(message)).run()
