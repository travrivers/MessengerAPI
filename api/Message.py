from datetime import datetime
from random import randint
from typing import Any

from pydantic import BaseModel, validator
from rethinkdb import RethinkDB

""" Model for a Message object, includes validators to ensure the correct data types
    are being used prior to creating a class instance. """

r = RethinkDB()


class Message(BaseModel):
    sender_id: int
    recipient_id: int
    message: str
    date: datetime = datetime.now(r.make_timezone("-07:00"))

    @validator("sender_id")
    def validate_sender_id(cls, sender_id) -> int:
        if sender_id:
            if not isinstance(sender_id, int):
                raise ValueError("Must be int")
        return sender_id

    @validator("recipient_id")
    def validate_recipient_id(cls, recipient_id) -> int:
        if recipient_id:
            if not isinstance(recipient_id, int):
                raise ValueError("Bad value type, must be int")
        return recipient_id

    @validator("message")
    def validate_message(cls, message) -> int:
        if message:
            if not isinstance(message, str):
                raise ValueError("Bad value type, must be string")
        return message


# Messages to seed DB
MESSAGES = [
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Anyway, dogs are great",
        date="2020-11-04T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Hey, this message is super boring",
        date="2020-11-02T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Please go vote",
        date="2020-11-03T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Bubble sort is the most efficient sorting algorithm",
        date="2020-10-28T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
    Message(
        sender_id=randint(1, 10),
        recipient_id=randint(1, 10),
        message="Greetings",
        date="2020-10-01T21:16:57.652Z",
    ),
]
