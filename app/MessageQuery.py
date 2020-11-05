from pydantic import BaseModel, validator

"""  Model for MessageQuery object, includes validators to ensure proper data types are being passed in prior to creating a class instance."""


class MessageQuery(BaseModel):
    sender_id: int = None
    recipient_id: int = None

    @validator("sender_id")
    def validate_sender_id(cls, sender_id) -> int:
        if sender_id:
            if not isinstance(sender_id, int):
                raise ValueError("Must be Int")
        return sender_id

    @validator("recipient_id")
    def validate_recipient_id(cls, recipient_id) -> int:
        if recipient_id:
            if not isinstance(recipient_id, int):
                raise ValueError("Bad value type, must be Int")
        return recipient_id
