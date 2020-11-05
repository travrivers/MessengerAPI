from rethinkdb import RethinkDB

from app.Message import Message
from app.MessageQuery import MessageQuery

r = RethinkDB()
r.connect("database", 28015).repl()


def get_data(query: MessageQuery = None):
    data = []

    if query.sender_id == None and query.recipient_id == None:
        cursor = (
            r.table("messages")
            .filter(r.now() - r.row["date"] < (60 * 60 * 24 * 30))
            .run()
        )
        for message in cursor:
            data.append(message)
        return data[:100]

    if query.sender_id and query.recipient_id:
        cursor = (
            r.table("messages")
            .filter(
                (r.row["sender_id"] == query.sender_id)
                & (r.row["recipient_id"] == query.recipient_id)
                & (r.now() - r.row["date"] < (60 * 60 * 24 * 30))
            )
            .run()
        )

        for message in cursor:
            data.append(message)
        data = data[:100]
        data.sort(key=lambda x: x["date"])
        return data

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
        data = data[:100]
        data.sort(key=lambda x: x["date"])
        return data

    if query.recipient_id:
        cursor = (
            r.table("messages")
            .filter(
                (r.row["recipient_id"] == query.recipient_id)
                & (r.now() - r.row["date"] < (60 * 60 * 24 * 30))
            )
            .run()
        )

        for message in cursor:
            data.append(message)
        data = data[:100]
        data.sort(key=lambda x: x["date"])
        return data


def post_data(message: Message):
    r.table("messages").insert(dict(message)).run()

    return {"status": "Message Sent", "message": dict(message)}
