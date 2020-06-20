from .Entry import Entry


class SQSmessageBuilderClient:

    def __init__(self, batch_id: str):
        self._id = batch_id
        self._entries = list()

    def construct(self, msg_id: str, msg_body: str, msg_delay: int = 0, msg_attributes: dict = {}):
        entry = Entry(Id= msg_id, MessageBody = msg_body, DelaySeconds= msg_delay, MessageAttributes=msg_attributes)
        self._entries.append(entry.__dict__)

    def get_message_entries(self):
        return self._entries
