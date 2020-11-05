from datetime import datetime
from typing import List

from fastapi import FastAPI, Request, Response, Depends
from starlette.responses import RedirectResponse, Response

from api.Message import Message
from api.MessageQuery import MessageQuery
from db.message_db import get_data, post_data


app = FastAPI(docs_url="/docs", root_path="/")

# Parses query parameters from get_messages into MessageQuery object
def get_message_query(sender_id: int = None, recipient_id: int = None) -> MessageQuery:
    query = MessageQuery(sender_id=sender_id, recipient_id=recipient_id)
    return query


# Parses message paremeters from post_message into Message object
def get_message(sender_id: int, recipient_id: int, message: str) -> Message:
    message = Message(sender_id=sender_id, recipient_id=recipient_id, message=message,)
    return message


# Url endpoints, root redirects to API docs
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse("/docs")


@app.get("/messages/", response_model=List[Message])
async def get_messages(query: MessageQuery = Depends(get_message_query)) -> Response:
    return get_data(query)


@app.post("/messages/")
async def post_message(message: Message):
    return post_data(message)
